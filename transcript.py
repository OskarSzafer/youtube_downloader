import os

import whisper
from pytube import YouTube
from moviepy.editor import VideoFileClip


model = whisper.load_model("small.en")

def make_transcript(video_path: str):
    try:
        video = VideoFileClip(video_path)
        video_path_mp3 = video_path.replace('.mp4', '.mp3')
        video_path_txt = video_path.replace('.mp4', '.txt')
        video.audio.write_audiofile(video_path_mp3)
        video.close()

        result = model.transcribe(video_path_mp3)

        with open(video_path_txt, 'w') as file:
            text_to_write = result['text'].strip()
            print(text_to_write)
            file.write(text_to_write)
    except:
        print('transcript failed')