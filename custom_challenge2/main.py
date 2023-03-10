

def quiz_game():
    print()
    class QuizQuestion():
        def __init__(self, question, answer1, answer2, answer3):
            self.question = question
            self.correctAnswer = answer1
            self.wrongAswer1 = answer2
            self.wrongAswer2 = answer3


    quiz_question = [QuizQuestion("How much is 1+1", "2", "3", "0"), QuizQuestion("")]

    def print_question_and_answers(quiz_question):
        print(quiz_question.question)
        # randomize n=[1-3], if n=1: correct, wrong1, wrong2, if n=2: wrong1, correct, wrong2, n=3: wrong1, wrong2, correct
        if n==1:
            print("1 - "+quiz_question.correctAnswer+" 2- "+quiz_question.wrongAnswer1+" 3 - "+quiz_question.wrongAnswer2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    quiz_game()

