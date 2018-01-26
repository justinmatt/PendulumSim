from Core.pendulum import pendulum
from visual import *
import sys  

def main():
    length=abs(input("Length of pendulum :"))   
    g=abs(input("Acceleration due to gravity :"))

    print "Give amplitude of oscillation (Value should be less than)",length #Maximum distance bob covers in x-axis
    
    amplitude=input("Amplitude :")
    if amplitude > length :                                                #Maximum distance bob covers in x-axis cannot exceed the length of pendulum
        print "Illegal value.Value of amplitude should be less",length
        sys.exit()
 
  
    pendulum(length,g,amplitude)


if __name__== '__main__':
    main()
