import re
import os
import fnmatch
import subprocess

directory_srt = 'd:/Works/'
ext_srt = "*srt"
inputs_srt = [os.path.join(directory_srt, f) for f in os.listdir(directory_srt) if
              os.path.isfile(os.path.join(directory_srt, f)) and fnmatch.fnmatch(f, ext_srt)]
def substitu(srt):
    '''去掉srt中的双引号句号等'''
    new_line = ''
    with open(srt, 'r', encoding='utf8') as f:
        for line in f:
            line = re.sub(r'[：“”]*', '', line)
            line1 = re.sub(r'[明崽]', '明仔', line)
            # print(line)
            new_line += line1

    with open(srt, 'w', encoding='utf8') as f:
        f.write(new_line)

# 将directory文件夹里的文件转换成wav格式
directory = 'd:/Works/'
ext = "*mp3"
inputs = [os.path.join(directory, f) for f in os.listdir(directory) if
          os.path.isfile(os.path.join(directory, f)) and fnmatch.fnmatch(f, ext)]
# inputs表示directory中的所有以ext为后缀的文件len（inputs）表示directory中以ext为后缀文件的个数
# print(inputs)
# subprocess.Popen(ffmpeg -i audio.mp3 -f wav audio.wav)
for audio in inputs:
    audio_name = os.path.splitext(audio)  # audio_name是个元组('E:/xunleiDownload/output', '.mp3')
    # print(audio_name)
    input_audio = audio_name[0] + '.mp3'
    output = audio_name[0] + '.wav'
    # print(output)
    command = ["ffmpeg", "-i", input_audio, "-f", "wav", output]
    subprocess.run(command)
    
    
if __name__ == '__main__':
    for srt_file in inputs_srt:
        substitu(srt_file)
