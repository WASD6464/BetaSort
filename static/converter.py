import os


os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/")
while True:
    while os.path.exists("Complete/Yolo/your_video.mp4"):
        if os.path.exists("Complete/Yolo/your_video.mp4"):
            os.system("rm -f Complete/your_video.mp4")
            os.system("ffmpeg -i /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/Yolo/your_video.mp4 -vcodec h264 /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/your_video.mp4")
            os.system("rm Complete/Yolo/your_video.mp4")
            os.system("mv Complete/Yolo/your_video.txt Complete/")