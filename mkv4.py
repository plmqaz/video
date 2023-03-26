import moviepy.editor as mp
import os
import random
import fnmatch
from math import ceil
from time import strftime

directory = "D:/素材/枕上书剧集"
xdim = 1280
ydim = 720
ext = "*mp4"
length = 6
print('working...')
outputs = []
# audio_length = audio_output.duration
audio_length = 300  # 需修改
# compile list of videos
inputs = [os.path.join(directory, f) for f in os.listdir(directory) if
          os.path.isfile(os.path.join(directory, f)) and fnmatch.fnmatch(f, ext)]
# inputs表示directory中的所有以ext为后缀的文件len（inputs）表示directory中以ext为后缀文件的个数
# collage = mp.concatenate_videoclips(outputs)
print(inputs)
while len(outputs) < ceil(audio_length / length):
    i = random.randint(0, len(inputs) - 1)
    # print("i=", i)
    # import to moviepy
    clip = mp.VideoFileClip(inputs[i]).resize((xdim, ydim))
    # clip = mp.VideoFileClip(inputs[i])

    # select a random time point
    start = round(random.uniform(180, clip.duration - 180))
    # print(start)#查看运行用，打印开始点
    # cut a subclip
    out_clip = clip.subclip(start, start + length)

    outputs.append(out_clip)
    # print(len(outputs))#打印列表的数据数目

# combine clips from different videos
collage = mp.concatenate_videoclips(outputs)
collage = collage.subclip(0, audio_length)
time = 'mkv4zss' + strftime("%Y%m%d%H%M%S")
# collage.write_videofile('%s.mp4' % time,audio=path_write_wav_file)


###########添加水印..............
# import moviepy.editor as mp
# 本地视频位置
# video = mp.VideoFileClip("E:/Works/%s.mp4" %time)
# 准备字幕背景sub_bg和logo图片
# sub_bg = (mp.ImageClip("D:/Works/图片/黑字幕条.png")
#           .set_duration(collage.duration)  # 水印持续时间
#           .resize(height=150)  # 水印的高度，会等比缩放
#           .margin(left=0, bottom=20, opacity=1)  # 水印边距和透明度
#           .set_pos(("left", "bottom")))  # 水印的位置
# logo = (mp.ImageClip("D:/Works/图片/mzlogo.png")
#         .set_duration(collage.duration)  # 水印持续时间
#         .resize(height=100)  # 水印的高度，会等比缩放
#         .margin(left=0, top=0, opacity=1)  # 水印边距和透明度
#         .set_pos(("left", "top")))  # 水印的位置

# final = mp.CompositeVideoClip([collage, logo])
# final = mp.CompositeVideoClip([collage, logo,sub_bg])
final = collage
# mp4文件默认用libx264编码， 比特率单位bps
# path_write_wav_file = "D:/Works/audio20200823155638.mp3"  # 需修改
# final.write_videofile('%s.mp4' % time,audio=path_write_wav_file)
final.write_videofile('D:/Works/%s.mp4' % time, audio=False)
