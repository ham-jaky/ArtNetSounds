#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2023 Jakob Felix Rieckers
"""
import stupidArtnet as artNet
import os
import argparse
import json


# own modules
import audioplayer


sounds_activated = []
SOUNDS_PATH = "sounds"


def gen_json():
    os.makedirs(SOUNDS_PATH, exist_ok=True)
    files = os.listdir(SOUNDS_PATH)
    if len(files) == 0:
        print(f"WARNING: folder '{SOUNDS_PATH}' is empty")
    with open("sounds.json", "w") as f:
        json.dump(files, f)

def data_callback(data):
    global sounds_activated
    lenght = len(audioplayer.sounds)
    for_range = range(lenght if lenght < len(data) else len(data))
    sounds_activated = [True if data[i] >= 127 else False for i in for_range]


def main():
    parser = argparse.ArgumentParser(prog="ArtNetSounds", description="Play sounds by increasing DMX-Channels")
    parser.add_argument("-u", "--universe", type=int, dest="universe", help="The ArtNet universe", default=0)
    parser.add_argument("-gj", "--generate-json", action="store_true", help="Read all files from folder", dest="gen_json")
    args = parser.parse_args()

    if args.gen_json or not "sounds.json" in os.listdir():
        gen_json()
    audioplayer.init_module()

    a = artNet.StupidArtnetServer()
    data_listener = a.register_listener(args.universe, callback_function=data_callback)
    while True:
        audioplayer.play_from_arr(sounds_activated)


if __name__ == "__main__":
    main()
