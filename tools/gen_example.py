import os, sys, json
import anthropic

MODEL = "claude-sonnet-5-5"   # 最新名稱見附錄 B
PROMPT = ("為英文單字「{word}」產生學習卡內容。只回傳 JSON，不要其他文字，不要 markdown 圍欄，"
          '格式：{{"word": "...", "sentence": "...", "zh": "...", "tip": "..."}}。'
          "sentence 用 CEFR B1 難度，且必須包含該單字。")
FALLBACK = {"sentence": "Practice makes perfect.",
            "zh": "熟能生巧。", "tip": "（預設內容：AI 暫時不可用）"}

def text_of(msg):                         # 依 type 只挑文字區塊，理由同 v1
    return "".join(b.text for b in msg.content if b.type == "text")

def ask(client, word):
    msg = client.messages.create(
        model=MODEL, max_tokens=1024,     # JSON 約 150～200 token，留餘裕給可能出現的 thinking
        system="你是高中英語老師。只輸出 JSON。",
        messages=[{"role": "user", "content": PROMPT.format(word=word)}],
    )
    return text_of(msg)

def generate(word):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("沒有 API key，改用預設內容。", file=sys.stderr)
        return {"word": word, **FALLBACK}
    client = anthropic.Anthropic()        # 建在檢查之後，沒 key 時才接得到降階
    for attempt in range(2):              # 失敗最多重試一次
        try:
            data = json.loads(ask(client, word))
            if word.lower() in data["sentence"].lower():
                return data               # 驗證通過才放行
        except (json.JSONDecodeError, KeyError, TypeError, anthropic.APIError):
            pass
    return {"word": word, **FALLBACK}     # 降階：永遠有東西可給

if __name__ == "__main__":
    word = sys.argv[1] if len(sys.argv) > 1 else "interval"
    print(json.dumps(generate(word), ensure_ascii=False, indent=2))
