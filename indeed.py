import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit="

# indeed 페이지 추출
def extract_indeed_pages():
    res = requests.get(f"{URL}{LIMIT}")
    # print(indeed_res.text)
    soup = BeautifulSoup(res.text, "html.parser")
    # print(indeed_soup)
    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
    # print(page.find("span"))
        pages.append(int(link.string))
    # print(pages)
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    # print(title)
    company = html.find("span", {"class": "company"})

    if company:
        company_anchor = company.find("a")
        # python strip 사용하여 양쪽 공백제거
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else :
        company = None
    location = html.find("div", {"class" : "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    # print(job_id)
    # print(location)
    # print(title, company)
    return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(last_page):

    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        # result : 각 일자리(soup object)
        result = requests.get(f"{URL}{LIMIT}&start={page*LIMIT}")
        # print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        # print(results)
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_page)
    return jobs