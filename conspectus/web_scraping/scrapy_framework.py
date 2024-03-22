import scrapy
from scrapy.crawler import CrawlerProcess

"""
For quick data collection from one page, BeautifulSoup is 100% suitable. 
But if you need to collect data on several pages, go through pages with pagination, 
then such a task makes the script much more difficult. After all, on each page you will also need to find the necessary link, 
and then make a request for this link. In addition, authentication and/or authorization management is the responsibility of the developer.

The last drawback of the relationship between BeautifulSoup and requests is the complexity of setting up "thrifty" scraping. 
When you need to collect a lot of data from thousands or tens of thousands of pages, your script will create too much 
and unwanted load on the server. As a result, and most likely, all requests to this server from your address will be blocked. 
To avoid this, you need to make requests at some interval, as if imitating the behavior of a real user. 
Implementing this mechanism can be a difficult task.

The asynchronous data collection framework Scrapy provides a solution to these shortcomings.

Key features of Scrapy:

asynchrony (significant increase in productivity);
automatic work with request headers and cookies;
"thrifty" scraping;
imitation of the browser of the specified version in the request headers;
tools for building complex multi-level processing schemes of the collected data (cleaning, validation, formatting, saving to the database, etc.);
own testing tool.


Scrapy provides a powerful framework for extracting, processing and storing data."""

# Installation:
"""Scrapy uses Spiders - a set of standalone scanners with a specific set of instructions. 
The framework makes it easy to develop even large scrapping projects so that other developers can use the code.

pip install Scrapy / poetry add Scrapy

Scrapy provides a web crawler shell, the Scrapy Shell, that developers can use to test their assumptions about site behavior. 
To enter the Scrapy console, execute: scrapy shell in the console. Next, you need to run the parser on the page using the fetch command in the shell. 
Before that, it is better to save the address of the page that we will parse into a variable: url = '<https://quotes.toscrape.com/'>.

After executing fetch(url),

>>> url = 'https://quotes.toscrape.com/'
>>> fetch(url)


the console will look something like this:
2021-07-24 07:40:13 [scrapy.core.engine] INFO: Spider opened
2021-07-24 07:40:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/> (referer: None)

The parser returns a response, which can be viewed using the view(response) command. 
And the page will open in the default browser. You can view the raw HTML using the print(response.text) command.
"""

# Using XPath to extract

XPath = """
is a query language for selecting nodes in XML documents. You can navigate the document using XPath. 
Scrapy uses this language to work with HTML document objects.

It is better to read the detailed documentation on using the XML parser in Scrapy on the documentation page.
"""


# To get a list of all quote authors on a page, you can do:
"""
>>> fetch(url)
2022-10-02 00:33:26 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/> (referer: None)
>>> response
<200 https://quotes.toscrape.com/>
>>> response.xpath("/html//small").extract()"""

# The result will be a list:
[
    '<small class="author" itemprop="author">Albert Einstein</small>',
    '<small class="author" itemprop="author">J.K. Rowling',
    '<small class="author" itemprop="author">Albert Einstein</small>',
    '<small class="author" itemprop="author">Jane Austen</small>',
    '<small class="author" itemprop="author">Marilyn Monroe</small>',
    '<small class="author" itemprop="author">Albert Einstein</small>',
    '<small class="author" itemprop="author">André Gide</small>',
    '<small class="author" itemprop="author">Thomas A. Edison</small>',
    '<small class="author" itemprop="author">Eleanor Roosevelt</small>',
    '<small class="author" itemprop="author">Steve Martin</small>',
]

# To get only the text from the tags, you need to add /text() to the Xpath expression:
command = "response.xpath(\"/html//small[@class='author']/text()\").extract()"

# The resulting list will contain only the names of the authors:
[
    "Albert Einstein",
    "J.K. Rowling",
    "Albert Einstein",
    "Jane Austen",
    "Marilyn Monroe",
    "Albert Einstein",
    "André Gide",
    "Thomas A. Edison",
    "Eleanor Roosevelt",
    "Steve Martin",
]


# Creating a Scrapy project

commangd = "scrapy startproject test_spyder"
"""
As a result, the structure of the project will be approximately as follows:

.
└── test_spyder
     ├── scrapy.cfg
     └── test_spyder
         ├── __init__.py
         ├── items.py
         ├── middlewares.py
         ├── pipelines.py
         ├── settings.py
         └── spiders
             └── __init__.py
"""

# After creating the project, you need to go to a new folder and write the following command:
command = "scrapy genspider authors quotes.toscrape.com"

# The command will create a spider template in spyders/authors.py:
# class AuthorsSpider(scrapy.Spider):
#      name = 'authors'
#      allowed_domains = ['quotes.toscrape.com']
#      start_urls = ['<http://quotes.toscrape.com/>']

#      def parse(self, response):
#          pass


