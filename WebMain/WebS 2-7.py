'''from indeed27 import extract_indeed_pages, extract_indeed_jobs


last_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_page)
print(indeed_jobs)'''

from indeed27 import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)