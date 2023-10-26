import os
import whisper
from pytube import YouTube
from moviepy.editor import *

model = whisper.load_model("small.en")

def make_transcript(vid_path):
    video = VideoFileClip(vid_path)
    video.audio.write_audiofile(vid_path.replace('.mp4', '.mp3'))

    result = model.transcribe(vid_path.replace('.mp4', '.mp3'))

    with open(vid_path.replace('.mp4', '.txt'), 'w') as file:
        text_to_write = result['text'].strip()
        file.write(text_to_write)