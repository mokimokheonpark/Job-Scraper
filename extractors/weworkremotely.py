from requests import get
from bs4 import BeautifulSoup

def extract_weworkremotely_jobs(keyword):

    # Extract job postings from the We Work Remotely website based on a provided keyword.

    # Argument: keyword (str), the keyword to search for in the job postings.

    # Returns a list of dictionaries, where each dictionary represents a job posting and contains
    # the following fields: "url", "company", "job type", "location", and "position".
    
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    full_url = f"{base_url}{keyword}"
    response = get(full_url)

    if response.status_code != 200:
        raise Exception("Can't request the weworkremotely website")
    
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")

    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop()

        for post in job_posts:
            anchors = post.find_all("a")
            anchor = anchors[1]
            url = anchor["href"]
            company, job_type, location = anchor.find_all("span", class_ = "company")
            position = anchor.find("span", class_="title")

            job_data = {
                "url": f"https://weworkremotely.com{url}",
                "company": company.string.replace(",", " "),
                "job type": job_type.string.replace(",", " "),
                "location": location.string.replace(",", " "),
                "position": position.string.replace(",", " ")
            }
            
            results.append(job_data)
    
    return results