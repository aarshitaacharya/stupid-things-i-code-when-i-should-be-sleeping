import random
import json
import os

RESPONSES = {
    "happy": ["Yay! 😄 I'm happy too!", "So much joy! 🌸"],
    "sad": ["Oh no 😢 Want a hug?", "Don’t worry, clouds cry sometimes ☁️"],
    "angry": ["Grr 😤 Let’s take deep breaths.", "Anger is just passion 🔥"],
    "neutral": ["Hmm... feeling chill today? 😌", "I'm here if you want to talk! 🐰"]
}

COMPLIMENTS = [
    "You’re doing amazing, btw 💫",
    "I’d totally star your GitHub repo 🌟",
    "You have great typing rhythm, like poetry on a keyboard 🎶",
    "Your code smells like perfection 😌",
    "You’re my favorite human today 🐰"
]
MOOD_FILE = "mood.json"

def mood_detect(text):
    text = text.lower()

    if any(word in text for word in ['happy', 'great', 'love', 'yay']):
        return "happy"
    if any(word in text for word in ["sad", "tired", "lonely", "cry"]):
        return "sad"
    if any(word in text for word in ["angry", "mad", "upset"]):
        return "angry"
    return "neutral"


def get_past_mood():
    if not os.path.exists(MOOD_FILE):
        return "neutral"
    with open(MOOD_FILE, 'r') as file:
        return json.load(file).get("mood", "neutral")
    
def save_mood(mood):
    with open(MOOD_FILE, 'w') as file:
        json.dump({"mood": mood}, file)


def main():
    print("🐰 Hi! I'm MoodPet, your terminal friend!")
    past_mood = get_past_mood()
    print(f"🐰: I remember last time you were feeling {past_mood}!")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("🐰: Bye-bye!")
            break
        
        mood = mood_detect(user_input)
        save_mood(mood)
        print("🐰: ",random.choice(RESPONSES[mood]))

        if random.random() < 0.3:
            print(f"🐰: ",random.choice(COMPLIMENTS))

if __name__ == "__main__":
    main()