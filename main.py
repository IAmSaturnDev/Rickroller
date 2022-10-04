from pygame import mixer
import time

mixer.init()
mixer.music.load("rickroll.wav")

while True:
    mixer.music.play()
    time.sleep(7)
