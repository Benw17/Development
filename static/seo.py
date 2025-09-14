index_title = "Slyce | Fractional Property Investments"
index_description = "Invest in property from just $25 with Slyce. Diversify your portfolio, earn rental income, and access real estate without saving hundreds of thousands upfront."

early_investors_title = "Early Investors at Slyce | Join the Future of Property Investment"
early_investors_description = " Become an early investor with Slyce and help shape the future of property investment. Gain exclusive benefits and be part of a growing community transforming real estate."

security_title = ""
security_description = ""

team__title =  ""
team_description = ""

contact_title = ""
contact_description = ""

class PageInfo:
    def __init__(self, title, description):
        self.title = title 
        self.description = description

index_page = PageInfo(index_title, index_description)
early_investors_page = PageInfo(early_investors_title, early_investors_description)
security_page = PageInfo(security_title, security_description)
team_page = PageInfo(team__title, team_description)
contact_page = PageInfo(contact_title, contact_description)