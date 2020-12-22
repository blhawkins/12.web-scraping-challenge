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

The initial objective of this project is to use Beautiful Soup, Splinter, and Pandas to scrape a variety of data types from a set of Mars-themed websites. This procedure was carried out in the mission_to_mars.ipynb file, which was then converted into the scrape_mars.py file. As can be seen in the Mission to Mars Jupyter Notebook, the following data was successfully targeted and scraped.
1. The most recent article is taken from the [NASA Mars Exploration Program's website](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest).
2. The featured image is taken from the [NASA Jet Propulsion Laboratory website](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
3. A table detailing Mars's planet profile is scraped from the [Space-Facts.com website](https://space-facts.com/mars/).
4. Photos of Mars's four hemispheres are taken from the [USGS Astropedia website](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

Following the successful retrieval of this information, it was passed into app.py, a python-based Flask server. Within this Flask application, the information was successfully passed into a local MongoDB database through the use of PyMongo. The information housed in the Mongo database was then queried and combined with the index.html template file to create a Flask-based webpage visualizing the information. Through the use of multiple routes within the Flask application, the website is able to be manually refreshed in order to pull real-time information.

#### Screen Capture:
![alt text](https://github.com/blhawkins/theRedPlanet/blob/main/Screenshots/screenshot1.png 'Screenshot 1 [Top of Page]')
![alt text](https://github.com/blhawkins/theRedPlanet/blob/main/Screenshots/screenshot2.png 'Screenshot 2')
![alt text](https://github.com/blhawkins/theRedPlanet/blob/main/Screenshots/screenshot3.png 'Screenshot 3')
![alt text](https://github.com/blhawkins/theRedPlanet/blob/main/Screenshots/screenshot4.png 'Screenshot 4 [Bottom of Page]')
