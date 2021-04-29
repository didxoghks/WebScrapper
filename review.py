import requests # 페이지의 html 정보를 가져오는 함수
from bs4 import BeautifulSoup # 페이지의 html 을 가공할 수 있는 함수

URL = "https://kr.indeed.com/jobs?q=&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%82%B0"
# https://kr.indeed.com/jobs?q=&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%82%B0&start=10
LIMIT = 10

def extract_kmong_pages(): #크몽 페이지 개수 가져오는 함수

    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser") #parser 뜻이 문장을 구성성분들로 분해한다 parsing : 구문 분석이라는 뜻
                                                    #즉 이 페이지HTML을 부분별로 분석하게 가공해라

    pagination = soup.find("ul", {"class": "pagination-list"})
    #pagination 은 paging 즉  '쪽수 매기기'라고 불린다.

    links = pagination.find_all('a') # 이 pagination 에는 beautifulsoup 로 html.parser 한 가공처리 html 이 담겨있기 때문에
                                     # BeautifulSoup 의 함수인 .find_all 을 사용할 수 있다.

    pages =[]
    for link in links[:-1]:
        pages.append(link.string)

    max_page = pages[-1]
    print(max_page)

    return max_page

def extract_jobs():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html,parser")
    title = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    print(title)

def extract_inform(html):

    anchor = html.find("h2", {"class": "title"})
    title = anchor.find("a")["title"]
    # 혹은 title = anchor.find("a").string
    company = html.find("div", {"class": "sjcl"})
    company = company.find("span", {"class": "company"})
    if (company.find("a") is not None):
        company = company.find("a").string
    else:
        company = company.string
    company = company.strip()

    return {'title': title, 'company': company}


def extract_indeed_jobs(last_page):
    jobs = []

    #for page in range(int(last_page)):
        #result = (f"{URL}&start={page*LIMIT}")
    result2 = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result2.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for html in results:
        jobs.append(extract_inform(html))


    return jobs

last_page = extract_kmong_pages()
result = extract_indeed_jobs(last_page)
print(result)