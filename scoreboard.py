from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.high_score = 0
        # with open("Scores.txt", "r") as file:
        #     data = file.readlines()
        #     for line in data:
        #         print(line)
        #         if int(line[-2]) >= self.high_score and line != "\n":
        #             self.high_score = int(line[-2])
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}\tHigh Score = {self.high_score}",
                   align="center", font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     # self.write("Game Over\n\nCreated by:\nSarthak Tharaney\nClass: BSc CM\n
    #     Reg. No.: 2243123", align="center", font=("Courier", 12, "normal"))

    def reset(self, name):
        if self.score > self.high_score:
            self.high_score = self.score
        # file = open("Scores.txt", "a+")
        # file.write(f"{name}: {self.score}\n")
        # file.close()
        self.score = 0
        self.update_score()



