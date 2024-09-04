#import modules
import subprocess
import gtts
#welcome tts msg
welcomemsg="Starting terminal voice assistant program"
a1=gtts.gTTS(welcomemsg)
a1.save("tts2.mp3")
subprocess.call("mpv tts2.mp3",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
print(bcolors.OKGREEN+"Select your option")
tools=["1)sl","2)cowsay","3)cmatrix"]
for i in tools:
    print(i)
num=input(bcolors.OKGREEN+"Enter your option:")
match num:
    case 1:
       speak="updating linux and installing sl package"
       print(bcolors.OKGREEN+speak)
       a1=gtts.gTTS(speak)
       a1.save("tts2.mp3")
       subprocess.call("mpv tts2.mp3",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
       subprocess.call("touch runner.sh && chmod +x runner.sh",shell=True)
       f = open("runner.sh", "w")
       f.write("apt update && apt install sl")
       f.close()
       subprocess.run("./runner.sh",shell=True,stdout=open("output.log", "w"), stderr=open("error.log", "w"))
       print(bcolors.OKGREEN+"Installation is complete")

    case 2:
       speak="updating linux and installing cowsay package"
       print(bcolors.OKGREEN+speak)
       a1=gtts.gTTS(speak)
       a1.save("tts2.mp3")
       subprocess.call("mpv tts2.mp3",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
       subprocess.call("touch runner.sh && chmod +x runner.sh",shell=True)
       f = open("runner.sh", "w")
       f.write("apt update && apt install sl")
       f.close()
       subprocess.run("./runner.sh",shell=True,stdout=open("output.log", "w"), stderr=open("error.log", "w"))
       print(bcolors.OKGREEN+"Installation is complete")




""" with open("output.log", "r") as f:
        output = f.read()
        print(bcolors.OKBLUE+output)
        """


