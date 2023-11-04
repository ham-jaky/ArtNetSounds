#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2023 Jakob Felix Rieckers
"""
import os
import json

VLC_COMMAND = "vlc --play-and-exit -I dummy"

def init_module():
    with open("sounds.json") as f:
        sounds = json.load(f)
    print("Sounds", sounds)

def playsound(index):
    os.system(VLC_COMMAND + " sounds/" + sounds[index])


def play_from_arr(arr):
    for i in range(len(arr)):
        if arr[i]:
            playsound(i)
