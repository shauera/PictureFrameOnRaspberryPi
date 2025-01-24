import os
import time
import RPi.GPIO as GPIO

# main function
def main():
        try:
                os.system ("vcgencmd display_power 0")
                GPIO.setmode(GPIO.BOARD)

                GPIO.setup(12, GPIO.IN)
                #GPIO.add_event_detect(12, GPIO.FALLING, callback=motionDetectedEventHandler)

                print "Waiting for sensor to settle"
                time.sleep(2)

                print "Starting motion detection"
                maxTimeToSleep = 300
                remainingTime = 0
                while True:
                        if GPIO.input(12):
                                print "Motion Detected!"
                                remainingTime = maxTimeToSleep
                                os.system ("vcgencmd display_power 1")

                        if remainingTime > 0:
                                remainingTime -= 2
                        else:
                                os.system ("vcgencmd display_power 0")

                        time.sleep(2)

        finally:
                GPIO.cleanup()

if __name__ == "__main__":
        print (__name__)
        main()