from pytube import YouTube

url = "ここに動画のURLを貼り付け"
YouTube(url).streams.get_highest_resolution().download()
