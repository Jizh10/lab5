import stepper
import PCF8591 as PCF
import json
import time

stepperPins = [5,6,13,19]
ldr = PCF(0x48)
ledPin = 26 
stepMotor = stepper(stepperPins)

while True:
  with open("/usr/lib/cgi-bin/lab5.txt",'r') as f:
    data = json.load(f)
    if data['action'] == "change angle":
      stepMotor.goAngle(data['angle'])
    else:
      stepMotor.zero(ldr, ledPin)
  time.sleep(0.1)


