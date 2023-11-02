import os
import time

from pytube import YouTube 
from moviepy.editor import VideoFileClip

from transcript import make_transcript


FORBIDDEN_FILENAME_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\'']


def replace_forbidden_characters(file_name: str) -> str:
    for char in FORBIDDEN_FILENAME_CHARACTERS:
        file_name = file_name.replace(char, '')
    return file_name


def save_cut(
        video_link: str,
        video_path: str,
        video_name: str,
        video_start: int = None,
        video_end: int = None,
        quality: int = 0
    ):
    video_path = video_path.replace('\\', '/')

    start_time = time.time()

    if video_end != None and video_start == None: # prevent moviepy.editor from crushing when only clip end time is set
        video_start = 0


    try:
        yt = YouTube(video_link)
        yt_streams = yt.streams.filter(file_extension="mp4", progressive=True)

        if quality:
            stream = yt_streams.get_highest_resolution()
        else:
            stream = yt_streams.first()
        
        if video_name == '':
            video_name = yt.title
        video_name = replace_forbidden_characters(video_name)
        print("set title: " + video_name)
        if video_start != None or video_end != None:
            full_video_name = f'{video_name}_full.mp4'
            video_name = f'{video_name}.mp4'
        else:
            full_video_name = f'{video_name}.mp4'

        stream.download(video_path, filename=full_video_name)
    except:
        print('Video is unavaialable')
    else:
        end_time = time.time()
        print(f'download time: {end_time-start_time:.2f}s')

        if video_start != None or video_end != None: # cutout clip
            clip = VideoFileClip(f'{video_path}/{full_video_name}').subclip(video_start, video_end)
            clip.write_videofile(f'{video_path}/{video_name}')
            clip.close()
            make_transcript(f'{video_path}/{video_name}')
        else:
            make_transcript(f'{video_path}/{full_video_name}')