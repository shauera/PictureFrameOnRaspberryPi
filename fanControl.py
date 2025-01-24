import os
import re
import time
import RPi.GPIO as GPIO

def main():
    try:
        print("start fans")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(5,GPIO.OUT)
        my_pwm = GPIO.PWM(5,40)

        while True:
            rawTmpr = os.popen("vcgencmd measure_temp").readline()
            tmpr = [float(s) for s in re.findall(r'-?\d+\.?\d*', rawTmpr)][0]
            if tmpr <= 40:
                my_pwm.start(0)
                GPIO.output(3,False)
            elif tmpr > 40 and tmpr <= 60:
                my_pwm.start((tmpr-40)*5)
                GPIO.output(3,False)
            elif tmpr > 60 and tmpr <= 75:
                my_pwm.stert(100)
                GPIO.output(3,False)
            else:
                my_pwm.start(100)
                GPIO.output(3,True)

            print(tmpr)
            time.sleep(10)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    print (__name__)
    main()