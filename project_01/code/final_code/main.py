# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Main Run Code
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
"""

import screen
import touch
import os
import transcribe

if __name__ == '__main__':
    
    
    #flags for checking our touchscreen buttons
    instruct = True
    begin = False
    start_rec = False
    stop_rec = False
    analysis = False
    
    
    try:
        import time
        delay = 2
        touchscreen = touch.Touchscreen()
        print('init display')
        display = screen.SPI_Display()
        print('init image')
        display.image('help.png')
        time.sleep(delay)

    
        while (1):
            
            #button is in quadrant 4, so checks if it is clicked
            if (touchscreen.check_quad_4() and instruct):
                print('touched, begin mode')
                display.image('begin.png')
                instruct = False
                begin = True
            
            #checks for touch on button location
            if (touchscreen.check_bottom_middle() and begin):
                print('touched, record mode on')
                display.image('startRec.png')
                begin = False
                start_rec = True
                
            #checks for touch on button location
            if (touchscreen.check_bottom_middle() and start_rec):
                print('touched, begin the recording')
                display.image('rec.png')
                os.system('sudo python3 record.py')
                start_rec = False
                stop_rec = True
                
            #checks for touch on button location
            if(stop_rec):
                print('touched, analyze')
                display.image('analysis.png')
                output = transcribe.analyze()
                #fit the text to make sure it doesn't truncate
                ret = display.text_fit(output, 25)
                display.text(ret)
                time.sleep(delay)
                while(1):
                    if os.path.isfile('winner.txt'): #the laptop has made a prediction
                        show = []
                        with open('winner.txt') as file:
                            for line in file:
                                show.append(line)
                        display.text('Prediction: ' + show[len(show)-1][19:len(show[len(show)-1])-2], justify=4, align=4)
                        break
                stop_rec = False
                analysis = True
                    
                
    except KeyboardInterrupt:
        print('Program ended by user.')

        