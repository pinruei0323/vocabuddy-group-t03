import os, sys, json, argparse
import anthropic
import requests

MODEL = "claude-sonnet-5-5"   # 最新名稱見附錄 B
LOCAL_MODELS = ["qwen3.5:4b", "qwen2.5:14b", "yet_another_model:1b"]    # 與 ollama pull 的一致；這台電腦 4 GB 顯存，選小型號
SYSTEM = "你是高中英語老師。只輸出 JSON。"
PROMPT = ("為英文單字「{word}」產生學習卡內容。只回傳 JSON，不要其他文字，不要 markdown 圍欄，"
          '格式：{{"word": "...", "sentence": "...", "zh": "...", "tip": "..."}}。'
          "sentence 用 CEFR B1 難度，且必須包含該單字。")
FALLBACK = {"sentence": "Practice makes perfect.",
            "zh": "熟能生巧。", "tip": "（預設內容：AI 暫時不可用）"}

def text_of(msg):                         # 依 type 只挑文字區塊，理由同 v1
    return "".join(b.text for b in msg.content if b.type == "text")

def ask_claude(prompt, system=SYSTEM):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("沒有 API key")  # 沒 key 就讓切換器換下一條路
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL, max_tokens=1024,     # JSON 約 150～200 token，留餘裕給可能出現的 thinking
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return text_of(msg)

def ask_local(prompt, system=SYSTEM):
    for model in LOCAL_MODELS:
        try:
            r = requests.post(f"http://localhost:11434/api/chat", json={
                "model": model,
                "messages": [{"role": "system", "content": system},
                             {"role": "user", "content": prompt}],
                "stream": False,
                "think": False,   # qwen3.5 預設先思考：實測 4 GB 顯存要 3 分鐘，關掉約 10 秒
            }, timeout=180)
            r.raise_for_status()
            return r.json()["message"]["content"]
        except Exception as e:
            #print(f"[{model}] 失敗：{type(e).__name__}", file=sys.stderr)
            continue
    return None

ASK = {"claude": ask_claude, "local": ask_local}   # 兩個同形的函式
CHAIN = {"claude": ["claude"], "local": ["local"],
         "auto": ["claude", "local"]}               # auto：雲端優先、本地備援

def generate(word, provider="auto"):
    for name in CHAIN[provider]:
        for attempt in range(2):          # 每條路失敗最多重試一次
            try:
                data = json.loads(ASK[name](PROMPT.format(word=word)))
                if word.lower() in data["sentence"].lower():
                    data["by"] = name     # 記錄這筆是誰生成的
                    return data
            except Exception as e:
                print(f"[{name}] 第 {attempt + 1} 次失敗：{type(e).__name__}", file=sys.stderr)
                continue                  # 這條路不通，換下一條
    return {"word": word, "by": "fallback", **FALLBACK}   # 降階：永遠有東西可給

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VocaBuddy 例句生成 CLI")
    parser.add_argument("word", nargs="?", default="interval")
    parser.add_argument("--provider", choices=CHAIN, default="auto")
    args = parser.parse_args()
    print(json.dumps(generate(args.word, args.provider), ensure_ascii=False, indent=2))
