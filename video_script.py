from os import mkdir
from pytube import YouTube

def download_with_diiferent_resolutions(url):
    my_video = YouTube(url)
    print(my_video.title)
    # video_resolutions = []
    # for stream in my_video.streams.order_by('resolution'):
    i = 20
    for stream in my_video.streams.order_by('resolution').desc():
        # # print(stream)
        # video_resolutions.append(stream.resolution)
        # videos.append(stream)
        name = str(i)+"-"+str(stream.resolution)
        print(name)
        stream.download(filename=name)
        i = i + 1 
       

url = 'https://www.youtube.com/watch?v=PFpI00f6v8I'
download_with_diiferent_resolutions(url)




# OLD CODE
from pytube import YouTube

# def download_with_diiferent_resolutions(url):
   
#     my_video = YouTube(url)
#     print(my_video.title)
    
    # video_resolutions = []
    # for stream in my_video.streams.order_by('resolution'):
    # for stream in my_video.streams.order_by('resolution').desc():
    #     # # print(stream)
    #     # video_resolutions.append(stream.resolution)
        # videos.append(stream)
#         stream.download(filename=input("enter file name"))
        

#     print(video_resolutions)

#     return video_resolutions, videos

# url = 'https://www.youtube.com/watch?v=qxbGDCOkMh4'

# sort_resolutions(url)