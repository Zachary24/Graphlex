#Adds Packages/Flask & Packages/Flask to package path (sys.path)
import subprocess
#Imports getMeta Function
from metaGrabber import getMovies360, getMovies480, getMovies720, getMovies1080, getEpisodes360, getEpisodes480, getEpisodes720, getEpisodes1080

#Imports Flask
from flask import Flask, render_template, request, flash

app = Flask(__name__)

#Adds Index/Home Page
@app.route('/', methods=['GET', 'POST'])
def Index():
    return render_template('index.html')

#Adds About Page
@app.route('/About', methods=['GET', 'POST'])
def About():
    return render_template('about.html')

#Adds Graphs Page
@app.route('/Graphs', methods=['GET', 'POST'])
def graphs():
    return render_template('graphs.html')

#Add Video Resolution Graphs Page
@app.route('/VideoResGraphs')
def VideoResGraphs():
    return render_template('videoresgraphs.html')

#Get all movies in 360p
@app.route('/getMovies360')
def fungetMovies360():
    getMovies360()
    return 'Ok'

#Get all movies in 480p
@app.route('/getMovies480')
def fungetMovies480():
    getMovies480()
    return 'Ok'

#Get all movies in 720p
@app.route('/getMovies720')
def fungetMovies720():
    getMovies720()
    return 'Ok'


#Get all movies in 1080p
@app.route('/getMovies1080')
def fungetMovies1080():
    getMovies1080()
    return 'Ok'







#Adds Settings Page
@app.route('/Settings', methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')












if __name__ == '__main__':
    app.run()
