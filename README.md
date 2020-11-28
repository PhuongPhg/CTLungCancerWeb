# CTLungCancerWeb

## Sources made with scrapy:
- Directory crawler/multiplesources/
- Crawler tool use: scrapy
- Source 1 NCBI: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420/
- Source 2 Wikimedia
- Source 3 Yandex
- How to use:
1. Go to crawler/multiplesources/one/spiders/
2. Run in Terminal: scrapy runspider [spydername].py

## Source 4:
- Data source: https://erj.ersjournals.com/content/19/4/722.figures-only
- Crawler tool use: Selenium
- Directory crawler/ERJ

## Source 5:
- Data source: https://radiopaedia.org/articles/lung-cancer-3
- Crawler tool use: BeautifulSoup
- Directory [Crawler/Radiopaedia](./crawler/radiopaedia)

## Source 6:
- Data source: DuckDuckGo
- Crawler tool use: Selenium
- Directory crawler/duckduckdo

## csv_to_json:
To use this, run command
```
python csv_to_json.py [csvFilePath] [jsonFilePath]
```
