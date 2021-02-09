#!/usr/bin/env python

import sys
import os
import pytube

from src.commands.remove_noise import remove_noise
from src.commands.merge_videos import merge_videos
from src.commands.remove_silence import remove_silence

from src.screens.template import template

os.system('cls' if os.name == 'nt' else 'clear')

print("----------------------EDIT VIDEO-----------------------------")
print("0) to donwload youtube video")
print("1) to remove video silence")
print("2) to remove video noise")
print("3) to merge videos")
print("4) create template")
print("5) edit by template")
print("6) to exit")
print("----------------------EDIT VIDEO-----------------------------")

opc = int(input(":"))

def opc0():
    print("Give URL:")
    url = input(":")
    print("loading...")
    pytube.YouTube(url).streams.get_highest_resolution().download('./videos/input/')

def opc1():
    print("what's the path of file_in")
    file_in = input(":")

    print("what's the path of file_out")
    file_out = input(":")

    print("what is the limit in decibels to be defined? (note, the part of the videos that has a sound below the defined will be cut)")
    deb = input("decibels (value only):")

    print("what is the limit in seconds for cutting? (note that time bands shorter than this value will not be cut)")
    sec = input("seconds (value only):")

    remove_silence(file_in, file_out, deb, sec)

def opc2():

    print("what's the path of file_in")
    file_in = input(":")

    print("what's the start_time of noise sample (secs)")
    start_time = input(":")

    print("what's the duration_time of noise sample (secs)")
    duration_time = input(":")

    remove_noise(file_in, start_time, duration_time)

def opc3():
    print("first video")
    url1 = input(":")
    print("second video")
    url2 = input(":")
    print("final file name")
    final = input(":")
    merge_videos(url1, url2, final)

def opc5():
    print("insert the template name")
    template_name = input(":")

    template_file = open(f"./storage/templates/{template_name}.txt", "r")

    lines  = template_file.readlines()

    for line in lines:
        list = line.split("(")
        cmd_name = list[0]
        vars = list[1].split(")")[0].split(",")
        print(cmd_name, vars)

        if cmd_name == "remove_silence":
            print(1)
        elif cmd_name == "remove_noise":
            print(2)
        elif cmd_name == "merge_videos":
            print(3)

cmds = [
    opc0,
    opc1,
    opc2,
    opc3,
    template,
    opc5,
    exit
]

cmds[opc]()