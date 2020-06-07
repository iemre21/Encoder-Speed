
import RPi.GPIO as GPIO
import threading
from time import sleep

Enc_A = 11
Enc_B = 8

Rotary_counter = 0
Current_A = 1
Current_B = 1

LockRotary = threading.Lock()
	

def encoder_init():
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)
    
	GPIO.setup(Enc_A, GPIO.IN)
	GPIO.setup(Enc_B, GPIO.IN)
    
	GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotary_interrupt)
	GPIO.add_event_detect(Enc_B, GPIO.RISING, callback=rotary_interrupt)
	return


def rotary_interrupt(A_or_B):
	global Rotary_counter, Current_A, Current_B, LockRotary
    
	Switch_A = GPIO.input(Enc_A)
	Switch_B = GPIO.input(Enc_B)
        
	if Current_A == Switch_A and Current_B == Switch_B:
		return

	Current_A = Switch_A
	Current_B = Switch_B

	if (Switch_A and Switch_B):
		LockRotary.acquire()
		if A_or_B == Enc_B:
			Rotary_counter += 1
		else:
			Rotary_counter -= 1
		LockRotary.release()
	return


def read_encoder():
    global Rotary_counter, LockRotary, old_counter, precision
    LockRotary.acquire()
    encoder_value2 = Rotary_counter
    LockRotary.release()
    encoder_value1 = encoder_value2/360
    encoder_value = round(encoder_value1)
    return encoder_value

def speed()

	wheel_diameter = 
	one_tour_distance = 2*3.14*wheel_diameter
	commune1 = read_encoder()
	sleep(1)
	commune2 = read_encoder()
	commune_difference = commune2-commune1
	speed = (commune_difference*one_tour_distance)/1
	return speed




        
#read_enc_value()

if __name__ == '__main__':
        encoder_init()
        while True:
                sleep(0.1)
                print(read_encoder())
    




