from turtle import Turtle
STARTING_POSITIONS = ((0, 0), (0, -20), (0, -40))


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def add_segments(self, position):
        t = Turtle()
        t.penup()
        # t.speed("fastest")
        t.color("white")
        t.shape("square")
        t.goto(position)
        self.segments.append(t)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def lft(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def rgt(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def collision(self):
        # if self.head.position() in [pos.position() for pos in self.segments[1:]]:
        #     return True
        for segment in self.segments:
            if segment == self.head:
                pass

            elif self.head.distance(segment) < 10:
                return True

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
