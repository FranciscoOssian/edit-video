import os

def template():

  
  os.system('cls' if os.name == 'nt' else 'clear')

  print("Insert the Template name:")
  template_name = input(":")

  template_file = open(f"./storage/templates/{template_name}.txt", "w")

  commands = []

  i = 1
  while 1:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(commands)

    print("---Write your template edit video---")
    
    print("Add a comand to your template.")
    print("1) to remove video silence")
    print("2) to remove video noise")
    print("3) to merge videos")
    print("4) to exit")

    opc = int(input(":"))

    if opc == 1:
      print("Insert X for values ​​you only want to enter when using")

      print("what's the path of file_in")
      file_in = input(":")

      print("what's the path of file_out")
      file_out = input(":")

      print("what is the limit in decibels to be defined? (note, the part of the videos that has a sound below the defined will be cut)")
      deb = input("decibels (value only):")

      print("what is the limit in seconds for cutting? (note that time bands shorter than this value will not be cut)")
      sec = input("seconds (value only):")

      command = f"remove_silence({file_in},{file_out},{deb},{sec})"

      commands.append(command)

      template_file.write(command+"\n")
    
    elif opc == 2:
      print("what's the path of file_in")
      file_in = input(":")

      print("what's the start_time of noise sample (secs)")
      start_time = input(":")

      print("what's the duration_time of noise sample (secs)")
      duration_time = input(":")

      command = f"remove_noise({file_in},{start_time},{duration_time})"

      commands.append(command)

      template_file.write(command+"\n")

    elif opc == 3:
      print("first video")
      url1 = input(":")
      print("second video")
      url2 = input(":")
      print("final file name")
      final = input(":")
      command = f"merge_videos({url1},{url2},{final})"
      commands.append(command)

      template_file.write(command+"\n")
    
    elif opc == 4:
      i = 0
      template_file.close()
    else:
      print("")