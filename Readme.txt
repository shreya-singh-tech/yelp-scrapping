Notes:
1 A. yelp_bs_Final is the script to get the links of resturants by location, keep adding last arugyment by 10, starting at 0 to get the results.Eg:
python3 yelp_bs_Final.py 0

1. There are three python scripts, the 'Restaurant_info' is to scrape information
in the restaurant level.

2. The other two scripts are scraping the data about comment in each restaurant,
like the comments, review date or the reviewer name. And the 'Reviewer_profile' 
scrapes the history information of the reviewers, like his previous rating distribution.

3. For running the code, the path of geckodrive.exe should change to your own.

4. Since the source code of the Yelp website is changing all the time, also the layout
of the site will be different from time to time, the code will not work correctly, so
if the code always print 'None' from the terminal, or the data you get is wrong, you 
may need to check the source code of the website, and update them in python code.
(the infomation in soup.find() or soup.select()) 
