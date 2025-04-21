# growth_mindset.py

def show_intro():
    print("🌱 Welcome to the Growth Mindset Reflector!")
    print("This tool will help you shift from a fixed mindset to a growth mindset.")
    print("Let's begin...\n")

def mindset_quiz():
    questions = [
        {
            "fixed": "I give up when things get tough.",
            "growth": "I try different strategies when I face difficulties."
        },
        {
            "fixed": "I’m either good at something or I’m not.",
            "growth": "I can improve with effort and practice."
        },
        {
            "fixed": "I don’t like challenges.",
            "growth": "Challenges help me grow and learn."
        },
        {
            "fixed": "I avoid feedback.",
            "growth": "I learn from feedback and use it to improve."
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(f"1️⃣ {q['fixed']}")
        print(f"2️⃣ {q['growth']}")
        choice = input("Which statement do you relate to more? (1 or 2): ")

        if choice == "2":
            score += 1

    return score

def final_message(score):
    print("\n✨ Reflection Result ✨")
    if score == 4:
        print("You're already practicing a strong growth mindset! Keep going! 🚀")
    elif 2 <= score <= 3:
        print("You're on the right path! Keep working on your mindset 💪")
    else:
        print("It’s never too late to start believing in growth. You got this! 🌟")

def main():
    show_intro()
    score = mindset_quiz()
    final_message(score)

if __name__ == "__main__":
    main()
