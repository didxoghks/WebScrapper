
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%82%B0&limit=" \
      f"50&fromage=3&radius=25&start={LIMIT}"

def extract_indeed_pages():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []

    for link in links[1:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        #얜 안되여results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard unifiedRow row result clickcard"})
        # 보니까 job~~Card 뒤에 uni~~~를 빼야함

        results = soup.find_all("h2", {"class" : "title"})

    for result in results:
        jobs.append(result.find("a")["title"])

    return jobs


