import os

def remove_noise(file_in, start_time, duration_time):

  audio_path = "./audios/audio.wav"
  noise_audio_path = "./audios/noise-audio.wav"
  audio_clean_path = "./audios/audio-clean.wav"
  noise_prof_path = "./audios/noise.prof"

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