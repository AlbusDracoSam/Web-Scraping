from bs4 import BeautifulSoup
import requests
import time

print("Tell us the Unfamiliar skills")
unfamiliar = input(">")
print(f" Filtering out {unfamiliar}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    job = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

    for index , j in enumerate(job) :
        date = j.find('span' , class_ = 'sim-posted').text
        if 'few ' in date :

            comp_name = j.find('h3' , class_ = 'joblist-comp-name').text.replace(" " , "")
            skills = j.find('span', class_ = "srp-skills").text.replace(" " ,"" )
            more_info = j.header.h2.a['href']

            if unfamiliar not in skills :
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name : {comp_name.strip()}")
                    f.write(f"Skills : {skills.strip()}")
                    f.write(f"More = info : {more_info}")
                    print('File {index}.txt saved')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10 ;
        print(f'Waiting {time_wait} seconds...')
        time.sleep(30)