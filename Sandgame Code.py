# Docstring required at the beginning of every program:
"""
    Description of program: Project 3 - SandGame Part 2
    Filename: Project 3 - Muskan Fatima
    Author: Muskan Fatima
    Date: 27th January 2023
    Course: PROG 1352
    Assignment: Project 3
    Collaborators: -
    Internet Source: Stack Overflow for reference
"""
import dudraw
from random import randint
from random import random

#Initializing variable which correspond to the number of rows and columns of a 2D list

width=100
height=100
scale=5
cells=[[0 for _ in range(width+5)]for _ in range(height+3)]

#setting up the x-scale and y-scale to match the dimensions of the 2d list
dudraw.set_canvas_size(width*scale, height*scale)
dudraw.set_x_scale(0, width)
dudraw.set_y_scale(0,height)

#animation loop
key='s'
frameCount=0
while key!='q':
  frameCount+=1
#checking which keys are pressed
  if dudraw.mouse_is_pressed():
    x=int(dudraw.mouse_x())
    y=int(dudraw.mouse_y())
    if key=='s':
      cells[y+randint(-3, 0)][x+randint(-3, 5)]=1 #sand
    elif key=='f':
        cells[y][x]=2 #floor
    elif key=='w':  #water
        cells[y+randint(-3, 0)][x+randint(-3, 5)]=3 
    elif key=='b':  #water
        cells[y+randint(-3, 0)][x+randint(-3, 5)]=4
#falling sand
  for i in range(height-1):
    for j in range(width):
      if cells[i][j]==0 and cells[i+1][j]==1:
        cells[i][j],cells[i+1][j]=cells[i+1][j], cells[i][j]
#falling water
  for i in range(height-1):
    for j in range(width):
      if cells[i][j]==0 and cells[i+1][j]==3:
        cells[i][j],cells[i+1][j]=cells[i+1][j], cells[i][j]
#falling balls
  for i in range(height-1):
    for j in range(width):
      if cells[i][j]==0 and cells[i+1][j]==4:
        cells[i][j],cells[i+1][j]=cells[i+1][j], cells[i][j]

#jiggle right sand
  if frameCount%10==5:
    for i in range(height-1):
      for j  in reversed(range(width-1)):
        if cells[i+1][j]==1 and cells[i][j+1]==0:
          cells[i+1][j],cells[i][j+1]=cells[i][j+1],cells[i+1][j]

#jiggle left sand
  if frameCount%10==0:
    for i in range(height):
      for j in range(width-1):
        if cells[i+1][j+1]==1 and cells[i][j]==0:
          cells[i+1][j+1],cells[i][j]=cells[i][j+1],cells[i+1][j+1]
          
#jiggle right balls
  if frameCount%10==5:
    for i in range(height-1):
      for j  in reversed(range(width-1)):
        if cells[i+1][j]==4 and cells[i][j+1]==0:
          cells[i+1][j],cells[i][j+1]=cells[i][j+1],cells[i+1][j]

#jiggle left balls
  if frameCount%10==0:
    for i in range(height):
      for j in range(width-1):
        if cells[i+1][j+1]==4 and cells[i][j]==0:
          cells[i+1][j+1],cells[i][j]=cells[i][j+1],cells[i+1][j+1]



#random_swaps for sand
  if frameCount%5==0:
    for i in range(height):
      for j in reversed(range(width-1)):
        if cells[i+1][j]==1 and cells[i][j]==0:
          if randint(0,1)==1:
            cells[i][j+1],cells[i][j]=cells[i][j],cells[i][j+1]  
#random_swaps for water
  if frameCount%5==2:
    for i in range(height):
      for j in range(width-1):
        if cells[i][j]==3 and cells[i][j+1]==0:
          if randint(0,3)==1:
            cells[i][j+1],cells[i][j]=cells[i][j],cells[i][j+1] 
#random_swaps for water
  if frameCount%5==0:
    for i in range(height):
      for j in reversed(range(width-1)):
        if cells[i][j]==0 and cells[i][j+1]==3:
          if randint(0,3)==1:
            cells[i][j+1],cells[i][j]=cells[i][j],cells[i][j+1] 
#random_swaps for balls
  if frameCount%5==0:
    for i in range(height):
      for j in reversed(range(width-1)):
        if cells[i+1][j]==1 and cells[i][j]==4:
          if randint(0,1)==4:
            cells[i][j+1],cells[i][j]=cells[i][j],cells[i][j+1]   
#changing what gets drawn on the screen depending on what's pressed
  for i in range(height):
    for j in range(width):
      if cells[i][j]==1:
        dudraw.set_pen_color(dudraw.ORANGE)
        dudraw.filled_rectangle(j+.5,i+.5, .5,.5)
      elif cells[i][j]==0:
        dudraw.set_pen_color(dudraw.LIGHT_GRAY)
        dudraw.filled_rectangle(j+.5,i+.5, .5,.5)
      elif cells[i][j]==2:
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.filled_rectangle(j+.5,i+.5, .5,.5)
      elif cells[i][j]==3:
        dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
        dudraw.filled_rectangle(j+.5,i+.5, .5,.5)
      elif cells[i][j]==4:
        dudraw.set_pen_color_rgb(int(random()*256), int(random()*256), int(random()*256))
        dudraw.filled_circle(j+.5,i+.5, .5)

#for checking which kdey the user has typed
  if dudraw.has_next_key_typed():
    key=dudraw.next_key_typed()
    
  
  dudraw.show(10)

