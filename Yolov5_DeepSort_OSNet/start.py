import os

while True:
    if os.path.exists("download/your_video.mp4"):
        os.system("mv download/your_video.mp4 toDO/")
        os.system(
            "python track.py --source toDO/your_video.mp4 --project / --save-txt --save-vid --yolo_model weights/best.pt --exist-ok")
    if os.path.exists("weights/best_osnet_x0_25/your_video.mp4"):
        os.system("mv weights/best_osnet_x0_25/your_video.mp4 static/")
    if os.path.exists("weights/best_osnet_x0_25/tracks/your_video"):
        os.system("mv weights/best_osnet_x0_25/tracks/your_video static/")
