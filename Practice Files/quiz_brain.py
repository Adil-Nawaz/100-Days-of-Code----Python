class QuizBrain:
    def __init__(self, q_list):
        self.questionNumber = 0
        self.questionList = q_list
        self.score = 0
        
    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        questionText = currentQuestion.text
        originalAnswer = currentQuestion.answer
        self.questionNumber += 1
        userResponse = input(f"Q. No. {self.questionNumber}: {questionText} (True / False)? ")
        self.checkAnswer(userResponse, originalAnswer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)
    
    def checkAnswer(self, response, correctAnswer):
        if response.lower() == correctAnswer.lower():
            self.score +=1
            print("You got it right! ")
        else:
            print(f"You are wrong! Correct Answer is: {correctAnswer} ")
        print(f"Your current score is: {self.score} / {self.questionNumber}\n")
