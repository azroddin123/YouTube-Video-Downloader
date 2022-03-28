import os
from pytube import YouTube
import csv


# import argparse 

# parser = argparse.ArgumentParser(description="Download and save youtube video with given links")

# parser.add_argument("-url",'--url_link', type="str",help="enter video url", required=True)
# parser.add_argument("-out","--ouput_dir", type="str" , help = "enter ouput path where video store", default="out/",required=True)

url_list = [] 
with open('Liveness_video_link.csv', 'r') as file :
    reader = csv.reader(file)
    for item in reader :
        url_list.append(item[0])


# function to download video with differnet resolution
def download_with_diiferent_resolutions(url):
    my_video = YouTube(url)
    print(my_video.title)
    dir_name =  os.path.join("data_folder",my_video.title)
    os.makedirs(dir_name,exist_ok=True)
    i = 1
    # for stream in my_video.streams.order_by('resolution'):
    for stream in my_video.streams.order_by('resolution').desc().filter(progressive=True,file_extension="mp4"):
        vid_name = str(i)+"-"+str(stream.resolution)
        stream.download(dir_name,filename=vid_name)
        i+=1
        
for link in url_list :
    download_with_diiferent_resolutions(link)
print("done")