import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=fi6e6wGrjsE")
videos = yt.streams

# print('videos', videos)

for i in range(len(videos)):
    print(i, ', ', videos[i])

input_num = int(input("화질은?"))

down_dir = "C:/crawling/youtube"

videos[input_num].download(down_dir)

new_file_name = input("변환 파일 명?")
org_file_name = videos[input_num].default_filename

print(os.path.join(down_dir, org_file_name))
print(os.path.join(down_dir, new_file_name))

# 커맨드 콜
subprocess.call(['ffmpeg', '-i',
                 os.path.join(down_dir, org_file_name),
                 os.path.join(down_dir, new_file_name)
                 ])


print("동영상 다운로드 및 mp3 변환 완료")

# ffmpeg-4.2.2-win64-static
# 코덱 변환