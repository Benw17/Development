class PageInfo:
    def __init__(self, title, description):
        self.title = title 
        self.description = description

pages = {
    "index": PageInfo(
        "Slyce | Fractional Property Investments",
        "Invest in property from just $25 with Slyce. Diversify your portfolio, "
        "earn rental income, and access real estate without saving hundreds of thousands upfront."
    ),
    "early_investors": PageInfo(
        "Early Investors at Slyce | Join the Future of Property Investment",
        "Become an early investor with Slyce and help shape the future of property investment. "
        "Gain exclusive benefits and be part of a growing community transforming real estate."
    ),
    "security": PageInfo(None, None),
    "team": PageInfo(None, None),
    "contact": PageInfo(None, None),
}