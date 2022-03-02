
#imort pytube using "pip install pytube" 

from pytube import YouTube

#taking input for youtube link

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

ys = yt.streams.get_highest_resolution()

#Now downloading start here......
print("Downloading...")
ys.download()
print("Download completed!!")

#After this the video will be stored in your directory where this program exist
