questions = [
    {"q": "What is the capital of France?", "options": ["A: Paris", "B: London", "C: Berlin"], "ans": "A"},
    {"q": "What is 2 + 2?", "options": ["A: 3", "B: 4", "C: 5"], "ans": "B"},
    {"q": "Largest planet?", "options": ["A: Earth", "B: Mars", "C: Jupiter"], "ans": "C"}
]

def run_quiz():
    score = 0
    for q in questions:
        print(q["q"])
        for opt in q["options"]:
            print(opt)
        ans = input("Answer (A/B/C): ").upper()
        if ans == q["ans"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! Correct: {q['ans']}")
    print(f"Score: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Trivia Quiz!")
    run_quiz()
