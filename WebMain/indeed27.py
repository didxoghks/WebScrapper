
import requests
from bs4 import BeautifulSoup

#LIMIT = 50
#URL = f"https://kr.indeed.com/jobs?q=&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%82%B0&limit=" \
#      f"50&fromage=3&radius=25&start={LIMIT}"
# 이건 스택오버플로우 싸이트
NUMBER = 1
URL = "https://stackoverflow.com/search?page={NUMBER}&tab=Relevance&q=blockchain"
def get_last_pages():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []

    for link in links[1:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page


def extract_job(html):

    title = html.find("a")["title"]
    #이렇게는 안되요 title = result.find("h2",{"class": "title"})
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")

        if(company_anchor is not None):
            company = company_anchor.string
        else:
             company = company.string


    company = company.strip()

    location = html.find("span", {"class": "location accessible-contrast-color-location"}).string
    job_id = html["data-jk"]

    # for err in location:
    #    if(err ==  "None"):
    #        print("None입니다")

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://kr.indeed.com/viewjob?jk={job_id}&from=serp&vjs=3"
    }


def extract_jobs(last_page):

    jobs = []
    for page in range(last_page):
        print(f"Scrapping page is {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        #results = soup.find_all("h2", {"class": "title"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)


    return jobs

def get_jobs():
    last_page = get_last_pages()
    jobs = extract_jobs(last_page)
    return jobs


