import RPi.GPIO as GPIO
import time

class Motor():
    def __init__(self) -> None:
        self.in1 = 17
        self.in2 = 18
        self.in3 = 27
        self.in4 = 22
        self.sleep = 0.002
        self.step_count = 4096
        self.direction = False
        self.step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
    
    def cleanup(self):
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()

    def run(self):
        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )
        
        # initializing
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        
        
        motor_pins = [self.in1, self.in2, self.in3, self.in4]
        motor_step_counter = 0 ;

        try:
            i = 0
            for i in range(self.step_count):
                for pin in range(0, len(motor_pins)):
                    GPIO.output(motor_pins[pin], self.step_sequence[motor_step_counter][pin])
                if self.direction==True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                elif self.direction==False:
                    motor_step_counter = (motor_step_counter + 1) % 8
                else: # defensive programming
                    print( "uh oh... direction should *always* be either True or False" )
                    self.cleanup()
                    exit( 1 )
                time.sleep(self.step_sleep )
        
        except KeyboardInterrupt:
            self.cleanup()
            exit( 1 )
        
        self.cleanup()
        exit( 0 )

motor = Motor()
motor.run()