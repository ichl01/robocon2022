from operator import truediv
import RPi.GPIO as GPIO
from time import sleep
import time 
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

def forward(motor):
	if motor == 1:
      print("forward:"+motor)
      GPIO.output(27, GPIO.HIGH)
	elif motor == 2:
      print("forward:"+motor)
		GPIO.output(22, GPIO.HIGH)
	else:
		print("forward:"+motor)
		GPIO.output(17, GPIO.HIGH)

def stop(motor):
   if motor == 1:
		print("stop:"+motor)
      GPIO.output(27, GPIO.LOW)
	elif motor == 2:
		print("stop:"+motor)
      GPIO.output(22, GPIO.LOW)
   else:
		print("stop:"+motor)
      GPIO.output(17, GPIO.LOW)
def reading(sensor): 
   TRIG = 16
   ECHO = 6
     
	if sensor == 0:
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG, GPIO.LOW)
		time.sleep(0.3)
         
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
 
		while GPIO.input(ECHO) == 0:
       signaloff = time.time()
         
		while GPIO.input(ECHO) == 1:
       signalon = time.time()
 
		timepassed = signalon - signaloff
		distance = timepassed * 17000
		return distance
	else:
        print "Incorrect usonic() function varible."
while True:
   print("Started")
	while True:
		x = reading(0)
		if x =>	130:
			break
		else:
			print(x)
			sleep(1)
		
   #リバース
	forward(3)
	sleep(10)
	stop(3)
	
	sleep(20)
	
   #1枚目のフリップ
   forward(1)
   sleep(1)
   stop(1)

   sleep(30)#フリップ間の待ち時間

   #2枚目のフリップ
   forward(2)
   sleep(1)
   stop(2)
	break
GPIO.cleanup()