import pytube
from pprint import pprint
import csv

# To store video link
video_link = [] 


# Download_video_path

res_list = ['/home/azhar/Liveness_Data/1280x720',"/home/azhar/Liveness_Data/176x144",'/home/azhar/Liveness_Data/620x144']

high_path = '/home/azhar/Liveness_Data/1280x720'
low_path = "/home/azhar/Liveness_Data/176x144"
mid_path = '/home/azhar/Liveness_Data/620x144'

# Read csv file and write all video link in list
with open('Liveness_video_link.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        video_link.append(row[0])
        


def download_video(url) :
    yt = pytube.YouTube(url) 
    stream = yt.streams.get_highest_resolution()
    print(yt.streams.get_highest_resolution().resolution)
    stream.download(high_path)
    stream = yt.streams.get_lowest_resolution()
    stream.download(low_path)
    # for stream in yt.streams:
    #     print(stream.resolution)
    # for stream in yt.streams.filter(progressive=True):
    #     print("resolution: " + stream.resolution)
    #     stream.download(res_list[i])
    #     print("----------------------")
    # stream = yt.streams.get_highest_resolution()
    # stream.download(high_path)
    # stream = yt.streams.get_lowest_resolution()
    # stream.download(low_path)
        
download_video('https://www.youtube.com/watch?v=qxbGDCOkMh4')

for url in video_link :
    download_video(url)