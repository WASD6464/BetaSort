import os

os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/")
while True:
    if os.path.exists("your_video.txt"):
        os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/database/")
        os.system("python bd_append.py")
        os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/")
        break