#!/usr/bin/env sh

IN=$1
THRESH=$2
DURATION=$3

ffmpeg -hide_banner -vn -i $IN -af "silencedetect=n=${THRESH}dB:d=${DURATION}" -f null - 2>&1 | grep 'silence_end\|silence_start' | awk '{if(NR%2!=0)printf $5}{if(NR%2==0)printf " " $5 "\n"}' > src/silence.txt
