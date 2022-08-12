#code made in class with teacher ariel
#A01753176 Gilberto André García Gaytán
from math import sqrt
from turtle import circle, fd, pencolor, pensize,rt, done, circle, pencolor, pensize, speed

PHI = 1 / ((sqrt(5) - 1) / 2)

#def square(n: int):
  #  for _ in range(4):
   #     fd(n)
     #   rt(90)
     
def spiral(times: int) -> None:
    lenght = 5
    for _ in range(times):
        circle(lenght, 90)
        lenght *= PHI

if __name__ == '__main__': 
   # for _ in range(36):
      #  square(100)      
      #  rt(10)
    pensize(10)
    speed(10)
    pencolor('medium purple')
    spiral(10)
    done()