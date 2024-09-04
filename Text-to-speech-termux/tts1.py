#import modules
import subprocess
import gtts
#welcome tts msg
welcomemsg="Starting terminal voice assistant program"
a1=gtts.gTTS(welcomemsg)
a1.save("tts2.mp3")
subprocess.call("mpv tts2.mp3",shell=True)
# store a color codes into class ...
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.HEADER+welcomemsg)



#command program
def repeat():
    msg=str(input(bcolors.OKBLUE+"Enter A Command: "))
    
    match msg:
        
        case "clear":
            a=gtts.gTTS("clearing a terminal")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3  && clear",shell=True),
            
        case "ls":
            a=gtts.gTTS("listing a files")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg+" > hari.txt",shell=True)
            with open("hari.txt", "r") as file:
                for line in file:
                    print (bcolors.OKGREEN+line),
           
        case "pwd":
            a=gtts.gTTS("the current location")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg+" > hari.txt",shell=True)
            with open("hari.txt", "r") as file:
                for line in file:
                    print (bcolors.OKGREEN+line),
            
        case "sl":
            a=gtts.gTTS("sl command is running")
            a.save("tts.mp3")
            subprocess.call("mpv tts.mp3",shell=True)
            subprocess.call(msg,shell=True),
        case _:
            if "cd" in msg:
                a=gtts.gTTS("changing directory to "+msg[3:]+" is executing")
                a.save("tts.mp3")
                subprocess.call("mpv tts.mp3",shell=True)
                subprocess.call(msg,shell=True)

            elif msg!="exit":
                a=gtts.gTTS("your command "+msg+" is executing")
                a.save("tts.mp3")
                subprocess.call("mpv tts.mp3",shell=True)
            
    
    if msg!="exit":
        repeat()
   
    else:
        msg1="closing the terminal assistant programe..."
        b=gtts.gTTS(msg1)
        b.save("tts.mp3")
        subprocess.call("mpv tts.mp3",shell=True)
        print(bcolors.FAIL+"Exit tts .....")
repeat()

    










