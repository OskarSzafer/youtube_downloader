from pytube import YouTube 
from moviepy.editor import VideoFileClip
from os.path import exists
import time
from transcript import make_transcript

def save_cut(
        vid_link,
        vid_path,
        vid_name='Clip',
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

        if quality:
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.first()

        stream.download(vid_path)
    except:
        print('Video is unavaialable')
    else:
        end_time = time.time()
        print(f'download time: {end_time-start_time:.2f}s')
        
        orginal_file_name = yt.title.replace('.', '').replace(':', '').replace('\'', '')

        if vid_start != None or vid_end != None:
            if exists(f'{vid_path}/{orginal_file_name}.mp4'):
                clip = VideoFileClip(f'{vid_path}/{orginal_file_name}.mp4').subclip(vid_start, vid_end)
            else:
                clip = VideoFileClip(f'{vid_path}/{orginal_file_name}.3gpp').subclip(vid_start, vid_end)
            clip.write_videofile(f'{vid_path}/{vid_name}.mp4')
            make_transcript(f'{vid_path}/{vid_name}')
        else:
            make_transcript(f'{vid_path}/{orginal_file_name}')