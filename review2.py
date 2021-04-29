import requests
from bs4 import BeautifulSoup

URL = "https://kr.indeed.com/%EA%B2%BD%EA%B8%B0%EB%8F%84-%EC%95%88%EC%82%B0-%EC%A7%80%EC%97%AD-%EC%B7%A8%EC%97%85"


def page_number():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("ul" , {"class" : "pagination-list"})

    links = pagination.find_all('a')

    pages = []

    for link in links[:-1]:
        pages.append(link.string) # 이제 보면 ~~~~~~~~ string 이 뭔 뜻인지 그리고 aria-label 을 가져오려면 어떻게 해야하는지

    max_page = pages[-1]
    print(max_page)

    return max_page

def extract_jobcard():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    job_card = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"}) #find 는 하나만 찾고 find_all 은 모두 찾음

    return job_card

def extrct_inform():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    card = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})  # find 는 하나만 찾고 find_all 은 모두 찾음
    #find_all 은 리스트 반환

    #find 는 문자열 반환
    #print 해보면서 문자열이면 .string 바로 써보고
    #리스트면 하나씩 꺼내서 .string 쓰고


    for c in card:
        title =  c.find("h2", {"class" : "title"})
        title = title('a')[title]


    # for b in card:
    #     #company = c.find("div", {"class" : "sjcl"})
    #     company = c.find("a")
    #     print(company)




page_number()
job_card = extract_jobcard()
extrct_inform()
