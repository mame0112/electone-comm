from flask import Flask, render_template, request
# from google.appengine.ext import ndb
from google.cloud import datastore

from datastore.DatastoreManager import DatastoreManager
from processor.propertydatamgr import PropertyDataManager
# from youtube.ytaccessor import YouTubeAccessor

from crawler.crawler import Crawler

from util.logger import Logger

# app = Flask(__name__)
app = Flask(__name__, static_url_path='',
            static_folder='./app/dist/electone-comm')


# testMethod()
# class User(ndb.Model):
#     name = ndb.StringProperty()
#     mail = ndb.StringProperty()
#     password = ndb.StringProperty()

# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/')
def toppage():
    # dataManager = DatastoreManager()
    # dataManager.createData()
    # return render_template('/src/index.html')
    # return render_template('index.html')
    return app.send_static_file('index.html')


@app.route('/props_tmp', methods=['GET'])
def tmp_process():
    processManager = PropertyDataManager()
    return processManager.save_property_data()


@app.route('/props/<string:properties>', methods=['GET'])
def get_contents_by_property(properties):
    dataManager = DatastoreManager()
    return dataManager.get_content_by_property(properties)


# @app.route('/youtube', methods=['GET'])
# def youtube():

#     dataManager = DatastoreManager()
#     return dataManager.get_latest_data()


@app.route('/contents/<string:song_id>', methods=['GET'])
def get_category_contents(song_id):

    dataManager = DatastoreManager()
    return dataManager.get_song_contents(song_id)


@app.route('/showname')
def showname():
    # name = request.args['name']
    # return render_template('showname.html', name=name)
    return render_template('showname.html')


@app.route('/songs', methods=['GET'])
def get_all_contents():
    # log = Logger("Main")
    # self.log.debug('index')

    dataManager = DatastoreManager()
    dataManager.get_data(12346)

    # dataManager.get_song_data()
    # json = request.get_json()
    # return jsonify(json)

    return render_template('/songs/toppage.html')


@app.route('/songs/<song_id>', methods=['GET'])
def get_one_content(song_id):

    dataManager = DatastoreManager()
    dataManager.create_data(12347)

    return render_template('/songs/song.html')


@app.route('/recommends', methods=['GET'])
def get_recommend_contents():

    dataManager = DatastoreManager()
    return dataManager.get_recommend_contents()


@app.route('/youtube', methods=['GET'])
def search_youtube():

    crawler = Crawler()
    crawler.crawel()

    return render_template('/songs/song.html')

if __name__ == "__main__":
    # main()
    # app.run(host='127.0.0.1:8000')
    app.run()
