from pytube import YouTube

link = input('put the link here: ')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()