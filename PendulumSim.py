
__author__ = 'justin'

from Modules.pendulum import pendulum
from visual import *
import sys  

def main():
    length=abs(input("Length of pendulum :"))   
    g=abs(input("Acceleration due to gravity :"))

    print "Give amplitude of oscillation (Value should be less than)",length #Maximum distance bob covers in x-axis
    
    amplitude=input("Amplitude :")
    if amplitude > length :                                                #Maximum distance bob covers in x-axis should exceed the length of pendulum
        print "Illegal value.Value of amplitude should be less than ",length
        sys.exit()
 
  
    pendulum(length,g,amplitude)  #calling function from Modules 


if __name__== '__main__':
    main()
