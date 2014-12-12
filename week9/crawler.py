from sqlalchemy import create_engine
from models import Website, Pages
from sqlalchemy.orm import Session
from connect import Base
from bs4 import BeautifulSoup, Doctype
from urllib.parse import urljoin, urlparse
from datetime import datetime
import requests


class Crawler:

    def __init__(self, session):
        self.session = session
        self.links = []
        self.visited = []

    def get_html(self, url):
        r = requests.get(url)
        html = r.text
        return BeautifulSoup(html)

    def parse_url(self, url, link):
        return urljoin(url, link)

    def get_page_hrefs(self, html):
        pages = [link.get("href") for link in html.find_all("a")]
        return pages

    def crawl_links(self, url):
        if url in self.visited:
            return
        print(url)

        self.visited.append(url)
        soup = self.get_html(url)
        pages = self.get_page_hrefs(soup)

        self.save_info_to_database(soup, url)

        for page in pages:
            new_link = self.parse_url(url, page)
            if self.can_be_scanned(new_link, url):
                self.links.append(new_link)

    def do_the_crawl(self, url):
        self.crawl_links(url)
        while len(self.links) > 0:
            self.crawl_links(self.links.pop())

    def get_page_main_url(self, page):
        parsed_uri = urlparse(page)
        url = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return url

    def is_outgoing(self, current_url, main_url):
        main_url = self.get_page_main_url(main_url)
        current_url = self.get_page_main_url(current_url)
        if main_url == current_url:
            return False
        return True

    def can_be_scanned(self, currend_url, main_url):
        has_hashtag = "#" in currend_url
        is_relative = "../" in currend_url
        is_visited = currend_url in self.visited

        if has_hashtag or is_visited or is_relative or self.is_outgoing(currend_url, main_url):
            return False
        return True

    def save_info_to_database(self, soup, url):
        if "DOCTYPE html" in soup:
            print("YES")

        try:
            description = soup.find(property="og:description")["content"]
            title = soup.title.string
        except Exception:
            print("Image link")
            return

        if "https://" in url:
            ssl = 1
        else:
            ssl = 0

        domain = self.get_page_main_url(url)

        current_time = datetime.now()

        hrefs = self.get_page_hrefs(soup)
        pages_count = len(hrefs)
        outgoing_hrefs = [self.parse_url(url, href) for href in hrefs if domain not in self.parse_url(url, href)]
        outgoing_hrefs = len(outgoing_hrefs)

        website = Website(title=title, domain=domain, pages_count=pages_count)
        self.session.add(website)
        self.session.commit()

        site = self.session.query(Website).filter(Website.domain == domain).first()
        site.pages = [Pages(date=current_time, url=url, title=title, desc=description, ads=outgoing_hrefs, SSL=ssl)]
        self.session.commit()


def main():
    engine = create_engine("sqlite:///search.db")

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    crawler = Crawler(session)
    url = "http://radorado.me"
    crawler.do_the_crawl(url)


if __name__ == "__main__":
    main()
