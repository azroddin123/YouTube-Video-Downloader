from pytube import Playlist
from youtube_video_downloader import download_with_diiferent_resolutions

def playlist_downloader(url) :
    p = Playlist(url)
    print(f"{p.title}")
    # print(len(p.count))
    for video in p.video_urls :
        download_with_diiferent_resolutions(video)
        break

    
# link = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"   
link2 = "https://www.youtube.com/watch?v=iCRh1IGw5wI&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa"
playlist_downloader(link2)