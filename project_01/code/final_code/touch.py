# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
--------------------------------------------------------------------------
TSC2007 Touchscreen Library with I2C Controller
--------------------------------------------------------------------------
License:   
Copyright 2023 Parnika Mandewalkar

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Software API:

    NOTE: CODE IS CALIBRATED TO DEVICE WITH ORIENTATION 270 deg.

    is_touched()
      - returns True if the display has been touched
    
    check_top_right()
      - returns True if the top right corner has been touched
      
    check_top_left()
      - returns True if the top left corner has been touched
      
    check_bottom_right()
      - returns True if the bottom right corner has been touched
      
    check_bottom_left()
      - returns True if the bottom left corner has been touched
      
    check_middle()
      - returns True if the middle has been touched
      
    check_bottom_middle()
      - returns True if the bottom half of the screen but middle has been touched
      
    check_top_middle()
      - returns True if the top half of the screen but middle has been touched
      
    check_quad_1()
      - returns True if the top right quadrant has been touched
      
    check_quad_2()
      - returns True if the top left quadrant has been touched
      
    check_quad_3()
      - returns True if the bottom left quadrant has been touched
      
    check_quad_4()
      - returns True if the bottom right quadrant has been touched


--------------------------------------------------------------------------
Background Information: 

Links:
  - https://www.adafruit.com/product/5423
  - https://github.com/adafruit/Adafruit_CircuitPython_TSC2007/blob/main/examples/tsc2007_simpletest.py
  - https://learn.adafruit.com/adafruit-tsc2007-i2c-resistive-touch-screen-controller
  - https://github.com/adafruit/Adafruit_CircuitPython_TSC2007
  
Software Setup:
  - sudo pip3 install adafruit-circuitpython-tsc2007
  - sudo pip3 install circup
  - sudo circup install adafruit_tsc2007

"""

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
        if not self.is_touched():
            return False
        if (self.x_coord < 800 and self.y_coord < 800):
            return True
        else:
            return False
        
    def check_top_left(self):
        if not self.is_touched():
            return False
        if (self.x_coord < 800 and self.y_coord > 3300):
            return True
        else:
            return False

    def check_bottom_right(self):
        if not self.is_touched():
            return False
        if (self.x_coord > 3300 and self.y_coord < 800):
            return True
        else:
            return False 

    def check_bottom_left(self):
        if not self.is_touched():
            return False
        if (self.x_coord > 3300 and self.y_coord > 3300):
            return True
        else:
            return False

    def check_middle(self):
        if not self.is_touched():
            return False
        if (self.x_coord < 2200 and self.x_coord > 1800 and self.y_coord < 2200 and self.y_coord > 1800):
            return True
        else:
            return False
        
    def check_bottom_middle(self):
        if not self.is_touched():
            return False
        if (self.x_coord > 2000 and self.y_coord > 1800 and self.y_coord < 2200):
            return True
        else:
            return False
            
    def check_top_middle(self):
        if not self.is_touched():
            return False
        if (self.x_coord < 2000 and self.y_coord > 1800 and self.y_coord < 2200):
            return True
        else:
            return False
        
    def check_quad_1(self):
        if not self.is_touched():
            return False
        if (self.x_coord < 2000 and self.y_coord < 2000):
            return True
        else:
            return False
        
    def check_quad_2(self):
        if not self.is_touched():
            return False
        if (self.x_coord < 2000 and self.y_coord > 2000):
            return True
        else:
            return False

    def check_quad_3(self):
        if not self.is_touched():
            return False
        if (self.x_coord > 2000 and self.y_coord > 2000):
            return True
        else:
            return False

    def check_quad_4(self):
        if not self.is_touched():
            return False
        if (self.x_coord > 2000 and self.y_coord < 2000):
            return True
        else:
            return False
    