#Import dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs

#Define the path to the chrome driver
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():  
    
    #Define a dictionary called scraped_data that will be returned by the function
    scraped_data = {}
    
    #Open a browser window
    browser = init_browser()
    
    #---------------Divider---------------#
    
    #----------This section allows for the scraping of NASA's Mars Exploration website
    #Feed the URL and visit the website
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    #Obtain the HTML and parse it into a BeautifulSoup object
    html = browser.html
    soup = bs(html, "html.parser")

    #Use the find function to find the most recent news title and description.
    news_title = soup.find('div', class_ = 'list_text').find('a').get_text()
    news_text = soup.find('div', class_ = 'article_teaser_body').get_text()
    
    #Save the news title and description to the scraped_data dictionary
    scraped_data['news_title'] = news_title
    scraped_data['news_text'] = news_text
    
    #---------------Divider---------------#
    
    #----------This section allows for the scraping of the JPL Featured Space Image website
    #Feed the URL and visit the website
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    #Obtain the HTML and parse it into a BeautifulSoup object
    html = browser.html
    soup = bs(html, "html.parser")

    #Use the find function to find and create the featured image URL
    featured_image_tag = soup.find('a', class_ = 'button fancybox')['data-fancybox-href']
    featured_image_url = f'https://www.jpl.nasa.gov{featured_image_tag}'
    
    #Save the featured_image_url to the scraped_data dictionary
    scraped_data['featured_image_url'] = featured_image_url
    
    #---------------Divider---------------#
    
    #----------This section allows for the scraping of the Mars Facts table
    #Define the target URL
    url = "https://space-facts.com/mars/"

    #Use Pandas to pull tables from the website's HTML code
    tables = pd.read_html(url)

    #Select the correct table
    mars_facts = tables[0]

    #Format the table
    mars_facts.rename(columns = {0: '', 1: 'Mars'}, inplace = True)

    #Export the table to an HTML string
    mars_html_table = mars_facts.to_html(index = False, header = True)

    #Save the mars_html_table string to the scraped_data dictionary
    scraped_data['mars_html_table'] = mars_html_table
    
    #---------------Divider---------------#
    
    #----------This section allows for the scraping of the USGS Astrogeology image site
    #Define a list that will hold the information pulled from each hemisphere's webpage
    hemisphere_info_list = []

    #Define a list of Mars's four hemispheres
    hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']

    #Define the main_url of the Mars web page of the USGS website
    main_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    #Define the base_url used in the formation of the hemisphere_image_urls
    base_url = 'https://astrogeology.usgs.gov'

    #Connect to the main_url
    browser.visit(main_url)

    #Obtain the HTML and parse it into a BeautifulSoup object
    main_html = browser.html
    main_soup = bs(main_html, "html.parser")

    for hemisphere in hemispheres:

        #Access the webpage for each hemisphere and pull the cooresponding HTML code
        browser.links.find_by_partial_text(f'{hemisphere}').click()
        inner_html = browser.html
        inner_soup = bs(inner_html, "html.parser")
    
        #Collect the image tag and title from each hemisphere's web page
        hemisphere_image_tag = inner_soup.find('img', class_ = 'wide-image')['src']
        hemisphere_title = inner_soup.find('h2', class_ = 'title').get_text()
    
        #Form full image URL for each hemisphere
        hemisphere_image_url = f'{base_url}{hemisphere_image_tag}'
    
        #Save the hemisphere_title and hemisphere_image_url
        hemisphere_info = {}
        hemisphere_info['title'] = hemisphere_title
        hemisphere_info['image_url'] = hemisphere_image_url
        hemisphere_info_list.append(hemisphere_info)
    
        #Return to the main page
        browser.visit(main_url)
        
    #Save the hemisphere_info_list to the scraped_data dictionary
    scraped_data['hemisphere_info_list'] = hemisphere_info_list
    
    browser.quit()
    
    return scraped_data