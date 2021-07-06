# import crawling
import crawling_1
import pymysql

from concurrent.futures import ThreadPoolExecutor ## 비동기처리
from concurrent.futures import ProcessPoolExecutor
# crawling.print_test()

page = 13323069
# page = str(page)
# url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

# with ThreadPoolExecutor(max_workers=3) as executor:
#         executor.submit(crawring_1.do_crawl,url)

# crawring_1.do_crawl(url)

while page > 13322569:
    page = str(page)
    url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"


    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(crawling_1.do_crawl, url)

        page = int(page)
        page -= 1
# crawling_1.do_crawl(url)


# '''
# while page > 13322069 :
#     page = str(page)
#     url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

#     with ThreadPoolExecutor(max_workers=3) as executor:
#         executor.submit(crawling.do_crawl, url)

#         page = int(page)
#         page -= 1
# '''