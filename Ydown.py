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
        print(int(((t-1)/k)*100),"%",end='\n')
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
    srch=input("|| Search Query(please use '+' instead of space)\n|| >>")
    print("|| Please be patient. This could take 10 to 20 seconds depending upon your internet connection.....")
    try:
        r=requests.get("https://www.youtube.com/results?search_query=%s"%srch)
        code=r.text
        k=0
        bs=BeautifulSoup(code,'lxml')
    except:
        print("\n|| Network or Input error :/")
        main()
    os.popen('cls')
    for i in bs.find_all('h3',{'class':'yt-lockup-title '}):
        k=k+1
        for j in i.find_all('a'):
            try:
                print("|| ",k,". "+j.string)
            except:
                k=k
    print("|| Which Video??\n|| >>", end='')
    t=input()
    k=0
    print("|| Enter Quality\n|| 1.LOW\n|| 2.AVERAGE\n|| 3.HIGH\n|| >>", end='')
    k=input()
    k=int(k)
    if k is 1:
        qual=0
    elif k is 2:
        qual=-2
    else:
        qual=-1
    print("|| Enter the Location to save video(s)\n|| 1. Tutorials\n|| 2. Video Songs\n|| 3. Give Location Manually\n|| >>", end='')
    k=input()
    k=int(k)
    if k is 1:
        loc='F:\Turtorials'
    elif k is 2:
        loc='F:\Video Songs'
    else:
        print("|| Enter Location\n|| >>", end='')
        loc=input()
    k=0
    for i in bs.find_all('h3',{'class':'yt-lockup-title '}):
        k=k+1
        if k>int(t):
            print("Error")
            break
        for j in i.find_all('a'):
            try:
                arr=j.get('href')
            except:
                print("|| error parsing link")
    print("|| downloading....Please wait")
    down(arr,qual,loc)
    print("|| Successfully Downloaded!!")


def main():
    #print("Use default proxy(172.27.16.154)(y/n)\n>>",end='\n')
    #if input() is 'y':
    os.system('set http_proxy=http://rakeshme:roopak1827@172.27.16.154:3128')
    os.system('cls')
    print("||      Ydown- The Ultimate Youtube Downloader\n||Made By: Pranjul Shukla\n|| \n|| You Know the drill. Do as you are asked to. As simple as that....\n||")
    print("|| 1. Search for Video to Download\n|| 2. Download a Video via link\n|| 3. Download a whole f*ckin Playlist\n|| 4. View Source Code\n|| 5. Exit\n|| >>",end=''),
    k=input()
    k=int(k)
    if k is 1:
        os.system('cls')
        search()
    elif k is 2:
        os.system('cls')
        print("|| Enter Link\n>>", end='')
        url=input()
        k=3
        print("|| Enter Quality\n|| 1.LOW\n|| 2.AVERAGE\n|| 3.HEIGH\n|| >>", end='')
        k=input()
        k=int(k)
        if k is 1:
            qual=0
        elif k is 2:
            qual=-2
        else:
            qual=-1
        print("|| Enter the Location to save video(s)\n|| 1. Tutorials\n|| 2. Video Songs\n|| 3. Give Location Manually\n|| >>", end='')
        k=input()
        k=int(k)
        if k is 1:
            print("\n|| Enter new folder's name\n|| >>", end='')
            l=input()
            loc='F:\Turtorials\%s'%l
            os.system('mkdir %s'%loc)
        elif k is 2:
            loc='F:\Video Songs'
        else:
            print("|| Enter Location\n>>", end='')
            loc=input()
        os.system('cls')
        down(url,qual,loc)
        print("|| Successfully Downloaded!!!")
    elif k is 4:
        os.system('notepad d:\Ydown\Ydown.py')
        main()
    elif k is 5:
        exit()
    else:
        os.system('cls')
        print("|| Enter Link to the playlist page\n|| >>", end='')
        url=input()
        k=3
        print("|| Enter Quality\n|| 1.LOW\n|| 2.AVERAGE\n|| 3.HEIGH\n|| >>", end='')
        k=input()
        k=int(k)
        if k is 1:
            qual=0
        elif k is 2:
            qual=-2
        else:
            qual=-1
        print("|| Enter the Location to save video(s)\n|| 1. Tutorials\n|| 2. Video Songs\n|| 3. Give Location Manually\n|| >>", end='')
        k=input()
        k=int(k)
        if k is 1:
            print("\n|| Enter new folder's name\n|| >>", end='')
            l=input()
            loc='F:\Turtorials\%s'%l
            os.system('mkdir %s'%loc)
        elif k is 2:
            loc='F:\Video Songs'
        else:
            print("|| Enter Location\n|| >>", end='')
            loc=input()
        playl(url,qual,loc)

    
main()
