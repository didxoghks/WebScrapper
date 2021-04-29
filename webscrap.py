
import requests
from bs4 import BeautifulSoup



indeed_result = requests.get("https://kr.indeed.com/jobs?q=&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%82%B0&limit=50&fromage=3&radius=25&start=500")


indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div",{"class" : "pagination"})

pages = pagination.find_all('a')

spans= []


for page in pages:
    spans.append(page.find("span"))

spans = spans[1:-1]

print(spans)
