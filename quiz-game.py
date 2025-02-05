def run_quiz(questions):
    """
    Function to run a multiple-choice quiz.
    :param questions: List of question dictionaries containing prompts, options, and answers.
    """
    score = 0
    
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['prompt']}")
        for option in question["options"]:
            print(option)
        
        while True:
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")
    
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
if __name__ == "__main__":
    run_quiz(questions)