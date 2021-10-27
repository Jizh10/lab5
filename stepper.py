import RPi.GPIO as GPIO
import PCF8591 as PCF

class Stepper:
  
  sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
            [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
  halfStepAngle = 360/512
  
  def __init__(pins):
    self.pins = pins
    self.state = 0
    self.angle = 0
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)

  def __halfStep(dir):
    # dir = +/- 1 (ccw / cw)
    self.state += dir
    if self.state > 7:
      self.state = 0
    elif self.state < 0:
      self.state = 7
    
    for pin in range(len(self.pins)):
      GPIO.output(pins[pin], sequence[state][pin])
    delay_us(1000)

    self.angle += dir*halfStepAngle

  def __moveSteps(steps, dir):
    
    for step in steps:
      self.__halfStep(dir)

  def goAngle(angle):
    if angle < self.angle:
      dir = -1
      while angle < self.angle:
        self.__halfStep(dir)
    else:
      dir = 1
      while angle > self.angle:
        self.__halfStep(dir)

  def zero(ldr, ledPin):
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
