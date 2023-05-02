def save_to_file(keyword, jobs):
    try:
        with open(f"{keyword}_jobs_data.csv", "w", encoding = "utf-8") as file:
            file.write("Company, Location, Position, Job Type, URL\n")
            for job in jobs:
                file.write(f"{job['company']}, {job['location']}, {job['position']}, {job['job_type']}, {job['url']}\n")
        print(f"Job data was successfully written to {keyword}_jobs_data.csv.")
    except Exception as e:
        print(f"An error occurred while writing job data to CSV: {e}")
        exit()