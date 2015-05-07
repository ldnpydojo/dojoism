__author__ = 'al'
import turtle
import random
import math
import subprocess

BEAT = 1


moves = [
    turtle.Turtle.forward,
    turtle.Turtle.back,
    turtle.Turtle.right,
    turtle.Turtle.left,
]

def get_steps():
    while True:
        yield random.choice(moves)


def play_sound(n):
    subprocess.call(("sox  -n -t wav /dev/stdout synth .8 pluck '%%'$(( %d  "
                     ")) "
                    "fade h 0.0 .3 .4 rate 48k  | paplay") % n, shell=True)


def main():
    turtle.Screen()
    turtle.colormode(255)

    percival = turtle.Turtle()
    percival.shape("turtle")
    percival.speed(BEAT)

    t = 0
    for step in get_steps():

        t += random.random()
        t -= random.random()

        color = (int(128 + 127*math.cos(t)),
                 int(128 + 127*math.sin(t)),
                 int(128 + 127*math.cos(t*0.3)))
        percival.pencolor(color)
        play_sound(random.randint(2, 20))
        step(percival, random.randint(10, 30))

if __name__ == "__main__":
    main()
