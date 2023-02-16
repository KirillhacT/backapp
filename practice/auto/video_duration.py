import os
import subprocess

#os.getcwd - текущий путь
"""
os.walk - возвращает генератор, каждая итерация которого
содержит кортеж c текущей папкой и два массивы, содержащие названия
других папок и название файлов, содержащихся в текущей директории
"""

# walk = os.walk(os.getcwd())
    # for i in walk:
    #     print(i)


video_extensions = ["mp4", "avi", "py"]

def get_videos():
    videos = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split(".")[-1] in video_extensions:
                path_file = os.path.join(root, file)
                videos.append(path_file)
    return videos

def get_ffprobe_output(filename: str):
    filename = filename.replace(" ", "\ ")
    p = subprocess.Popen()



def main():
    print(get_videos())


if __name__ == '__main__':
    main()