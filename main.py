import random

# Function to generate a random multiplication question
def generate_question():
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    answer = num1 * num2
    return num1, num2, answer

# Function to check the user's answer
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Initialize the score
score = 0

# Run the multiplication test with 10 questions
for _ in range(10):
    # Generate a question
    num1, num2, correct_answer = generate_question()

    # Prompt the user for an answer
    user_answer = int(input(f"{num1} x {num2} = "))

    # Check the answer and provide feedback
    if check_answer(user_answer, correct_answer):
        print("Correct!")
        score += 1
    else:
        print(f"Gah! That's not right! The correct answer is {correct_answer}")

# Display the final score
print(f"You got {score} right!")
