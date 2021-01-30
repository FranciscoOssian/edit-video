#!/usr/bin/env python

import sys
import os
import pytube

from src.remove_silence import remove_silence
from src.merge_videos import merge_videos

from src.screens.template import template

os.system("clear")
print("----------------------EDIT VIDEO-----------------------------")
print("1) to donwload youtube video")
print("2) to remove video silence")
print("3) to remove video noise")
print("4) to merge videos")
print("5) create template")
print("6) edit by template")
print("7) to exit")
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
    
    command = f"""ffmpeg -hide_banner -vn -i {file_in} -af "silencedetect=n={deb}dB:d={sec}" -f null - 2>&1 | grep 'silence_end\|silence_start' | awk '{{if(NR%2!=0)printf $5}}{{if(NR%2==0)printf " " $5 "\\n"}}' > ./src/silence.txt"""
    
    os.system(command)

    remove_silence(file_in, file_out)

def opc3():

    print("what's the path of file_in")
    file_in = input(":")

    audio_path = "./audios/audio.wav"
    noise_audio_path = "./audios/noise-audio.wav"
    audio_clean_path = "./audios/audio-clean.wav"
    noise_prof_path = "./audios/noise.prof"

    print("what's the start_time of noise sample (secs)")
    start_time = input(":")

    print("what's the duration_time of noise sample (secs)")
    duration_time = input(":")

    commands = [
        f"ffmpeg -i {file_in} {audio_path}",
        f"sox {audio_path} {noise_audio_path} trim {start_time} {duration_time}",
        f"sox {noise_audio_path} -n noiseprof {noise_prof_path}",
        f"sox {audio_path} {audio_clean_path} noisered {noise_prof_path} 0.21",
        f"ffmpeg -i {file_in} -i {audio_clean_path} -c:v copy -map 0:v:0 -map 1:a:0 ./videos/video-clean-audio.mp4"
    ]

    
    os.system(commands[0])
    os.system(commands[1])
    os.system(commands[2])
    os.system(commands[3])
    os.system(commands[4])

if opc == 1:
    print("Give URL:")
    url = input(":")
    print("loading...")
    pytube.YouTube(url).streams.get_highest_resolution().download('./videos/input/')
elif opc == 2:
    opc2()
elif opc == 3:
    opc3()
elif opc == 4:
    print("first video")
    url1 = input(":")
    print("second video")
    url2 = input(":")
    print("final file name")
    final = input(":")
    merge_videos(url1, url2, final)
elif opc == 5:
    template()
elif opc == 6:

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

elif opc == 7:
    exit()