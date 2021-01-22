#!/usr/bin/env python

import sys
import subprocess
import os
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Input file path
file_in = sys.argv[1]
# Output file path
file_out = sys.argv[2]
# Silence timestamps
silence_file = sys.argv[3]

# Ease in duration between cuts
try:
    ease = float(sys.argv[4])
except IndexError:
    ease = 0.0
minimum_duration = 1.0

def main():
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
            last_start = start
        except ValueError:
            print(end)
            print(ValueError)
            print("erro {} - {}".format(start, end))

    final_clip  = concatenate_videoclips(clips)
    final_clip.write_videofile(
        file_out,
        fps=60,
        preset='ultrafast',
        codec='libx264'
    )
    times.close()
    clip.close()

main()
