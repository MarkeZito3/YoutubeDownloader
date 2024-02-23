import pytube

def __eliminar_caracteres_especiales__(cadena):
    '''Delete caracters not available to save a file
    :param cadena: In this parameter you can put your string
    :returns: It will be removed from the string the next caracters ```'\\', '/', ':', '?', '"', '<', '>'```
    '''
    caracteres_a_eliminar = ['\\', '/', ':', '?', '"', '<', '>', '|']
    for caracter in caracteres_a_eliminar:
        cadena = cadena.replace(caracter, '')
    return cadena

def download_video(url=str, name="Unknown"):
    '''Procedure to download videos to mp4 files uwu
    
    :param url: This is url of a youtube video
    :param name: This is the name of the video that you want, if this is not avalible to use, the name will be `Unknown.mp4`
    '''

    youtube_url = url

    youtubeVideo = pytube.YouTube(youtube_url)
    
    video = youtubeVideo.streams.get_highest_resolution()

    name = pytube.YouTube(youtube_url).title
    name = __eliminar_caracteres_especiales__(name)

    try:
        video.download(filename=f'{name}.mp4')
    except:
        print(name+'\n')
        name="Unknown"
    video.download(filename=f'{name}.mp4')

def download_audio(url):
    '''Procedure to download audio to mp4 file uwu
    
    :param url: (str) url of a youtube video
    '''

    youtube_url = url

    youtubeVideo = pytube.YouTube(youtube_url)

    audio = youtubeVideo.streams.get_audio_only()
    
    name = pytube.YouTube(youtube_url).title

    audio.download(filename=f'{name}.mp4')

if (__name__ == "__main__"):
    download_video(url="https://www.youtube.com/watch?v=QPIywLfRC40&ab_channel=elWacky")

    # download_video("https://www.youtube.com/watch?v=rkm7mUJr_6A&ab_channel=FastyDubs")
