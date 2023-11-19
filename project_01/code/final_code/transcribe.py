
"""
--------------------------------------------------------------------------
Speech Transcription Code
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
  - https://realpython.com/python-speech-recognition/
  
Software Setup:
  - sudo pip3 install SpeechRecognition

"""
import speech_recognition as sr
import glob
import os

def analyze():
    try:
        #grab the file that starts with voice
        for filename in glob.glob("voice*"):
            name = filename 
            
        r = sr.Recognizer()
        sample = sr.AudioFile(name)
        
        with sample as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            output = r.recognize_google(audio, show_all = False)
    except:
        output = "Try Again."
    return output
    
