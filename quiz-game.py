def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "Which symbol is used to end a statement in C?",
        "options": ["A. .", "B. ;", "C. :", "D. ,"],
        "answer": "B"
    },
    {
        "prompt": "Which data type is used to store decimal numbers in C?",
        "options": ["A. int", "B. char", "C. float", "D. bool"],
        "answer": "C"
    },
    {
        "prompt": "What is the file extension of a Java source file?",
        "options": ["A. .class", "B. .java", "C. .jav", "D. .jv"],
        "answer": "B"
    },
    {
        "prompt": "Which keyword is used to define a class in Java?",
        "options": ["A. class", "B. Class", "C. define", "D. struct"],
        "answer": "A"
    }
]

# Run the quiz
run_quiz(questions)
