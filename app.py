from transformers import pipeline

# بارگذاری مدل آماده از Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result['label'],
        "score": round(result['score'], 3)
    }

if __name__ == "__main__":
    print("=== AI Sentiment Analyzer ===")
    while True:
        user_input = input("Enter your text (or 'exit' to exit): ")
        if user_input.lower() == "exit":
            break
        output = analyze_text(user_input)
        print(f"result: {output['label']} (trust: {output['score']})\n")
