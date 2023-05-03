# Job-Scraper-Project

This project is a Python web application that scrapes job postings from job platform websites and allows users to search for job listings by keyword and save the data to a CSV file.

## Features

The Project has the following features:

- Scrapes job postings from the We Work Remotely website, which is a popular platform for remote job listings.
- Allows users to search for job postings based on a specific keyword.
- Collects relevant job data such as company name, location, job title and job type.
- Supports users in exporting the collected job data to a CSV file for easy analysis and manipulation.
- Handles exceptions and errors gracefully, informing users when something goes wrong and how to resolve it.

## Dependencies

This project requires the following Python libraries and framework:

- Requests: a library that simplifies sending HTTP requests in Python.
- BeautifulSoup: a library for parsing HTML and XML files to extract relevant data.
- Flask: a lightweight web framework for building web applications in Python.

## Installation

To get started with the project, follow the steps below:

1. Clone the repository using the following command: git clone https://github.com/mokimokheonpark/Job-Scraper-Project.git
2. Install the required libraries and framework using the following command: pip install requests beautifulsoup4 flask

## Usage

To use the web application, follow the steps below:

1. Navigate to the project directory using the terminal.
2. Run the "main.py" file to start the application using the following command: python main.py
3. Open your web browser and navigate to "http://localhost:5000".
4. Enter a keyword in the search bar and click "Search" to retrieve job listings.
5. View the job listings and click "Export to csv file" to download a CSV file containing the job data.
6. Press CTRL+C in terminal to quit the application.

## Improvements

The following are some potential improvements with future updates for the project:

- Add support for scraping job postings from other websites, such as Indeed or LinkedIn.
- Implement a more advanced filtering system to allow users to narrow down their job search results.

## Contributions

Contributions to the project are welcome! If you find any issues or have any suggestions for improvement, feel free to create an issue or a pull request.

## License

The project is licensed under the MIT License.
