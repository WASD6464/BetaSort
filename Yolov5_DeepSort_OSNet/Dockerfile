FROM python:3.9.13

RUN mkdir -p /Users/wasd64/Desktop/Code/VVIT/DeepSort/
WORKDIR /Users/wasd64/Desktop/Code/VVIT/DeepSort/

COPY . /Users/wasd64/Desktop/Code/VVIT/DeepSort/
RUN apt-get update && apt-get install libgl1 -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir


CMD ["python", "start.py"]