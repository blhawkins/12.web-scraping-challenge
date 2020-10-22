from flask import Flask, render_template, redirect
from flask_pymongo  import PyMongo
import scrape_mars

app = Flask(__name__)

#Use PyMongo to set up a Mongo connection
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

#Route to render index.html template incorporating the data imported into Mongo
@app.route('/')
def index():
    #Find one record of data from the Mongo database
    scraped_data = mongo.db.scraped_data.find_one()
    return render_template('index.html', scraped_data = scraped_data)

#Route that initiates the scraping process
@app.route('/scrape')
def scrape():
    #Run the scrape function
    current_scrape = scrape_mars.scrape()
    mongo.db.scraped_data.update({}, current_scrape, upsert = True)
    return redirect('/', code = 302)

if __name__ == '__main__':
    app.run(debug = True)