"""
- name is the name of the robot. Good and well-chosen names will make it easier to track all existing robots. 
They must be unique, because they are what are used to run the scrapy crawl name_of_spider command.

- allowed_domains (optional) – list of domains allowed for parsing. Requests to URLs not in this list will not be executed. 
It should only include the domain of the site (e.g. aliexpress.com) and not the entire URL specified in start_urls, otherwise errors will occur.

- start_urls - request to the mentioned URLs. From them, the robot will start searching, if a specific URL is not specified. 
The first pages loaded will be the ones listed here. Subsequent requests will be generated sequentially from the data stored in the initial URLs.

- parse – This function is called when the URL has been successfully parsed. It is also called a callback function.
 The Response (used in the Scrapy wrapper) is returned as the result of the parsing, passed to this function, and contains the code to extract.
"""

# The parse method should return:

"""- the Request object, which is a new request and the result of which will be processed in parse again;
- the Item object, which will be processed and stored;
- a dictionary that behaves similarly to Item.


Scrapy uses the Tornado framework and all methods that are executed asynchronously must be generators, 
parse being one such method. Scrapy uses the type of the returned result to determine what to do with it.

For parse to be a generator, you must return results from it using the yield statement."""


# Parsing HTML using XPath


"""Using the browser, you can determine that all blocks of code with quotes are inside a div tag with a quote class. 
Then we will loop through all the blocks on the page that match this Xpath expression:
"""

code = "for quote in response.xpath(\"/html//div[@class='quote']\"):..."

# Inside each block, keywords are inside a link tag, which itself is inside a div tag with the tags class. The keywords can then be retrieved using Xpath:

code = """for quote in response.xpath("/html//div[@class='quote']"):
     keywords = quote.xpath("div[@class='tags']/a/text()").extract()"""

"""The authors of the quotes are inside the small tag, which in turn is inside the span tag, and the quote text is inside the span tag with the text class.
"""


# Let's return the dictionary with the collected information:
# class AuthorsSpider(scrapy.Spider):
#      name = 'authors'
#      allowed_domains = ['quotes.toscrape.com']
#      start_urls = ['http://quotes.toscrape.com/']

#      def parse(self, response):
#          for quote in response.xpath("/html//div[@class='quote']"):
#              yield {
#                  "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
#                  "author": quote.xpath("span/small/text()").extract(),
#                  "quote": quote.xpath("span[@class='text']/text()").get()
#              }


"""

The result can be seen in the console, for this we will launch the spider with the command: scrapy crawl authors.

The output will be large, but not too informative. Therefore, it is better to save the scraping results to a file.
"""

# Let's save the collection result in a CSV tabular document. To do this, we will add two settings to settings.py:
FEED_FORMAT = "csv"
FEED_URI = "result.csv"

"""The scraping results will now be saved in the result.csv file.
"""
# keywords, author, quote
# "change, deep-thoughts, thinking, world", Albert Einstein, "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# "abilities, choices", J.K. Rowling,"“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
# "inspirational, life, live, miracle, miracles", Albert Einstein, “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# "alliteracy,books,classic,humor",Jane Austen,"“The person, be it gentleman or lady, who has no pleasure in a good novel, must be intolerably stupid.”"
# "be-yourself,inspirational",Marilyn Monroe,""Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.""
# "adulthood, success, value", Albert Einstein, "Try not to become a man of success. Rather become a man of value.”
# "life, love", André Gide, "It is better to be hated for what you are than to be loved for what you are not."
# "edison,failure,inspirational,paraphrased",Thomas A. Edison,"“I have not failed. I've just found 10,000 ways that won't work.""
# misattributed-eleanor-roosevelt, Eleanor Roosevelt, “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# "humor,obvious,simile",Steve Martin,"“A day without sunshine is like, you know, night.”"


# Pagination

"""
The parse method can return a Request object and then Scrapy will make the request and process it, passing the response to parse. 
By looking at the code of the page, you can determine that the link to the next page is under the li tag with the next class. 
All links are placed in the href attribute of a tag. Then the expression to get the link to the next page will be: response.xpath("//li[@class='next']/a/@href").get().

This will not be a full link, but only a relative path, we will get the full path by adding the domain and the relative path self.start_urls[0] + next_link.
"""


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get(),
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)


"""
When the spider reaches the last page of the pagination, there will be no next button and the next request will not be generated.

After executing the scrapy crawl authors command, the results of a new scraping with pagination will be added to the result.csv file.

Here we need to clarify a few points regarding a live example. The structure of the project is the same, but the return of the result to the result.csv file has been removed.

Because the sample size is limited to 1024 MB and each run of the sample will increase the result.csv file. 
Second, since the example can only be run by running the main.py file in the replit system, the crawler is run as a script, not by running the scrapy crawl authors command.
"""


# import scrapy
# from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get(),
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)


# run spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()


# If we wanted to use the main.py script to save the result to the result.csv file, then just add the custom_settings attribute to the QuotesSpider class:


class QuotesSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {"FEED_FORMAT": "csv", "FEED_URI": "result.csv"}
    ...
