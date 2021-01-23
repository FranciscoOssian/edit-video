#!/usr/bin/env python

import sys
import os
import pytube
from src.remove_silence import remove_silence
from src.merge_videos import merge_videos

os.system("clear")
print("----------------------EDIT VIDEO-----------------------------")
print("1) to donwload youtube video")
print("2) to remove video silence")
print("3) to merge videos")
print("4) to exit")
print("----------------------EDIT VIDEO-----------------------------")

opc = int(input(":"))

def opc2():
    print("what's the path of file_in")
    file_in = input(":")

    print("what's the path of file_out")
    file_out = input(":")

    print("what is the limit in decibels to be defined? (note, the part of the videos that has a sound below the defined will be cut)")
    deb = input("decibels (value only):")

    print("what is the limit in seconds for cutting? (note that time bands shorter than this value will not be cut)")
    sec = input("seconds (value only):")
    
    command = "cd src | sh detect_silence.sh " + file_in + " " + deb + " " + sec + " | cd .."
    os.system(command)
    remove_silence(file_in, file_out)

if opc == 1:
    print("Give URL:")
    url = input(":")
    print("loading...")
    pytube.YouTube(url).streams.get_highest_resolution().download('./videos/input/')

elif opc == 2:
    opc2()
elif opc == 3:
    print("first video")
    url1 = input(":")
    print("second video")
    url2 = input(":")
    print("final file name")
    final = input(":")
    merge_videos(url1, url2, final)
elif opc == 4:
    exit()