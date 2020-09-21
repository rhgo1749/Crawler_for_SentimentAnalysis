# 프로젝트 제목
Crawler_for_SentimentAnalysis with Scrapy
![2323](https://user-images.githubusercontent.com/43494047/93021119-f1d46580-f61b-11ea-9a70-ed591cdd50ac.png)

## 설치 방법 (Installation)
Go to the Crawler folder and
```python
pip install -r requirements.txt
```
then run run.py

## 사용 방법 (Usage)
This Crawler targeted on Daum movie reviews.

Here is run.py // file
You can change the run.py for your conveninence

```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Crawler.pipelines import TextPipeline

process = CrawlerProcess(get_project_settings())
process.crawl('reviewbot.py', domain='https://movie.daum.net/moviedb/main?movieId=2') # you can change the url.
process.start() # the script will block here until the crawling is finished

print(TextPipeline.list_csv) # for data analysis
```
