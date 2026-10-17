Web VPython 3.2
g = 9.8
L1 = 1
L2 = 1
M1 = 2000
M2 = 1
theta1 = 1.15
theta2 = 2
theta1D = 0
theta2D = 0

x1 = L1*sin(theta1)
y1 = -L1*cos(theta1)
x2 = (L1*sin(theta1))+(L2*sin(theta2))
y2 = (-L1*cos(theta1))-(L2*cos(theta2))

pivot = sphere(pos=vec(0,0,0), radius=0.03, color=color.white, make_trail = False)
ball1 = sphere(pos=vec(x1,y1,0), radius=0.05, color=color.yellow, make_trail = True)
ball2 =  sphere(pos=vec(x2,y2,0), radius=0.05, color=color.yellow, make_trail = True)
arm1 = cylinder(pos=pivot.pos, axis=ball1.pos, color=color.white, size=vec(L1,L1*0.02,L1*0.02))
arm2 = cylinder(pos=ball1.pos, axis=ball2.pos-ball1.pos, color=color.white, size=vec(L2,L2*0.02,L2*0.02))

t = 0
dt = 0.001
while t<100:
    rate(1.0/dt)
    a = -(M1+M2)*g*L1*sin(theta1)-M2*L1*L2*theta2D**2*sin(theta1-theta2)
    b = (M1+M2)*L1**2
    c = M2*L1*L2*cos(theta1-theta2)
    d = -M2*g*L2*sin(theta2)+M2*L1*L2*theta1D**2*sin(theta1-theta2)
    e = M2*L2**2
    f = M2*L1*L2*cos(theta1-theta2)
    theta2DD = (d-a*f/b)/(e-c*f/b)
    theta1DD = a/b - c*theta2DD/b
    theta2D += theta2DD*dt
    theta1D += theta1DD*dt
    theta2 += theta2D*dt
    theta1 += theta1D*dt
    x1 = L1*sin(theta1)
    y1 = -L1*cos(theta1)
    x2 = (L1*sin(theta1))+(L2*sin(theta2))
    y2 = (-L1*cos(theta1))-(L2*cos(theta2))
    ball1.pos = vector(x1,y1,0)
    ball2.pos = vector(x2,y2,0)
    arm1.axis = ball1.pos
    arm2.pos = ball1.pos
    arm2.axis = ball2.pos-ball1.pos
    t += dt
