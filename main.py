import argparse
from common import config
import new_page_objects as news
import logging
logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        choices=news_sites_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site)
