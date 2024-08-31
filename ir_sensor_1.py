from machine import Pin
import utime
from time import sleep
import random


sensor_left = Pin(14, Pin.IN) # left
sensor_center = Pin(15, Pin.IN) # center
sensor_right = Pin(16, Pin.IN) # right

motor1_GP18 = Pin(18, Pin.OUT)
motor1_GP19 = Pin(19, Pin.OUT)

motor2_GP21 = Pin(21, Pin.OUT)
motor2_GP20 = Pin(20, Pin.OUT)

"""
def obstacle():
    while True:
    
        if sensor_center.value() == 1:
            sensor_center_val=1
        else:
            sensor_center_val=0
        
        if sensor_left.value() == 1:
            sensor_left_val=0
        else:
            sensor_left_val=1
        
        if sensor_right.value() == 1:
            sensor_right_val=0
        else:
            sensor_right_val=1
    #print("sensor left "+str(sensor_left.value())+" sensor center "+str(sensor_center_val)+" sensor right "+str(sensor_right.value()))
    
    
    utime.sleep_us(1000)
    
"""

"""
        each sensor give 1 when no obstruction
        give 0 when obsrtuction
"""
def obstacle():
       
    if sensor_center.value() == 1:
        sensor_center_val=1
        
    else:
        sensor_center_val=0
     #   return "centre"
    if sensor_left.value() == 1:
        sensor_left_val=0
        
    else:
        sensor_left_val=1
       # return "left"
        
    if sensor_right.value() == 1:
        sensor_right_val=0
        
    else:
        sensor_right_val=1
    #return "clear"
   # print("sensor left "+str(sensor_left.value())+" sensor center "+str(sensor_center_val)+" sensor right "+str(sensor_right.value()))
    
    return str(sensor_left.value())+str(sensor_center_val)+str(sensor_right.value())
    
    

    
def forward():
    
    motor1_GP18.value(1)
    motor1_GP19.value(0)
    
    motor2_GP21.value(1)
    motor2_GP20.value(0)
    

def backward():
    
    motor1_GP18.value(0)
    motor1_GP19.value(1)
    
    motor2_GP21.value(0)
    motor2_GP20.value(1)
    
def stop():
    
    motor1_GP18.value(0)
    motor1_GP19.value(0)
    
    motor2_GP21.value(0)
    motor2_GP20.value(0)
    
def left():
    
    motor1_GP18.value(1)
    motor1_GP19.value(0)
    
    motor2_GP21.value(0)
    motor2_GP20.value(1)

def right():
    
    motor1_GP18.value(0)
    motor1_GP19.value(1)
    
    motor2_GP21.value(1)
    motor2_GP20.value(0)
    
'''   
forward()
sleep(5)
stop()
sleep(5)
backward()
sleep(5)
left()
sleep(20)
stop()
'''
while True:
    print(obstacle())
    utime.sleep_us(500)

    
    forward()
    #right obstruction
    if obstacle() =="110": 
        backward()
        sleep(2)
        left()
        sleep(2)
    elif obstacle() =="011": 
        backward()
        sleep(2)
        right()
        sleep(2)
    elif obstacle() =="101": 
        backward()
        sleep(2)
        
        # Generate either 0 or 1 randomly
        random_number = random.randint(0, 1)
        
        if random_number==1:
            right()
            sleep(2)
        else:   
            left()
            sleep(2)
#stop()