import psycopg2
import os
import pandas as pd
import csv


os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/")
os.system("cp static/Complete/your_video.txt database/")
os.chdir("/Users/wasd64/Desktop/Code/VVIT/DeepSort/database/")
conn = psycopg2.connect(dbname='postgres', user='wasd64',
                        password='', host='localhost')
cursor = conn.cursor()

account = pd.read_csv('your_video.txt', delimiter = ' ')
account.to_csv('your_video.csv', index = None)

with open('your_video.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cursor.execute(
        "INSERT INTO public.detect VALUES (%s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()
os.system("rm your_video.csv")
os.system("rm your_video.txt")