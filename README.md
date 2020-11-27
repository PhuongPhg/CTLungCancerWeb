# CTLungCancerWeb

## Source 1:
- Directory /one
- Url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420/
- How to use:
1. Go to one/one/spiders
2. Run in Terminal: scrapy runspider ImgSpyder.py -o output.json
3. Output: image urls + title + caption

## Source 2:
- Crawler tool use: Selenium
- Directory /ERJ
- Url: https://erj.ersjournals.com/content/19/4/722.figures-only
- How to use:
1. Install the specify browser web driver based on the browser you use, [More Information](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) 
2. Go to folder ERJ
3. Run file test3.py
4. Output:
    - Csv file: erj_crawl.csv
    - In terminal: Images title + Images link
