import requests

from pages.all_investors_page import AllInvestorsPage

URL = "https://www.dataroma.com/m/home.php"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#r = requests.get(url=urlLogin, params=params, headers=headers)
page_content = requests.get(URL, allow_redirects=True, headers=headers).content
page = AllInvestorsPage(page_content)

investors = page.investors

for inv in investors:
    print(inv)



