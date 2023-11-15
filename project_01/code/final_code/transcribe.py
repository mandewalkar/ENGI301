import speech_recognition as sr
import glob
import os

def analyze():
    try:
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
    
