from transformers import pipeline

بارگذاری مدل آماده از Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result['label'],
        "score": round(result['score'], 3)
    }

if name == "main":
    print("=== AI Sentiment Analyzer ===")
    while True:
        user_input = input("متن خود را وارد کنید (یا 'exit' برای خروج): ")
        if user_input.lower() == "exit":
            break
        output = analyzetext(userinput)
        print(f"نتیجه: {output['label']} (اعتماد: {output['score']})\n")