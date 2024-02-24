import pytube
import os

# Private functions
def __delete_special_characters__(string):
    '''Delete caracters not available to save a file
    :param string: In this parameter you can put your string
    :returns: It will be removed from the string the next caracters ```'\\', '/', ':', '?', '"', '<', '>'```
    '''
    chat_to_delete = ['\\', '/', ':', '?', '"', '<', '>', '|']
    for caracter in chat_to_delete:
        string = string.replace(caracter, '')
    return string

# Exportable functions
def download_video(url, path=None, name="Unknown"):
    '''Procedure to download videos to mp4 files uwu
    
    :param url: This is url of a youtube video
    :param path: directory where you want to download the video files, by default the directory will be `\\videos` on this file
    :param name: This is the name of the video that you want, if this is not avalible to use, the name will be `Unknown.mp4`
    '''

    youtubeVideo = pytube.YouTube(url)
    
    video = youtubeVideo.streams.get_highest_resolution()

    name = youtubeVideo.title
    name = __delete_special_characters__(name)
    if path is None:
        path = os.getcwd()+'\\videos'
    else:
        path = path+'\\videos'
    try:
        video.download(filename=f'{name}.mp4',output_path=path)
    except:
        name="Unknown"
    video.download(filename=f'{name}.mp4',output_path=path)

def download_audio(url, path=None, name="Unknown"):
    '''Procedure to download audio to mp4 file uwu
    
    :param url: (str) url of a youtube video
    :param path: directory where you want to download the audio files, by default the directory will be `\\audios` on this file
    :param name: This is the name of the video that you want as audio, if this is not avalible to use, the name will be `Unknown.mp4`
    '''

    youtubeVideo = pytube.YouTube(url)

    audio = youtubeVideo.streams.get_audio_only()
    
    name = youtubeVideo.title

    if path is None:
        path = os.getcwd()+'\\audios'
    else:
        path = path+'\\audios'

    try:
        audio.download(filename=f'{name}.mp4',output_path=path)
    except:
        name="Unknown"
    audio.download(filename=f'{name}.mp4',output_path=path)

if (__name__ == "__main__"):
    path = os.getcwd()+'\\videos'
    print(path)