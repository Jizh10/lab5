import RPi.GPIO as GPIO
import time

class Stepper:
  
  sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
            [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
  halfStepAngle = 360.0/512.0
  
  def __init__(self, pins):
    self.pins = pins
    self.state = 0
    self.angle = 0
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)

  def __delay_us(self, tus):
    endTime = time.time() + float(tus)/float(1E6)
    while time.time() < endTime:
      pass
    

  def __halfStep(self, dir):
    # dir = +/- 1 (ccw / cw)
    self.state += dir
    if self.state > 7:
      self.state = 0
    elif self.state < 0:
      self.state = 7
    
    print('current angle: %f' % self.angle)

    for pin in range(len(self.pins)):
      GPIO.output(self.pins[pin], Stepper.sequence[self.state][pin])
    self.__delay_us(1000)

    
    print('half step change: %f' % Stepper.halfStepAngle)

    self.angle += dir*Stepper.halfStepAngle
    print('after halfstep: %f' % self.angle)

  def __moveSteps(self, steps, dir):
    
    for step in steps:
      self.__halfStep(dir)

  def goAngle(self, angle):
    if angle < self.angle:
      dir = -1
      while angle < self.angle:
        self.__halfStep(dir)
    else:
      dir = 1
      while angle > self.angle:
        self.__halfStep(dir)

  def zero(self, ldr, ledPin):
    GPIO.output(ledPin, 1)
    ldrVal = ldr.read(0)
    zero = False
    threshVal = 10

    if ldrVal < threshVal:
      zero = True

    while not zero:
      self.__halfStep(1)
      ldrVal = ldr.read(0)
      if ldrVal < threshVal:
        zero = True
    
    GPIO.output(ledPin, 0)
