import random
import moviepy.editor as mp
import os

# directory containing video files
# video_dir = 'path/to/video/folder'
video_dir = 'D:/素材/斗罗大陆'

# list of video files
videos = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith('.mp4')]


# list to store video clips
clips = []

# loop through each video and randomly select a 4 second clip
for video in videos:
    clip = mp.VideoFileClip(video).subclip(random.uniform(300, 310), random.uniform(305, 315))
    clips.append(clip)

# concatenate the clips into a new video
final_clip = mp.concatenate_videoclips(clips)
final_clip = final_clip.resize((1280, 720))
final_clip = final_clip.resize((1920, 1080))



# 使用GPU加速视频合成
import moviepy.video.fx.all as vfx
final_clip = vfx.speedx(final_clip, factor=2.0, final_duration=60)
# write the new video to file
final_clip.write_videofile("new_video.mp4", audio=False, codec=h264_hvenc)
final_clip.close()