import pygame
import signal
import random, os
import RPi.GPIO as GPIO

# this code is pretty shitty but it gets the job done #

index = 0

def play_song():
    try:
        if (pygame.mixer.music.get_busy() == False):
            global index
            filename = clips[index]
#             print("filename is" + filename)
            pygame.mixer.music.load(path + filename)
            pygame.mixer.music.play()
            index = index + 1
            if (index >= len(clips)):
                index = 0
    except ValueError:
        print('Exception: ()'. format(ValueError))

def button_callback(channel):
    print("button was just pushed")
    play_song()

path = "line_3/"
clips = os.listdir(path)
clips = [fi for fi in clips if fi.endswith(".mp3") ]
clips.sort()
pygame.init()
pygame.mixer.init()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback, bouncetime=200)

while True:
    signal.pause()

# if __name__ == '__main__':
#     while True:
#         play_songs()
