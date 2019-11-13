from turtle import Turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle__init__(self)
		self.penup()
		self.dx = dx
		self.dy = dy
		self.shape(circle) 
		self.color("color")
		self.r = r
		self.size(self.r/15)
		def move(self,screen_width,screen_height):
			current_x = self.xcor()
			newX = current_x + self.dx
			current_y = self.ycor()
			newY + current_y + self.dy
			right_side_ball = newX + self.r
			left_side_ball = newX + self.r
			upper_side_ball = newY + self.r
			lower_side_ball = newY + self.r
			if right_side_ball >screen_width:
				newX = newX

			if left_side_ball< -screen_width:
				newX = newX

			if lower_side_ball< -screen_height:
				newY = newY

			if upper_side_ball> screen_height:
				newY = newY
		self.goto(newX, newY)
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
ball = Ball(5,"red",12,3)

		

