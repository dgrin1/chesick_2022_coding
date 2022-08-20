from vpython import *
#Web VPython 3.2
#Set up a python graph
g1=graph(width=400,height=200,xtitle='time',ytitle='position')
yDots=gdots(color=color.green,graph=g1)

#defining the object and constant velocity
obj=sphere(pos=vector(0,-1,0),radius=0.4,color=color.red,make_trail=True)

b=box(pos=vector(0,-6,0),size=vector(20,1,1),color=color.red,make_trail=True)
#Set initial conditions and velocity

t=0
dt=0.05
y0=-1
v0=1
g=9.8

##switch to y and add acceleration
##The main part ( a loop to move the ball)
while (t<2):
    rate(10)
    y=y0+v0*t-0.5*g*t*t
    obj.pos=vector(0,y,0)
    yDots.plot(t,y)
    t=t+dt
         

