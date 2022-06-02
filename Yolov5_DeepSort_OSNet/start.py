import os

while True:
    if os.path.exists("static/Upload/your_video.mp4"):
            os.system("rm -f toDO/*")
            os.system("mv static/Upload/your_video.mp4 toDO/")
            os.system(
                "python track.py --source toDO/your_video.mp4 --save-txt --save-vid --yolo_model weights/best.pt --exist-ok")
    if os.path.exists("runs/track/weights/best_osnet_x0_25/your_video.mp4"):
        os.system("mv runs/track/weights/best_osnet_x0_25/your_video.mp4 static/Complete")
    if os.path.exists("runs/track/weights/best_osnet_x0_25/tracks/your_video.txt"):
        os.system("mv runs/track/weights/best_osnet_x0_25/tracks/your_video.txt static/Complete")
