# 프로젝트 제목
Crawler_for_SentimentAnalysis with Scrapy
![2323](https://user-images.githubusercontent.com/43494047/93021119-f1d46580-f61b-11ea-9a70-ed591cdd50ac.png)

## 설치 방법 (Installation)
Go to the Crawler folder and
```python
pip install -r requirements.txt
```
then run main.py

## 사용 방법 (Usage)
This Crawler targeted on Daum movie reviews.

Here is main.py // file
You can change the main.py for your conveninence

```python
from crawler.utils import MovieCrawler
url = 'https://movie.daum.net/moviedb/main?movieId=1'

if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    crawler = MovieCrawler()
    crawler.crawl(url)
```
