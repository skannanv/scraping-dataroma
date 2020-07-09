from locators.InvestorLocators import InvestorLocators

class InvestorParser:

    def __init__(self,parent):
        self.soup = parent

    def __repr__(self):
        return f'Investor {self.name}'

    @property
    def name(self):
        locator = InvestorLocators.NAME_LOCATER
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name
