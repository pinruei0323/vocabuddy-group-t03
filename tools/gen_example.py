import os
import sys
import anthropic

MODEL = "claude-sonnet-5-5"   # 模型名稱會更新，最新值見附錄 B

def text_of(msg):
    """回應的 content 是「區塊列表」，新模型常先回一個 thinking 區塊，
    所以依 type 只挑文字區塊接起來；直接拿 content[0].text 會失敗（見 2.5）。"""
    return "".join(b.text for b in msg.content if b.type == "text")

def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("還沒設定環境變數 ANTHROPIC_API_KEY，回到步驟 1。")
    word = sys.argv[1] if len(sys.argv) > 1 else "interval"
    client = anthropic.Anthropic()   # 自動讀取環境變數的 key
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,             # 含 thinking 的 token；300 會被「想」掉，印出空白
        system="你是高中英語老師，例句使用 CEFR B1 難度。",
        messages=[{"role": "user",
                   "content": f"用單字 {word} 造一個例句，附中文翻譯與一個好記的聯想。"}],
    )
    print(text_of(msg))

if __name__ == "__main__":
    main()
