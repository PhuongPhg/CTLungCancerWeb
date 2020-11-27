# CTLungCancerWebCrawler

- Crawler tool use: Selenium
- Data source: https://erj.ersjournals.com/content/19/4/722.figures-only
- How to use:
1. Install the specify browser web driver based on the browser you use. [More Information](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/) 
2. Go to folder ERJ
3. Run file `test3.py`
4. Output:
    - Csv file: erj_crawl.csv
    - In terminal: Images title + Images link
- Function explanation: 
    + `Driver`: Web browser driver to use
    + `find_elements_by_class_name()`: Finds elements by class name
    + `find_element_by_tag_name()`: Finds elements by class name
    + `get_attribute()`: Get attributes of an element
    + `csv.writer`: Returns a writer object which writes data into CSV file

- Limitation: Requires specify web browser driver to use