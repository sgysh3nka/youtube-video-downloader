from pytube import YouTube

def download_youtube_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(path)

url = input("Enter the YouTube video URL: ")
path = input("Enter the download path: ")
download_youtube_video(url, path)
