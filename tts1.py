#import modules
import subprocess
import gtts
#welcome tts msg
welcomemsg="welcome to text to speech termux"
a1=gtts.gTTS(welcomemsg)
a1.save("tts.mp3")
subprocess.call("mpv tts.mp3",shell=True)
print("welcome to text to speech termux...")

def repeat():
    msg=input("Enter A Message: ")
    a=gtts.gTTS(msg)
    a.save("tts.mp3")
    subprocess.call("mpv tts.mp3",shell=True)
    if msg!="exit":
        repeat()
    else:
        print("Exit tts .....")
        msg1="closing the text to speech programe..."
        b=gtts.gTTS(msg1)
        b.save("tts.mp3")
        subprocess.call("mpv tts.mp3",shell=True)
repeat()

    










