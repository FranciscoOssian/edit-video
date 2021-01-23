from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(url1, url2, name):
  clip_1 = VideoFileClip(url1)
  clip_2 = VideoFileClip(url2)

  final_clip  = concatenate_videoclips([clip_1, clip_2])
  final_clip.write_videofile(
        "./videos/output/"+name,
        fps=60,
        preset='ultrafast',
        codec='libx264'
  )