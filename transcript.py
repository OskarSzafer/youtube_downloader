import os
import whisper
from pytube import YouTube
from moviepy.editor import *

model = whisper.load_model("small.en")

def make_transcript(vid_path):
    if os.path.exists(f'{vid_path}.mp4'):
        clip = video = VideoFileClip(f'{vid_path}.mp4')
        video.audio.write_audiofile(f'{vid_path}.mp3')
    else:
        clip = video = VideoFileClip(f'{vid_path}.3gpp')
        video.audio.write_audiofile(f'{vid_path}.mp3')

    result = model.transcribe(f'{vid_path}.mp3')

    with open(f'{vid_path}.txt', 'w') as file:
        text_to_write = result['text'].strip()
        file.write(text_to_write)