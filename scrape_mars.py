# Dependencies
from urllib.request import urlopen
from bs4 import BeautifulSoup as bsoup
from splinter import Browser
import pandas as pd

# define a scraping function -> scrape
# IN: nothing, just needs to be called
# OUT: a dictionary of scraped data
def scrape():
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #browser = Browser('chrome', **executable_path, headless=False)
    #browser.visit(url)
    
    
    #################################################################
    # NASA Mars News
    #################################################################

    #import client
    mars_url = 'https://mars.nasa.gov/news/'
    uclient = urlopen(mars_url)
    # HTML object
    mars_html = uclient.read()
    # at end include mars_html.close()
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #browser = Browser('chrome', **executable_path, headless=False)
    #browser.visit(url)

    # Parse HTML with BeautifulSoup
    mars_soup = bsoup(mars_html, 'html.parser')
    # Retrieve all elements that contain title information
    #article = mars_soup.find('div', class_='list_text').find('div', class_='content_title')
    #article_title = article.text

    # Parse HTML with BeautifulSoup to find article teasers
    articles = mars_soup.find("div",{'class':'article_teaser_body'})
    #article_teaser = 


    #################################################################
    # JPL Mars Space Images - Featured Image
    #################################################################

    # new basic tools
    mars_url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    uclient2 = urlopen(mars_url2)
    mars_html2 = uclient2.read()
    mars_soup2 = bsoup(mars_html2, 'html.parser')

    # scrape site for website's featured image
    # return a url for the image
    mars_image = mars_soup2.find('div', class_='carousel_items')
    mars_image = mars_image.article.a['data-fancybox-href']
    featured_image_url = f"{mars_url2}{mars_image}"


    #################################################################
    # Mars Facts
    #################################################################

    # define and print a dataframe from the url
    df = pd.read_html(mars_url3)
    # important to note that read_html(arg) gives a LIST of dataframes, not a single dataframe itself
    # now the data frames must be converted back into a simpler html table string
    df_1 = df[0].to_html()
    df_2 = df[1].to_html()
    df_3 = df[2].to_html()


    #################################################################
    # Mars Hemispheres
    #################################################################

    # initialize dictionary for hemisphere data
    hemisphere_image_urls = {"title":[],"img_url":[]}

    # Make a list of the 4 urls (one for each hemisphere)
    # [Cerberus, Schiparelli, Syrtis Major, Vallis Marineris]
    urls = [
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    ]

    # Cycle through the urls and append scraped information to the dictionary 'hemisphere_image_urls'
    for url in urls:
        mars_url4 = url
        uclient4 = urlopen(mars_url4)
        mars_html4 = uclient4.read()
        mars_soup4 = bsoup(mars_html4, 'html.parser')
        info = mars_soup4.find("img",{'class':'wide-image'}).get('src')
        img_url_info = 'https://astrogeology.usgs.gov' + info
        hemisphere_image_urls["img_url"].append(img_url_info)
        title = mars_soup4.find("h2", {"class":"title"}).text
        hemisphere_image_urls["title"].append(title)

    #################################################################
    # Returning the information
    #################################################################

    # Build a dictionary for the data so it can all be sent out in one
    # single unit
    scraped_data = {
    'News' : {
        'Title' : article_title,
        'Teaser' : article_teaser
    },
    
    'FeatureImage' : featured_image_url,
    'Hemispheres' : hemisphere_image_urls,
    'FactTable' : df_1
    }

    return scraped_data