from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.pipelines import TextPipeline

process = CrawlerProcess(get_project_settings())
process.crawl('reviewbot1.py', domain='https://movie.daum.net/moviedb/main?movieId=2')
process.start() # the script will block here until the crawling is finished
print(TextPipeline.list_csv)