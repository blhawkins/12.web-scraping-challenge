# 12.web-scraping-challenge
University of Kansas Data Analytics Bootcamp Homework Assignment 12

# Main Contents:
    mission_to_mars.ipynb
    scrape_mars.py
    app.py
    index.html
# Tools Used:
    Beautiful Soup
    Splinter
    Pandas
    Flask
    PyMongo
    MongoDB
    HTML
    CSS
    Bootstrap
    Jupyter Notebook

# Description:

#### The initial objective of this project is to use Beautiful Soup, Splinter, and Pandas to scrape a variety of data types from a set of Mars-themed websites. This procedure was carried out in the mission_to_mars.ipynb file, which was then converted into the scrape_mars.py file. As can be seen in the Mission to Mars Jupyter Notebook, the following data was successfully targeted and scraped.
#### The most recent article is taken from the [NASA Mars Exploration Program's website](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest).
![alt text](https://github.com/blhawkins/12.web-scraping-challenge/blob/main/Screenshots/mars_news.png 'Screenshot of NASA Mars Exploration Program Website')
#### The featured image is taken from the [NASA Jet Propulsion Laboratory website](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
![alt text](https://github.com/blhawkins/12.web-scraping-challenge/blob/main/Screenshots/mars_featured_image.png 'Screenshot of NASA Jet Propulsion Laboratory website')
#### A table detailing Mars's planet profile is scraped from the [Space-Facts.com website](https://space-facts.com/mars/).
![alt text](https://github.com/blhawkins/12.web-scraping-challenge/blob/main/Screenshots/mars_table.png "Screenshot of Mars's Planet Profile on Space-Facts.com")
#### Photos of Mars's four hemispheres are taken from the [USGS Astropedia website](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).
![alt text](https://github.com/blhawkins/12.web-scraping-challenge/blob/main/Screenshots/mars_hemispheres.png 'Screenshot of USGS Astropedia website')

#### Following the successful retrieval of this information, it was passed into app.py, a python-based Flask server. Within this Flask application, the information was successfully passed into a local MongoDB database through the use of PyMongo. The information housed in this Mongo database was then queried and combined with the index.html template file to create a Flask-based webpage visualizing the information.

#### Webpage Screenshots:

