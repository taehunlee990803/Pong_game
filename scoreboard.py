from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.pencolor("white")
        self.goto(-150, 200)
        self.write(f"{self.l_score}", True, align="center",
                   font=('Arial', 80, 'normal'))
        self.goto(150,200)
        self.write(f"{self.r_score}", True, align="center",
                   font=('Arial', 80, 'normal'))

    def left_win(self):
        self.clear()
        self.l_score += 1
        self.goto(-150, 200)
        self.write(f"{self.l_score}", True, align="center",
                   font=('Arial', 80, 'normal'))
        self.goto(150, 200)
        self.write(f"{self.r_score}", True, align="center",
                   font=('Arial', 80, 'normal'))

    def right_win(self):
        self.clear()
        self.r_score += 1
        self.goto(-150, 200)
        self.write(f"{self.l_score}", True, align="center",
                   font=('Arial', 80, 'normal'))
        self.goto(150, 200)
        self.write(f"{self.r_score}", True, align="center",
                   font=('Arial', 80, 'normal'))

    def final_check(self):
        if self.r_score == 3:
            self.clear()
            self.goto(0,0)
            self.write("Winner is right", True, align="center",
                       font=('Arial', 60, 'normal'))
            return True

        elif self.l_score == 3:
            self.clear()
            self.goto(0,0)
            self.write("Winner is left", True, align="center",
                       font=('Arial', 60, 'normal'))
            return True
