from vpython import *
#Web VPython 3.2
#Circular planetary motion
obj=sphere(pos=vector(10,0,0),radius=0.5,color=color.red,make_trail=True)
sun=sphere(pos=vector(0,0,0),radius=1.0,color=color.yellow)

#initial conditions, stepsize, frequency
t=0
dt=1
y0=2
y0=0.0
theta=0.0
thetavenus=0
omega=2*pi/365

while True:
    rate(10)
    x=10*cos(theta)
    y=10*sin(theta)


    theta=omega*t
    t=t+dt
    obj.pos=vector(x,y,0)
