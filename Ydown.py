from bs4 import BeautifulSoup
import requests
import os
from pprint import pprint
from pytube import YouTube
import time

def down(url,qual,loc):
    if "youtube" in url and "http" in url:
        url=url
    else:
        url="http://www.youtube.com%s"%url
    obj=YouTube(url)
    video=obj.filter('mp4')[qual]
    video.download(loc)


def playl(url,qual,loc):
    os.system('cls')
    print("Please be patient. This could take 10 to 20 seconds depending upon your internet connection")
    try:
        r=requests.get(url)
        code=r.text
        k=0
        bs=BeautifulSoup(code,'lxml')
    except:
        print("\nNetwork or Input error :/")
        main()
    os.system('cls')
    for i in bs.find_all('td',{'class':'pl-video-title'}):
        k=k+1

    t=0

    for i in bs.find_all('td',{'class':'pl-video-title'}):
        t=t+1
        os.system('cls')
        print("downloading...\n",end='\n'),
        print(int((t/k)*100),"%",end='\n')
        for b in range(0,50):
            if b<((t/k)*50):
                print("#",end=''),
            else:
                print(" ",end=''),

        print("|",end='')
        for j in i.find_all('a'):
            try:
                arr=j.get('href')
                if 'watch' in arr:
                    down(arr,qual,loc)
            except:
                print("error parsing link!!")

    os.system('cls')
    print("Successfully Downloaded!")

def search():
    srch=input("search query(please use '+' instead of space)\n>>")
    print("Please be patient. This could take 10 to 20 seconds depending upon your internet connection.....")
    try:
        r=requests.get("https://www.youtube.com/results?search_query=%s"%srch)
        code=r.text
        k=0
        bs=BeautifulSoup(code,'lxml')
    except:
        print("\nNetwork or Input error :/")
        main()
    os.popen('cls')
    for i in bs.find_all('h3',{'class':'yt-lockup-title '}):
        k=k+1
        for j in i.find_all('a'):
            try:
                print(k,". "+j.string)
            except:
                k=k
    print("Which Video??\n>>", end='')
    t=input()
    k=0
    for i in bs.find_all('h3',{'class':'yt-lockup-title '}):
        k=k+1
        if k>int(t):
            break
        for j in i.find_all('a'):
            try:
                arr=j.get('href')
            except:
                print("error parsing link")
    
    down(arr)


def main():
    #print("Use default proxy(172.27.16.154)(y/n)\n>>",end='\n')
    #if input() is 'y':
        #os.system('set http_proxy=http://rakeshme:roopak1827@172.27.16.154:3128')
    os.system('cls')
    print("||      Ydown- The Ultimate Youtube Downloader\n||Made By: Pranjul Shukla\n\nYou Know the drill. Do as you are asked to. As simple as that....\n")
    print("1. Search for Video to Download\n2. Download a Video via link\n3. Download a whole f*ckin Playlist\n>>"),
    k=input()
    k=int(k)
    if k is 1:
        os.system('cls')
        search()
    elif k is 2:
        os.system('cls')
        print("Enter Link\n>>", end='')
        url=input()
        k=3
        print("Enter Quality\n1.LOW\n2.AVERAGE\n3.HEIGH\n>>", end='')
        k=input()
        k=int(k)
        if k is 1:
            qual=0
        elif k is 2:
            qual=-2
        else:
            qual=-1
        print("Enter the Location to save video(s)\n1. Tutorials\n2. Video Songs\n3. Give Location Manually\n>>", end='')
        k=input()
        k=int(k)
        if k is 1:
            loc='F:\Turtorials'
        elif k is 2:
            loc='F:\Video Songs'
        else:
            print("Enter Location\n>>", end='')
            loc=input()
        os.system('cls')
        down(url,qual,loc)
        print("Successfully Downloaded!!!")
    else:
        os.system('cls')
        print("Enter Link to the playlist page\n>>", end='')
        url=input()
        k=3
        print("Enter Quality\n1.LOW\n2.AVERAGE\n3.HEIGH\n>>", end='')
        k=input()
        k=int(k)
        if k is 1:
            qual=0
        elif k is 2:
            qual=-2
        else:
            qual=-1
        print("Enter the Location to save video(s)\n1. Tutorials\n2. Video Songs\n3. Give Location Manually\n>>", end='')
        k=input()
        k=int(k)
        if k is 1:
            loc='F:\Turtorials'
        elif k is 2:
            loc='F:\Video Songs'
        else:
            print("Enter Location\n>>", end='')
            loc=input()
        playl(url,qual,loc)

    
main()
