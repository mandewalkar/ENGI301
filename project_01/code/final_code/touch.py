# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense


import board
import adafruit_tsc2007


class Touchscreen():
    tsc = None
    point = None
    x_coord = None
    y_coord = None
    
    def __init__(self):
        
        # Use for I2C
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

        irq_dio = None  # don't use an irq pin by default
        # uncomment for optional irq input pin so we don't continuously poll the I2C for touches
        # irq_dio = digitalio.DigitalInOut(board.A0)
        self.tsc = adafruit_tsc2007.TSC2007(i2c, irq=irq_dio)
        
    def is_touched(self):
        if (self.tsc != None):
            if self.tsc.touched:
                self.point = self.tsc.touch
                self.x_coord = self.point["x"]
                self.y_coord = self.point["y"]
                if self.point["pressure"] >= 100:  # ignore touches with no 'pressure' as false
                    return True
        return False
        
    
    def check_top_right(self):
        if (self.x_coord < 800 and self.y_coord < 800):
            return True
        else:
            return False
        
    def check_top_left(self):
        if (self.x_coord < 800 and self.y_coord > 3300):
            return True
        else:
            return False

    def check_bottom_right(self):
        if (self.x_coord > 3300 and self.y_coord < 800):
            return True
        else:
            return False 

    def check_bottom_left(self):
        if (self.x_coord > 3300 and self.y_coord > 3300):
            return True
        else:
            return False

    def check_middle(self):
        if (self.x_coord < 2200 and self.x_coord > 1800 and self.y_coord < 2200 and self.y_coord > 1800):
            return True
        else:
            return False
        
    def check_quad_1(self):
        if (self.x_coord < 2000 and self.y_coord < 2000):
            return True
        else:
            return False
        
    def check_quad_2(self):
        if (self.x_coord < 2000 and self.y_coord > 2000):
            return True
        else:
            return False

    def check_quad_3(self):
        if (self.x_coord > 2000 and self.y_coord > 2000):
            return True
        else:
            return False

    def check_quad_4(self):
        if (self.x_coord > 2000 and self.y_coord < 2000):
            return True
        else:
            return False


touchy = Touchscreen()
try:
    while(1):
        if (touchy.is_touched()):
            print(touchy.check_quad_4())
except KeyboardInterrupt:
    print("Program ended by user.")
    