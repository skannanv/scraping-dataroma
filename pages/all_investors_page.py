from bs4 import BeautifulSoup

from locators.All_Investors_Locator import AllInvestorsPageLocators
from parsers.investor_parser import InvestorParser


class AllInvestorsPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def investors(self):
        return [InvestorParser(e) for e in self.soup.select(AllInvestorsPageLocators.INVESTORS)]
