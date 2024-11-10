class AlbumReleasesClient():
    def __init__(self):
        self.page_scraper = AlbumReleasesScraper()
        self.page_scraper().run_page.scrape()

    def fetch_confirmed_album_releases(self):
        return self.page_scraper.get_confirmed_album_releases()

    def fetch_anticipated_album_releases(self):
        return self.page_scraper.get_anticipated_album_releases()

    
