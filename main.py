#!/usr/bin/env python

import sys
import os
from src.remove_silence import remove_silence

os.system("clear")
print("----------------------EDIT VIDEO-----------------------------")
print("1) to donwload youtube video")
print("2) to to remove video silence")
print("----------------------EDIT VIDEO-----------------------------")

opc = int(input(":"))

if opc == 2:
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