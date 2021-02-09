from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def remove_silence(file_in, file_out, deb, sec):

  #create silence.txt
  command = f"""ffmpeg -hide_banner -vn -i {file_in} -af "silencedetect=n={deb}dB:d={sec}" -f null - 2>&1 | grep 'silence_end\|silence_start' | awk '{{if(NR%2!=0)printf $5}}{{if(NR%2==0)printf " " $5 "\\n"}}' > ./src/silence.txt"""
  os.system(command)

  clips = []
  clip = VideoFileClip(file_in)
  times = open("./src/silence.txt", "r")
  last_end = 0
  while 1:
    line = times.readline()
    if(not line):
      break
        
    try:
      start, end = line.strip().split()
      clipTemp = clip.subclip(float(last_end), start)
      print("cuting {} to {}".format(float(last_end)-1, start))
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