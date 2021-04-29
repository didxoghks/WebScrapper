from indeed24 import extract_indeed_pages, extract_indeed_jobs


last_page = extract_indeed_pages()
jobs = extract_indeed_jobs(last_page)
print(jobs)
