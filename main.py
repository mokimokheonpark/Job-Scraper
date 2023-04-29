from extractors.weworkremotely import extract_weworkremotely_jobs

keyword = input("Please enter your keyword: ")

try:
    weworkremotely_jobs = extract_weworkremotely_jobs(keyword)
except Exception as e:
    print(f"An error occurred while extracting job data: {e}")
    exit()

if not weworkremotely_jobs:
    print("No job data was found for the given keyword.")
    exit()

keyword = keyword.replace(" ", "_")

try:
    with open(f"{keyword}_jobs_data.csv", "w", encoding = "utf-8") as file:
        file.write("Company, Location, Position, Job Type, URL\n")
        for job in weworkremotely_jobs:
            file.write(f"{job['company']}, {job['location']}, {job['position']}, {job['job type']}, {job['url']}\n")
    print(f"Job data was successfully written to {keyword}_jobs_data.csv.")
except Exception as e:
    print(f"An error occurred while writing job data to CSV: {e}")
    exit()