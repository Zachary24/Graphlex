import subprocess
#Connects to Plex Account
from plexapi.server import PlexServer
baseurl = 'http://192.168.0.7:32400'
token = '45np4xhBH3fis6xsmCEK'
plex = PlexServer(baseurl, token)

#Gets Plex Libraries
movies = plex.library.section('Movies')
shows = plex.library.section('TV Shows')



#Sets Media Resolutions
targetRes1080 = ['1080']
targetRes720 = ['720']
targetRes480 = ['480']
targetRes360 = ['360']

#UserWantedResolution
userTargetRes = 'targertRes1080'


#Gets Movie Title For 360 Movies
def getMovies360():
    for movie in movies.all():
        if movie.media[0].videoResolution in targetRes360:
            print(movie.title.encode('utf-8'))

#Gets Movie Title For 480 Movies
def getMovies480():
    for movie in movies.all():
        if movie.media[0].videoResolution in targetRes480:
            print(movie.title.encode('utf-8'))

#Gets Movie Title For 720 Movies
def getMovies720():
    for movie in movies.all():
        if movie.media[0].videoResolution in targetRes720:
            print(movie.title.encode('utf-8'))

#Gets Movie Title For 1080 Movies
def getMovies1080():
    for movie in movies.all():
        if movie.media[0].videoResolution in targetRes1080:
            print(movie.title.encode('utf-8'))



#Get Episode titles for 360 Episodes
def getEpisodes360():
        for show in shows.all():
            for video in show.episodes():
                if video.media[0].videoResolution in targetRes360:
                    print('{} - S{:0=2d}E{:0=2d} - {}'.format(
                        video.grandparentTitle, int(video.parentIndex),
                        int(video.index), video.title.encode('utf-8')))

#Get Episode titles for 480 Episodes
def getEpisodes480():
        for show in shows.all():
            for video in show.episodes():
                if video.media[0].videoResolution in targetRes480:
                    print('{} - S{:0=2d}E{:0=2d} - {}'.format(
                        video.grandparentTitle, int(video.parentIndex),
                        int(video.index), video.title.encode('utf-8')))

#Get Episode titles for 720 Episodes
def getEpisodes720():
        for show in shows.all():
            for video in show.episodes():
                if video.media[0].videoResolution in targetRes720:
                    print('{} - S{:0=2d}E{:0=2d} - {}'.format(
                        video.grandparentTitle, int(video.parentIndex),
                        int(video.index), video.title.encode('utf-8')))

#Get Episode titles for 1080 Episodes
def getEpisodes1080():
        for show in shows.all():
            for video in show.episodes():
                if video.media[0].videoResolution in targetRes1080:
                    print('{} - S{:0=2d}E{:0=2d} - {}'.format(
                        video.grandparentTitle, int(video.parentIndex),
                        int(video.index), video.title.encode('utf-8')))


if __name__ == "__main__":
    getMovies360()
    getMovies480()
    getMovies720()
    getMovies1080()
    getEpisodes360()
    getEpisodes480()
    getEpisodes720()
    getEpisodes1080()
