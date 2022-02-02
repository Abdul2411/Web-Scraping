import requests
from bs4 import BeautifulSoup

import pandas as pd
df = pd.DataFrame()


def ps4_games(page_number):
    Title = []
    Price = []
    Link_urls = []
    Description = []
    AdditionalInfo = []
    page_num = 1
    while page_num <= page_number:

        page_url = f"?Sort=Relevance&TypeGames=on&PriceFrom=&PriceTo=&Meta=All&GameType=All&PEGI=All&Internet=All" \
                   f"&GamePlayFrom=&GamePlayTo=&ReleaseDateFrom=All&ReleaseDateTo=All&Page={page_num}&OnlyListing=true "
        loadmore_url = f"https://gamenation.in/PlayStation/PS4{page_url}"
        r = requests.get(loadmore_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        ps4Games = soup.find_all("a", class_="game-card-link")

        for ps4Data in ps4Games:
            ps4GameLinks = ps4Data.get("href")

            Link_urls.append(ps4GameLinks)

        for link in range(len(Link_urls)):
            newLink_url = Link_urls[link]
            r = requests.get(newLink_url)
            soup = BeautifulSoup(r.content, 'html.parser')

            ps4AboutGames = soup.find_all(class_="content-wrap no-banner pt-0")

            for ps4PageData in ps4AboutGames:

                ps4Titles = ps4PageData.find(id = "ProductName").text
                Title.append(ps4Titles)
                # print(ps4Titles)

                ps4prices = ps4PageData.find(id = "ProductPrice").text
                Price.append(ps4prices)
                # print(ps4prices)
                abouts = ps4PageData.find("div", class_="description").getText("p", "br")
                Description.append(abouts)
                additionalInfos = ps4PageData.find("div", class_="requirements-block").getText("h2".strip("h2"))
                AdditionalInfo.append(additionalInfos)

        page_num = page_num + 1
    df['Game Title'] = Title
    df['Price'] = Price
    df['Description'] = Description
    df['Additional Info'] = AdditionalInfo
    df["Link"] = Link_urls
    df.to_csv(r'C:\Users\A\PycharmProjects\pythonProject\Ps4GameData.csv', index=True)


def ps5_games(page_number):
    Title = []
    Price = []
    Link_urls = []
    Description = []
    AdditionalInfo = []

    page_num = 1
    while page_num <= page_number:

        page_url = f"?Sort=Relevance&TypeGames=on&PriceFrom=&PriceTo=&Meta=All&GameType=All&PEGI=All&Internet=All" \
                   f"&GamePlayFrom=&GamePlayTo=&ReleaseDateFrom=All&ReleaseDateTo=All&Page={page_num}&OnlyListing=true "
        loadmore_url = f"https://gamenation.in/PlayStation/PS5{page_url}"
        r = requests.get(loadmore_url)
        soup = BeautifulSoup(r.content, 'html.parser')

        ps5Games = soup.find_all("a", class_="game-card-link")

        for ps5Data in ps5Games:
            ps5GameLinks = ps5Data.get("href")

            Link_urls.append(ps5GameLinks)

        for link in range(len(Link_urls)):
            newLink_url = Link_urls[link]
            r = requests.get(newLink_url)
            soup = BeautifulSoup(r.content, 'html.parser')

            ps5AboutGames = soup.find_all(class_="content-wrap no-banner pt-0")

            for ps5PageData in ps5AboutGames:

                ps5Titles = ps5PageData.find(id = "ProductName").text
                Title.append(ps5Titles)

                ps4prices = ps5PageData.find(id = "ProductPrice").text
                Price.append(ps4prices)
                # print(ps4prices)
                abouts = ps5PageData.find("div", class_="description").getText("p", "br")
                Description.append(abouts)
                additionalInfo = ps5PageData.find("div", class_="requirements-block").getText("h2".strip("h2"))
                AdditionalInfo.append(additionalInfo)

        page_num = page_num + 1
    df['Game Title'] = Title
    df['Price'] = Price
    df['Description'] = Description
    df['Additional Info'] = AdditionalInfo
    df["Link"] = Link_urls
    df.to_csv(r'C:\Users\A\PycharmProjects\pythonProject\Ps5GameData.csv', index=True)


ps5_games(1)
