#!/usr/bin/env python

import sys
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def remove_silence(file_in, file_out):
    print("ddfd")
    clips = []
    clip = VideoFileClip(file_in)
    times = open("silence.txt", "r")
    last_end = 0
    while 1:
        line = times.readline()
        if(not line):
            break
        
        start, end = line.strip().split()

        try:
            clipTemp = clip.subclip(last_end, start)
            print("cuting {} to {}".format(last_end, start))
            clips.append(clipTemp)
            last_end = end

        except ValueError:
            print(type(ValueError))
            print(ValueError.args)
            print(ValueError)
            print("erro {} - {}".format(last_end, start))
            last_end = end

    final_clip  = concatenate_videoclips(clips)
    final_clip.write_videofile(
        file_out,
        fps=60,
        preset='ultrafast',
        codec='libx264'
    )
    times.close()
    clip.close()

os.system("clear")
print("----------------------EDIT VIDEO-----------------------------")
print("1) to donwload youtube video")
print("2) to to remove video silence")
print("----------------------EDIT VIDEO-----------------------------")

opc = int(input(":"))

if opc == 1:
    print("what's the path of file_in")
    file_in = input(":")
    print("what's the path of file_out")
    file_out = input(":")
    print("qual o limite em deciécibeis para ser definido? (obs, a parte de vídeos que tiver um som abaixo do definido será cortada)")
    deb = input("decibéis (apenas o valor):")
    print("qual o limite em segundos para o corte? (obs, não será cortado faixas de tempo menores que esse valor)")
    seg = input("segundos (apenas o valor):")
    command = "sh detect_silence.sh " + file_in + " " + deb + " " + seg
    os.system(command)
    remove_silence(file_in, file_out)