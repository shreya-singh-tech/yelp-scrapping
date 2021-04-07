import pandas as pd
import time as t
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import re
from lxml import html

boston_urls = pd.read_csv("url_yelp.csv")
urls = boston_urls['URL'].tolist()

def res_scraper(url):
	driver = webdriver.Firefox(options=fireFoxOptions)
	driver.get(url)
	
	
	t.sleep(1)
	page = driver.page_source
	soup = BeautifulSoup(page, 'lxml')
	soup2 = BeautifulSoup(page, 'html.parser')
	final_data = []

	# retrieve the total page number
	info_scraped = {}
	final_tag = ''
	final_address = ''

	info_scraped['restaurant_name'] = None
	info_scraped['restaurant_url'] = url
	info_scraped['restaurant_tag'] = None
	info_scraped['restaurant_neighborhood'] = None
	info_scraped['restaurant_address'] = None
	info_scraped['ratings'] = None
	info_scraped['review_number'] = None
	info_scraped['price'] = None

	all = soup.find('div', {'class': "main-content-wrap main-content-wrap--full"})
	special_divs = soup2.find_all('div',{'class':'main-content-wrap'})
	# retrieve tags and append to one string
	try:
		#tags = all.select('.link-size--inherit__373c0__1VFlE').text
		for text in special_divs:
    			tags = text.find_all('a', href = re.compile('/c/'))
		
		for tag in tags:
			final_tag += tag.text + ','
			info_scraped['restaurant_tag'] = final_tag
			
			
	except:
		
		print (None)
		 
		

    # retrieve restaurant name
	try:
		info_scraped['restaurant_name'] = all.find('h1').text
	except:
		print(None)

    # retrieve neighborhood on yelp, which now is CT_ID_10
	try:
		for text in special_divs:
    			neighbor = text.find_all('p', {'class': 'css-8yg8ez'})
		#neighbor = all.select('.text-weight--semibold__373c0__2l0fe').text
		info_scraped['restaurant_neighborhood'] = neighbor[0].text
	except:
		print(None)

    # retrieve address and append road, city, zip code to one string
	try:
		addresses = all.find('address').find('p').find_all('span',{'class': 'raw__373c0__3rcx7'})
		addresses2 = all.find('address').find('p',{'class':'css-znumc2'}).find_all('span',{'class': 'raw__373c0__3rcx7'})
		
		for address in addresses:
            		final_address += address.text + ','
		for address in addresses2:
            		final_address += address.text + ','
		info_scraped['restaurant_address'] = final_address
	except:
		print(None)

    # retrieve the average rating of each restaurant
	try:
		info_scraped['ratings'] = all.find('div', {'aria-label': re.compile(' star rating')})['aria-label']
	except:
		print(None)

    # retrieve total review numbers
	try:
		review_number = all.find('span', {'class': 'css-bq71j2'}).text
		review_number = [int(i) for i in review_number.split() if i.isdigit()][0]
		info_scraped['review_number'] = review_number
	except:
		print(None)

    # retrieve price category listed on YELP
	try:
		#for text in special_divs:
    			#price_data = text.find_all('span', {'class': 'css-1xxismk'})
		
		#if len(price_data > 1):
			#info_scraped['price'] = price_data[1].text
		#else:
			#info_scraped['price'] = price_data[0].text
		
		#price_data = special_divs.find_all('span', {'class' : 'display--inline__373c0__3JqBP margin-r1__373c0__zyKmV border-color--default__373c0__3-ifU'}).find('span', {'class' : 'css-1xxismk'})
		
		price_data = driver.find_element_by_xpath('/html/body/div[2]/div[3]/yelp-react-root/div/div[2]/div[1]/div[1]/div/div/span[2]/span').text
		if price_data[0] == '$':
			info_scraped['price'] = price_data
		else:
			info_scraped['price'] = ''
	except:
		print(None)

	final_data.append(info_scraped)

	df = pd.DataFrame(final_data)
	df.index += 1
	driver.quit()

	return df


iteration_from = 60
iteration_end = 61
#iteration_end = len(urls)
review_data = []

# set driver to headless mode
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

for i in range(iteration_from, iteration_end):
	print(str(datetime.now()) + " "+ str(i) + " restaurant out of " + str(len(urls)))
	item = urls[i] + '?sort_by=date_desc'
	resreview = res_scraper(item)
	review_data.append(resreview)
	review_all = pd.concat(review_data)
    
# encoding is utf-8-sig
review_all.to_csv("Res_info60-61.csv", encoding='utf-8-sig')
#do for res no 20,40 and 60 in the end
