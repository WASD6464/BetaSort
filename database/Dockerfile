FROM python:3.9.13

RUN mkdir -p /Users/wasd64/Desktop/Code/VVIT/DeepSort/
WORKDIR /Users/wasd64/Desktop/Code/VVIT/DeepSort/

COPY . /Users/wasd64/Desktop/Code/VVIT/DeepSort/
RUN apt-get install postgresql postgresql-contrib -y



CMD ["python", "bd.py"]