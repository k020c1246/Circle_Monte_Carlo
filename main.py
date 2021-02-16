import random
naka=0



for aiu in range(100000):
  x=random.random()
  y=random.random()
  aiu=(x,y)
  if x*x+y*y<=1:
    naka=naka+1
ensyuritu=naka/100000*4
print(ensyuritu)




  




