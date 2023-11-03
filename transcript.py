import os

import torch
from transformers import pipeline
from pytube import YouTube
from moviepy.editor import VideoFileClip


pipe = pipeline(
    "automatic-speech-recognition",
    model="distil-whisper/distil-large-v2",
    device="cpu",
    torch_dtype=torch.float32,
    max_new_tokens=128,
)

def make_transcript(video_path: str):
    try:
        video = VideoFileClip(video_path)
        video_path_mp3 = video_path.replace('.mp4', '.mp3')
        video_path_txt = video_path.replace('.mp4', '.txt')
        video.audio.write_audiofile(video_path_mp3)
        video.close()

        result = pipe(video_path_mp3)

        with open(video_path_txt, 'w') as file:
            text_to_write = result['text'].strip()
            print(text_to_write)
            file.write(text_to_write)
    except:
        print('transcript failed')
