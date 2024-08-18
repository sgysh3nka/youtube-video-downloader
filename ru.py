from pytube import YouTube

def download_youtube_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(path)

url = input("Введите ссылку на Ютуб видео: ")
path = input("Введите куда скачать видео: ")
download_youtube_video(url, path)
