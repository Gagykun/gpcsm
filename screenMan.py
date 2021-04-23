# Supports all file types but all other supported file types will be converted to mp4. MP4 is the only supported end product

import os, time
from colorama import Fore, Back, Style

os.chdir("/home/pi/screenManager/") # Set current directory
if os.path.isfile("active.gif"): #gif we use moviepy to gif > mp4
    if os.path.isfile("active.mp4"):
        print(Fore.YELLOW+"Cannot start the conversion process with an old .mp4. Deleting and converting...")
        print(Style.RESET_ALL)
        os.system("rm active.mp4")
    import moviepy.editor as mp
    clip = mp.VideoFileClip("active.gif")
    clip.write_videofile("active.mp4")
    clip.close()
    os.system("rm active.gif")
    os.system("mplayer active.mp4 -loop 0 -fs")

if os.path.isfile("active.mp4"): #mp4
    os.system("mplayer active.mp4 -loop 0 -fs")

else:
    os.system("mplayer warn.mp4 -loop 0 -fs")
    print(Fore.RED+"ERROR:Unsupported file type!")
