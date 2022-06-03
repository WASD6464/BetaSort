import os

os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/")
while True:
    if os.path.exists("Upload/your_video.mp4"):
        os.system("docker run --rm --name deep -v /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Upload:/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Upload -v /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/Yolo:/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete deepsort")
