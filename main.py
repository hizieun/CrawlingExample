# #2.2 Navigating with Python
# import requests
# from bs4 import BeautifulSoup

# indeed_res = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# # print(indeed_res.text)

# indeed_soup = BeautifulSoup(indeed_res.text, "html.parser")

# # print(indeed_soup)

# pagination = indeed_soup.find("div", {"class": "pagination"})

# # print(pagination)

# links = pagination.find_all('a')
# pages = []
# # print(pages)

# # for link in links:
# #     # print(page.find("span"))
# #     pages.append(link.find("span").string)
# # pages = pages[0:-1]
# # print(pages)

# # integer로 변환
# for link in links[:-1]:
#     # print(page.find("span"))
#     pages.append(int(link.string))
# print(pages)
# # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# max_page = pages[-1]
# print(range(max_page)) # range(0, 20)

# for n in range(max_page):
#     # print(n * 50)
#     print(f"start={n*50}")


# from indeed import extract_indeed_pages, extract_indeed_jobs
from indeed import get_jobs as get_indeed_jobs
from stackOverflow import get_jobs as get_so_jobs
from save import save_to_file

# last_indeed_pages = extract_indeed_pages()
# # print(last_indeed_pages) # 20
# indeed_jobs = extract_indeed_jobs(last_indeed_pages)
# print(indeed_jobs)
# print(so_jobs)


# indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs
# print(jobs)
save_to_file(jobs)


