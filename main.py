import requests
from bs4 import BeautifulSoup

def message():
    response = requests.get("https://news.ycombinator.com/news")
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")
    articles = soup.find_all(name="span", class_="titleline")  
    article_texts = []
    article_links = []
    for article_tag in articles:           
        text = article_tag.find("a").getText()         # get a list of text, getText 只能抓單一text, 因此用迴圈
        article_texts.append(text)
        link = article_tag.find("a").get("href")
        article_links.append(link)

    article_upvotes = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]  
    largest_upvote = max(article_upvotes)
    largest_index = article_upvotes.index(largest_upvote)

    msg= article_texts[largest_index]
    link= article_links[largest_index]
    return("\n" + msg + "\n" + link)

