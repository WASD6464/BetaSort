FROM python:3.9.13

RUN mkdir -p /Users/wasd64/Desktop/Code/VVIT/DeepSort/
WORKDIR /Users/wasd64/Desktop/Code/VVIT/DeepSort/


COPY . /Users/wasd64/Desktop/Code/VVIT/DeepSort/
RUN apt-get update
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8080

CMD ["python", "app.py"]