import os

while True:
    os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/")
    if os.path.exists("Upload/your_video.mp4"):
        os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/Yolov5_DeepSort_OSNet/")
        os.system("docker run --rm --name deep -v /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Upload:/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Upload -v /Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete/Yolo:/Users/wasd64/Desktop/Code/VVIT/DeepSort/static/Complete deepsort")