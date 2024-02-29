import pytube
from pathlib import Path

class YouTubeDownloader:
    def __init__(self, path=None):
        self.path = path or Path.cwd()

    def __delete_special_characters__(self, string):
        '''Delete caracters not available to save a file'''
        char_to_delete = ['\\', '/', ':', '?', '"', '<', '>', '|']
        for character in char_to_delete:
            string = string.replace(character, '')
        return string

    def download_video(self, url, name="Unknown"):
        '''Procedure to download videos to mp4 files'''
        youtube_video = pytube.YouTube(url)
        video = youtube_video.streams.get_highest_resolution()
        name = self.__delete_special_characters__(youtube_video.title)
        try:
            video.download(filename=f'{name}.mp4', output_path=self.path / 'videos')
        except:
            name = "Unknown"
            video.download(filename=f'{name}.mp4', output_path=self.path / 'videos')

    def download_audio(self, url, name="Unknown"):
        '''Procedure to download audio to mp4 file'''
        youtube_video = pytube.YouTube(url)
        audio = youtube_video.streams.get_audio_only()
        name = self.__delete_special_characters__(youtube_video.title)
        try:
            audio.download(filename=f'{name}.mp4', output_path=self.path / 'audios')
        except:
            name = "Unknown"
            audio.download(filename=f'{name}.mp4', output_path=self.path / 'audios')

    def file_exist(self, filename):
        path = self.path / filename
        if not path.exists():
            return filename

        base_name = path.stem
        extension = path.suffix

        index = 1
        while True:
            new_filename = f"{base_name}({index}){extension}"
            if not (self.path / new_filename).exists():
                return new_filename
            index += 1

    def title(self, url):
        youtube_video = pytube.YouTube(url)
        return youtube_video.title

    def file_name(self, url):
        youtube_video = pytube.YouTube(url)
        name = self.__delete_special_characters__(youtube_video.title)
        return f"{name}.mp4"

if __name__ == "__main__":
    downloader = YouTubeDownloader()
    # Aquí puedes llamar a los métodos de la clase según sea necesario
