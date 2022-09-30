from moviepy.editor import *

#below subclip is used to give time in video you like to cut: 00:00 to 00:05
video = VideoFileClip("file.mp4").subclip(00,5)
video.write_gif("test1.gif")
print("*****Video converted to Gif*****")
