#!/usr/bin/env python3
import time, os
from pynput import mouse, keyboard

cdir = os.getcwd()

tap_key = "["
flick_key = "]"
base_key = "\\"
love_key = "`"
light_tap_key = "="

mx = 0
my = 0

flick_dist = 500

do_half_flick = 0

def apply_settings():
    global cdir, tap_key, flick_key, base_key, love_key, light_tap_key, flick_dist, do_half_flick
    stext = open(os.path.join(cdir, "config.txt"), "r").read().split("\n")
    for i in stext:
        d = i.split(" = ")
        if d[0] == "tap_key":
            tap_key = d[1]
        if d[0] == "flick_key":
            flick_key = d[1]
        if d[0] == "base_key":
            base_key = d[1]
        if d[0] == "love_key":
            love_key = d[1]
        if d[0] == "light_tap_key":
            light_tap_key = d[1]
        if d[0] == "flick_dist":
            flick_dist = int(d[1])
        if d[0] == "do_half_flick":
            do_half_flick = int(d[1])

apply_settings()

in_flick = False

keys_pressed = [False, False, False]

# 0 is tap, #1 is flick, #2 is love lizards/love lab mode

mousecon = mouse.Controller()


def process_key(key):
    try:
        return key.char
    except AttributeError:
        return key


def on_key_press(key):
    global mx, my, tap_key, flick_key, mousecon, keys_pressed, love_key, flick_dist
    if process_key(key) == love_key:
        keys_pressed[2] = True
        press(mx, my)
    if keys_pressed[2]:
        if process_key(key) == tap_key:
            mousecon.position = (mx, my)
            time.sleep(0.02)
        elif process_key(key) == flick_key:
            if do_half_flick:
                mousecon.position = (mx, my - (flick_dist / 2))
            else:
                mousecon.position = (mx, my - flick_dist)
            time.sleep(0.02)
    if process_key(key) == tap_key or process_key(key) == flick_key:
        press(mx, my)
        if process_key(key) == tap_key:
            keys_pressed[0] = True
        elif process_key(key) == flick_key:
            keys_pressed[1] = True
    elif process_key(key) == base_key:
        mx, my = mousecon.position
        print("Set base position to " + str(mousecon.position))
    elif process_key(key) == light_tap_key:
        light_tap()


def on_key_rl(key):
    global mx, my, tap_key, flick_key, keys_pressed, love_key
    if process_key(key) == love_key:
        keys_pressed[2] = False
        release()
    if process_key(key) == flick_key:
        if not keys_pressed[0] and not keys_pressed[2]:
            flick(mx, my)
        keys_pressed[1] = False
    elif process_key(key) == tap_key:
        if not keys_pressed[1] and not keys_pressed[2]:
            release()
        keys_pressed[0] = False


def press(x, y):
    global mousecon
    mousecon.press(mouse.Button.left)


def release():
    global mousecon
    mousecon.release(mouse.Button.left)


def flick(x, y):
    global in_flick, mx, my, mousecon, flick_dist
    oldx, oldy = mx, my
    in_flick = True
    mousecon.move(0, flick_dist * -1)
    time.sleep(0.02)
    release()
    mousecon.position = (mx, my)
    mx, my = oldx, oldy
    in_flick = False


def light_tap():
    global mousecon
    x, y = mousecon.position
    press(x, y)
    time.sleep(0.03)
    release()


print("AutoFlick has launched. Press " + base_key + " to set the base point.")
with keyboard.Listener(on_press=on_key_press, on_release=on_key_rl) as kl:
    kl.join()
