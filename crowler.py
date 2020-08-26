"""
    File: crawler.py
    Author: Emanuel Inacio
    Purpose: Crawls jobs from indeed.com by searching by a given "job" title and other
    criteria entered by the user
    Date Created: 08/16/2020
"""


from urllib import request, error
from bs4 import BeautifulSoup
import re
import pandas as pd


def crawl_results(url, years_of_experiece):
    """
        Pulls data from a web page given by url and gets all the jobs that match
        a given criteria

        Parameters: url is the url to fetch html page from,
        years_of_experience is the max years of experience of the desired job

        Returns: no return value

        Pre-condition:  url and years_of_experience are both strings

        Post-condition: prints the jobs that has been pulled from indeed.com
        that match the given criteria
    """
    jobs = []

    try:
        search_results = request.urlopen(url).read()
        soup = BeautifulSoup(search_results, 'html.parser')

        print("Searching for jobs matching your criteria ...")

        for job in soup.find_all(class_="result"):

            # get the link of the full job description page, the title and company
            link = "https://indeed.com" + job.find(class_="turnstileLink").get('href')
            title = job.find(class_="title").get_text().strip("\n")
            company_name = job.find(class_='company').get_text().strip("\n")

            # Check if this jobs passes my criteria, i.e experience <= 2 years,
            # no US Citizenship required
            if not criteria_matches(link):
                continue

            # Append job to the list of jobs
            job = {"Title": title,  "Link": link}
            jobs.append(job)

        # Format the data as table
        job_count = len(jobs)
        df = pd.DataFrame(jobs)

        # print corresponding table and total jobs found
        print("Found the following jobs: \n\n")
        print(df.head(job_count))
        print("\nTotal Jobs Found: {}".format(job_count))

    except error.HTTPError as ex:
        print(ex)
    except error.URLError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


def criteria_matches(to_visit):
    """
        Gets the html page given by to_visit url and checks if it passes
        a given criteria (no us citizenship required and years of experience < 2

        Parameters: to_visit is the url to fetch the html page from,

        Pre-condition:  to_visit is a string holding the job url

        Post-condition: the return value is a boolean

        Returns: true if this job page passes the required criteria.
        False, otherwise
        """

    html_doc = request.urlopen(to_visit).read().decode('utf-8')

    p1 = re.compile('[2-9]\s*\+?-?\s*[2-9]?\s*[yY]e?a?r[Ss]?')
    p2 = re.compile('[Cc]itizen(ship)?')

    m = p1.search(html_doc)
    n = p2.search(html_doc)

    return not m and not n


# Program execution begins here
def main():
    years_of_experience = 2
    page_number = 0
    next_page = True

    # job_title = input("Enter the job title: \n")
    # job_title = job_title.replace(" ", "+").lower()

    job_title = "software+engineer"

    while next_page:

        if page_number == 0:
            page_number += 10
            continue

        url_to_crawl = "https://www.indeed.com/jobs?q={}&start={}".format(job_title, page_number)
        crawl_results(url_to_crawl, years_of_experience)

        print("----------------------------------------------------"
              "----------------------------------------------------\n")
        user_input = input("Go to the next page? (y/n) \n")

        if user_input.lower() != 'y':
            next_page = False

        print("\n")
        page_number += 10


main()




