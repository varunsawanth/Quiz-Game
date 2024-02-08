import random

class Question:
  def __init__(self, text, options, answer, feedback):
    self.text = text
    self.options = options
    self.answer = answer
    self.feedback = feedback

  def display(self):
    print(f"\n{self.text}")
    for i, option in enumerate(self.options):
      print(f"{i+1}. {option}")

  def check_answer(self, user_choice):
    if user_choice == self.answer:
      return True, self.feedback["correct"]
    else:
      return False, self.feedback["incorrect"]

class Quiz:
  def __init__(self, questions, difficulty=1):
    self.questions = questions
    self.score = 0
    self.difficulty = difficulty

  def adjust_difficulty(self, user_performance):
    if user_performance >= 0.8:
      self.difficulty += 1
    elif user_performance < 0.5:
      self.difficulty = max(1, self.difficulty - 1)

  def play(self):
    random.shuffle(self.questions)  # Shuffle questions for each play
    for question in self.questions:
      question.display()
      user_choice = input("Your answer: ")
      is_correct, feedback = question.check_answer(user_choice)
      if is_correct:
        print(feedback)
        self.score += 1
      else:
        print(feedback)

    total_questions = len(self.questions)
    performance = self.score / total_questions
    print(f"\nYour final score: {self.score} out of {total_questions}")
    print(f"Your performance: {performance:.2f}")
    self.adjust_difficulty(performance)


questions = [
  Question(
    "What is the capital of France?",
    ["Berlin", "London", "Paris", "Madrid"],
    2,
    {"correct": "Excellent!", "incorrect": "Hmm, close enough!"},
   # difficulty=1
  ),
  Question(
    "What is the square root of 16?",
    ["3", "4", "5", "6"],
    1,
    {"correct": "You got it!", "incorrect": "Think about perfect squares!"},
   # difficulty=2
  ),
  Question(
    "What is the largest ocean on Earth?",
    ["Pacific", "Atlantic", "Arctic", "Indian"],
    0,
    {"correct": "That's right!", "incorrect": "Remember the map!"},
   # difficulty=3
  ),
]


quiz = Quiz(questions)
difficulty_chosen = int(input("Choose difficulty (1-easy, 2-medium, 3-hard): "))
quiz.difficulty = difficulty_chosen
quiz.play()


play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
  quiz.play()

