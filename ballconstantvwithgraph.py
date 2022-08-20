from vpython import *
#Web VPython 3.2
#Set up a python graph
g1=graph(width=400,height=200,xtitle='time',ytitle='position')
xDots=gdots(color=color.green,graph=g1)

#defining the object and constant velocity
obj=sphere(pos=vector(-1,0,0),radius=0.1,color=color.red,make_trail=True)

#Set initial conditions and velocity
t=0
dt=0.05
x0=-1
v0=1


#The main part ( a loop to move the ball)
while t<2:
    rate(10)
    x=x0+v0*t
    obj.pos=vector(x,0,0)
    xDots.plot(t,x)
    t=t+dt

