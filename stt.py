#!/usr/bin/env python3
import speech_recognition as sr
from gtts import gTTS
import os

tts=gTTS(text='เติมน้ำมันอะไรดีคะ',lang='th')
tts.save('AskforOil.mp3')

file = "AskforOil.mp3"
print("Play mp3")
os.system("mpg123 "+file)

print(sr.__version__)


print(sr.Microphone.list_microphone_names()) #print all the microphones connected to your machine

r = sr.Recognizer()

def fuel_ask():
    with sr.Microphone(device_index=0) as source:
        print("Please say somethings ... ")
        audio = r.listen(source, phrase_time_limit=5)
        text = r.recognize_google(audio, language='th-TH')
        print("You said: ", text)
        
        tts=gTTS(text='เติมน้ำมัน'+ text +'เรียบร้อย',lang='th')
        tts.save('Hello.mp3')

        file = "Hello.mp3"
        print("Play mp3")
        os.system("mpg123 "+file)
        # reduce noise 
        r.adjust_for_ambient_noise(source)

# device = ['HDA Intel PCH: CX8200 Analog (hw:0,0)', 'HDA Intel PCH: HDMI 0 (hw:0,3)', 'HDA Intel PCH: HDMI 1 (hw:0,7)', 'HDA Intel PCH: HDMI 2 (hw:0,8)', 'HDA Intel PCH: HDMI 3 (hw:0,9)', 'HDA Intel PCH: HDMI 4 (hw:0,10)', 'sysdefault', 'front', 'surround40', 'surround51', 'surround71', 'hdmi', 'samplerate', 'speexrate', 'pulse', 'upmix', 'vdownmix', 'dmix', 'default']
# print(device[0])