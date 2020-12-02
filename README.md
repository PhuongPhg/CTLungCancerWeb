# CTLungCancerWeb

## Source 1:
- Data source: [NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420/)
- Crawler tool use: Scrapy
- Directory crawler/multiplesources/one/spiders/

## Source 2:
- Data source: [Wikimedia](https://commons.wikimedia.org/w/index.php?search=lung%20cancer%20%22lung%20cancer%22%2C%20%22ct%22%20-house%20filetype%3Abitmap&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%22fields%22%3A%7B%22phrase%22%3A%22%5C%22lung%20cancer%5C%22%2C%20%5C%22ct%5C%22%22%2C%22filetype%22%3A%22bitmap%22%2C%22not%22%3A[%22house%22]%7D%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1&fbclid=IwAR21dTtkml_wxfXCtJgCI1iy3buTgzGhlrleq76IhN8uWN2MIBXbScyZOSw)
- Crawler tool use: Scrapy
- Directory crawler/multiplesources/one/spiders/

## Source 3:
- Data source: [Yandex](https://yandex.com/images/search?text=lung%20cancer%20ct%20scan)
- Crawler tool use: Scrapy
- Directory crawler/multiplesources/one/spiders/

## Source 4:
- Data source: [ERJ](https://erj.ersjournals.com/content/19/4/722.figures-only)
- Crawler tool use: Selenium
- Directory crawler/ERJ

## Source 5:
- Data source: [Radiopaedia](https://radiopaedia.org/articles/lung-cancer-3)
- Crawler tool use: BeautifulSoup
- Directory [Crawler/Radiopaedia](./crawler/radiopaedia)

## Source 6:
- Data source: [DuckDuckGo](https://duckduckgo.com/?q=lung+cancer+ct+scan&t=h_&iax=images&ia=images)
- Crawler tool use: Selenium
- Directory crawler/duckduckdo

## Source 7:
- Data source: [OpenI](https://openi.nlm.nih.gov/gridquery?q=lung%20cancer%20ct&it=xg,c&m=1&n=100)
- Crawler tool: BeautifulSoup (bs4)
- Directory [Crawler/openi](./crawler/openi)

## Source 8:
- Data source: [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2176079/)
- Crawler tool use: Selenium
- Directory crawler/PMC

## csv_to_json:
To use this, run command
```
python csv_to_json.py [csvFilePath] [jsonFilePath]
```
