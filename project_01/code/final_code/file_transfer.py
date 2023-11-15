import pysftp
import glob
import os
HOSTNAME = "192.168.7.2"
USERNAME = "debian"
PASSWORD = "temppwd"
PORT = 22
recieved = False

try:
    conn = pysftp.Connection(host=HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD)
    print("Connection Success")
except:
    print("Connection Failed")

conn.chdir('/var/lib/cloud9/ENGI301/project_01/code/final_code')
while(1):
    recieved = False
    files = conn.listdir()
    filename = None
    for file in files:
        if ('voice' in file):
            conn.get(file)
            filename = file
            recieved = True
    if(recieved):
        os.chdir(r"C:\Users\parni\Desktop\College\ENGI301\ENGI301\project_01\code\Voice samples\pyAudioAnalysis\pyAudioAnalysis>")
        os.system('python audioAnalysis.py classifyFile -i data/wrec.wav --model svm --classifier data/svmVoice'.format(''))


conn.close()

