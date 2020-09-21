from crawler.utils import MovieCrawler
url = 'https://movie.daum.net/moviedb/main?movieId=1'

if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    crawler = MovieCrawler()
    crawler.crawl(url)