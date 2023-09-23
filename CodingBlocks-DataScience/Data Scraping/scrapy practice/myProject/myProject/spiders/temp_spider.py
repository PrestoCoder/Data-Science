import scrapy
from pathlib import Path

class QuotesSpider(scrapy.Spider):
	name = "rohan"

	# These 2 methods help in working with spider

	def start_requests(self):
		urls = [
			'https://quotes.toscrape.com/page/1',
			'https://quotes.toscrape.com/page/2',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)


	# It basically writes the html body onto the file
	# We can even use normal data scrapping to write specific tags as well.
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = f'quotes-{page}.html'
		Path(filename).write_bytes(response.body)
		self.log(f'Saved file {filename}')