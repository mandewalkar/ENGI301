import speech_recognition as sr
import os
r = sr.Recognizer()

def startConversion(path = os.path.join('./Brendan.wav'),lang = 'en-IN'):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text)
            print(text)
    
        except:
            print('Sorry.. run again...')

startConversion()