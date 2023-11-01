![alt text]([http://url/to/img.png](https://sun9-34.userapi.com/c638919/v638919329/5cec2/QKWkOlPn0sQ.jpg))
## HH Vacancy Scraper



Python script for scraping job vacancies from the HeadHunter job board (hh.ru) and automatically opening application pages for specific employers. It can be useful for job seekers who want to automate the process of applying for jobs.


## Features

- Scrape job vacancies from HeadHunter by job title and region.
- Automatically open job application pages for specific employers


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Install the required libraries using pip:
```
pip install requests webbrowser pyautogui rich
```

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## How to Use

1. Clone this repository to your local machine:
```
git clone https://github.com/Genone22/python_hh_vacancy_scraper.git
```
2. Modify the job_titles and regions lists to match your job search criteria. You can add or remove job titles and regions as needed.

3. Run the script by executing the following command:

```
python vacancy_scraper.py
```

The script will scrape job vacancies based on your criteria and open the application pages for employers not in the specified exclusion list.

## Configuration

You can configure the following options in the script:

job_titles: List of job titles you are interested in.
regions: List of region codes (e.g., Moscow is 113).
page_range: The range of pages to scrape for each job title and region.
exclude_employers: List of employer names to exclude from opening application pages.

## Notes

The script may open a web browser and simulate keyboard shortcuts to close tabs.
Make sure you understand the behavior of the script before running it.

Use this script responsibly and ensure that your actions comply with the terms and conditions of the HeadHunter job board.

## Disclaimer

This script is provided as-is and comes with no warranties or guarantees. Use it at your own risk.

Lucky job hunting mate!
