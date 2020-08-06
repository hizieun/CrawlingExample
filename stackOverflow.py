import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2",{"class":"fs-body3"}).find("a")["title"]
    # print(title)
    company = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
    location = company[1].get_text(strip=True)
    companys = company[0].get_text(strip=True)
    # print(companys, location)
    job_id = html['data-jobid']
    return {
        'title': title, 
        'companys': companys, 
        'location' : location, 
        'apply_link' : f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(page+1)
        # print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        # print(result.status_code) # 200이 여러개 뜸
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            # print(result["data-jobid"])
            job = extract_job(result)
            # print(job)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    # print(last_page)
    jobs = extract_jobs(last_page)
    return jobs
