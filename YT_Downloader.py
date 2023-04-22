from pytube import YouTube

# Ex: "And Your Bird Can Sing(The Beatles Guitar Cover)"
url = "https://www.youtube.com/watch?v=LwH7YNwHdas"

my_video = YouTube(url)

# set stream resolution
my_video = my_video.streams.get_highest_resolution()

# download YouTube video
my_video.download("./PyTube/VideoDownloads/")



