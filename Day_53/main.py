from scrape_data import ScrapeData
from store_data import StoreData


def main():
    scrape_data: ScrapeData = ScrapeData()

    store_data: StoreData = StoreData(scrape_data.get_listing_data())


if __name__ == '__main__':
    main()
