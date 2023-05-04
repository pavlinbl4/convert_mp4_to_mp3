#To convert mp4 files to mp3 using Python, you can use the moviepy library. Below is the function that does the conversion:
from moviepy.editor import *

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    # Load mp4 file
    video = VideoFileClip(mp4_file_path)
    # Extract audio from mp4 file
    audio = video.audio
    # Save audio as mp3 file
    audio.write_audiofile(mp3_file_path, bitrate='96k', nbytes=2)
    # Close video and audio objects
    audio.close()
    video.close()



if __name__ == '__main__':
    convert_mp4_to_mp3('/Users/evgeniy/Downloads/Агата Кристи - Тайна охотничьей сторожки Аудиокнига -Рассказ- Читает Большешальский.mp4',
                       '/Users/evgeniy/Downloads/Агата Кристи - Тайна охотничьей сторожки Аудиокнига -Рассказ- Читает Большешальский.mp3')
"""
 Here, mp4_file_path is the path to the input mp4 file and mp3_file_path is the path to the output mp3 file. 
 The function loads the mp4 file using VideoFileClip from moviepy library and extracts the audio from it. 
 It then saves the audio as an mp3 file using `write_audiofil
"""