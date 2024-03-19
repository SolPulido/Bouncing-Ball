import play #loading the play module library 
import random #loading the random library 


width = 300  #defining global varibale for horizontal size of court. 
height = 400  #defining global varibale for vertical size of court.
half_width = width/2 #definig global variables for horizontal size of court 
half_height= height/2 #definig global variables for vertical sie of court

score= 0 #global variable for score 
speed= 3 #global variable for speed of ball 

@play.when_program_starts() #when the program starts  as soon as you press RUN
def doBackground():
  play.set_backdrop(255,204,229) #setting the background color to pink
court = play.new_box() #creating a group for court
color = (128,0,128)
x = 0 #x coodinate of court
y = 0#y coodinate of court 
width=width, #width of court
height=height, #height of court 

paddle = play.new_box(
  color="blue",
  width= 50,
  height= 10, 
  x = 0,
  y = -half_height + 10,
) #creating a group for paddle

#creating a variabale for the text of the score.
#and initilizing it with a build in fuction new text from play module. 
score_text = play.new_text(
 words= "Score : " + str(score),
 x= 0,
 y= half_height + 15 ,
 font = None , 
 color= "Black", 
)
@play.repeat_forever #Creates a key frame as long as the game is playing.
def do(): #define the fuction or subroutine.
  global score #calling for the global varibale score 
  paddle.x= play.mouse.x # DOT notation to recall the x parameter of the paddle and reassigned value to match mouse x coodinates. 
  # to ensure the paddle is not off the playfield 
if play.mouse.x < -half_width + paddle.width/2:
  paddle.x = -half_width + paddle.width/2
  
  if(play.mouse.x > half_width - paddle.width/2):

 ball = play.new_circle()
 #bounce off the top/bottom of the screen 360 angle 
 if (ball.y + ball.radius > half_height):
  ball.angle = 360 - ball.angle 
 #bottom wall
 if (ball.y + ball.radius < -half_height):
  ball.angle = 360 - ball.angle
  score -= 1 # subtracting 1 from the score
 #bounce off the left/right of the screen 180 angle 
 if (ball.x + ball.radius > half_width):
  ball.angle = 180 - ball.angle 
 if (ball.x + ball.radius < -half_width):
  ball.angle = 180 - ball.angle
 #make sure it bouce as if it has hit the bottom , and give it a little change 
 if (ball.is_touching(paddle)):
  ball.angle %= 360
 if (ball.angle < 20):
  ball.angle= 20
 elif(ball.angle > 160):
  ball.angle =160 
 if (score == 5):
   paddle.width -= 5
   