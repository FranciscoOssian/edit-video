from moviepy.editor import VideoFileClip, concatenate_videoclips

def remove_silence(file_in, file_out):
    clips = []
    clip = VideoFileClip(file_in)
    times = open("./src/silence.txt", "r")
    last_end = 0
    while 1:
        line = times.readline()
        if(not line):
            break
        
        start, end = line.strip().split()

        try:
            clipTemp = clip.subclip(float(last_end), start)
            print("cuting {} to {}".format(float(last_end)-1, start))
            clips.append(clipTemp)
            last_end = end

        except ValueError:
            print(type(ValueError))
            print(ValueError.args)
            print(ValueError)
            print("erro {} - {}".format(float(last_end), start))
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