# для начала нам нужно установить moviepy командой : pip3 install moviepy
import moviepy.editor 
from pathlib import Path


video_file = Path('video_name_who_transformation.mp3') # расположение файла для преобразования 




video = moviepy.editor.VideoFileClip(f'{video_file}') 
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')