from visual import*

def pendulum(length,acceleration_due_to_gravity,amplitude):
    l=length
    g=acceleration_due_to_gravity+0.0   #0.0 is added to avoid type divison error
    A=amplitude
    t=0
    dt=0.01
    T=2*pi*sqrt(l/g)                    #Calculate the time period of pendulum
    omega=2*pi/T                        #Angular frequency of pendulum
     
    bob=sphere(pos=(A,A),radius=1,material=materials.rough,color=color.yellow,make_trail=False,visible=True)
    string=cylinder(pos=(0,l),radius=0.05,axis=(0,-l),color=color.blue,visible=True)
    roof=box(pos=(0,l),size=(4,0.06,4),color=color.red,material=materials.silver)
    scene.waitfor('click')  

    while True:                         #To continue execution for infinite time
        rate(250)                       #Number of execution of below code per second 
        bob.pos.x=A*sin(omega*t)        #calculate position of bob in X-axis
        bob.pos.y=l-sqrt(l**2 - bob.pos.x**2)   #calculate position of bob in Y-axis
        string.axis=bob.pos-string.pos          #changes the position of string axis with change in bob position
        t=t+dt

    
