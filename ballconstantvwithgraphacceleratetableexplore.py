from vpython import *
#Web VPython 3.2
#Set up a python graph
g1=graph(width=400,height=200,xtitle='time',ytitle='position')
yDots=gdots(color=color.green,graph=g1)
g2=graph(width=400,height=200,xtitle='time',ytitle='velocity')
vyDots=gdots(color=color.black,graph=g2)

#defining the object and constant velocity
obj=sphere(pos=vector(0,-1,0),radius=0.4,color=color.red,make_trail=True)

b=box(pos=vector(0,-6,0),size=vector(20,1,10),color=color.white)
#Set initial conditions and velocity

t=0
dt=0.05
y0=-1
v0=0
g=9.8
x=0

##switch to y and add acceleration
##The main part ( a loop to move the ball)
q=True
print(q)
y=y0
while q:
 #   q=(t<2 and -4.4<=y)
    yold=y
    print(q)
    rate(10)
    obj.pos=vector(x,y,0)
    yDots.plot(t,y)
    vyDots.plot(t,v0-g*t)
    t=t+dt
    if (y<-5):
        print('unphysical solution')
        q=False
        y=yold
        x=x+t
        q=True
    else:
        print('things are good')
        y=y0+v0*t-0.5*g*t*t


