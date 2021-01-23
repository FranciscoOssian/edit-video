#!/usr/bin/env python

import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips

file_in = sys.argv[1]
file_out = sys.argv[2]
silence_file = sys.argv[3]

def main():
    print("ddfd")
    clips = []
    clip = VideoFileClip(file_in)
    times = open(silence_file, "r")
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


main()