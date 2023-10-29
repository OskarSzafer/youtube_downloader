import os

import whisper
from pytube import YouTube
from moviepy.editor import VideoFileClip


model = whisper.load_model("small.en")

def make_transcript(vid_path):
    try:
        video = VideoFileClip(vid_path)
        vid_path_mp3 = vid_path.replace('.mp4', '.mp3')
        vid_path_txt = vid_path.replace('.mp4', '.txt')
        video.audio.write_audiofile(vid_path_mp3)
        video.close()

        result = model.transcribe(vid_path_mp3)

        with open(vid_path_txt, 'w') as file:
            text_to_write = result['text'].strip()
            print(text_to_write)
            file.write(text_to_write)
    except:
        print('transcript failed')