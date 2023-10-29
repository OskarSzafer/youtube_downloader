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
        vid_link,
        vid_path,
        vid_name,
        vid_start=None,
        vid_end=None,
        quality=0
    ):
    vid_path = vid_path.replace('\\', '/')

    start_time = time.time()

    if vid_end != None and vid_start == None: # prevent moviepy.editor from crushing when only clip end time is set
        vid_start = 0


    try:
        yt = YouTube(vid_link)
        yt_streams = yt.streams.filter(file_extension="mp4", progressive=True)

        if quality:
            stream = yt_streams.get_highest_resolution()
        else:
            stream = yt_streams.first()
        
        if vid_name == '':
            vid_name = yt.title
        vid_name = replace_forbidden_characters(vid_name)
        print("set title: " + vid_name)
        if vid_start != None or vid_end != None:
            full_vid_name = f'{vid_name}_full.mp4'
            vid_name = f'{vid_name}.mp4'
        else:
            full_vid_name = f'{vid_name}.mp4'

        stream.download(vid_path, filename=full_vid_name)
    except:
        print('Video is unavaialable')
    else:
        end_time = time.time()
        print(f'download time: {end_time-start_time:.2f}s')

        if vid_start != None or vid_end != None: # cutout clip
            clip = VideoFileClip(f'{vid_path}/{full_vid_name}').subclip(vid_start, vid_end)
            clip.write_videofile(f'{vid_path}/{vid_name}')
            clip.close()
            make_transcript(f'{vid_path}/{vid_name}')
        else:
            make_transcript(f'{vid_path}/{full_vid_name}')