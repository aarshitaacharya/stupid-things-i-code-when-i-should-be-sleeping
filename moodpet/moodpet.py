import random

RESPONSES = {
    "happy": ["Yay! 😄 I'm happy too!", "So much joy! 🌸"],
    "sad": ["Oh no 😢 Want a hug?", "Don’t worry, clouds cry sometimes ☁️"],
    "angry": ["Grr 😤 Let’s take deep breaths.", "Anger is just passion 🔥"],
    "neutral": ["Hmm... feeling chill today? 😌", "I'm here if you want to talk! 🐰"]
}

def mood_detect(text):
    text = text.lower()

    if any(word in text for word in ['happy', 'great', 'love', 'yay']):
        return "happy"
    if any(word in text for word in ["sad", "tired", "lonely", "cry"]):
        return "sad"
    if any(word in text for word in ["angry", "mad", "upset"]):
        return "angry"
    return "neutral"

def main():
    print("🐰 Hi! I'm MoodPet, your terminal friend!")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("🐰: Bye-bye!")
            break
        
        mood = mood_detect(user_input)
        print("🐰: ",random.choice(RESPONSES[mood]))

if __name__ == "__main__":
    main()