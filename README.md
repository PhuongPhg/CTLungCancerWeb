# CTLungCancerWeb

## Source 1:
- Directory crawler/ERJ
- Url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419420/
- How to use:
1. Go to one/one/spiders
2. Run in Terminal: scrapy runspider ImgSpyder.py -o output.json
3. Output: image urls + title + caption

## Source 2:
- Data source: https://erj.ersjournals.com/content/19/4/722.figures-only
- Crawler tool use: Selenium
- Directory crawler/ERJ


## Source 3:
- Data source: https://radiopaedia.org/articles/lung-cancer-3
- Crawler tool use: BeautifulSoup
- Directory [Crawler/Radiopaedia]('./crawler/radiopaedia')

## csv_to_json:
To use this, run command
```
python csv_to_json.py [csvFilePath] [jsonFilePath]
```