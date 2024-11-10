import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from album_release import *

class AlbumReleasesScraper():
    def __init__(self):
        self._page_url = 'https://www.metacritic.com/browse/albums/release-date/coming-soon/date'
        self._upcoming_album_class = 'musicTable'
        self._album_tables = []

    def run_page_scrape(self):
        page = self._request_and_get_parsed_page(self._page_url)
        self._album_tables = self._extract_release_tables(page)

    def get_confirmed_album_releases(self):
        return self._parse_anticipated_releases(self.album_tables[0])

    def get_anticipated_album_releases(self):
        return self._parse_anticipated_releases(self.album_tables[1])    
        
    def _request_and_get_parsed_page(self, url):
        request = Request(url, headers={"User-Agent": "Mozilla/6.0"})
        unparsed_page = urlopen(request).read()
        return BeautifulSoup(unparsed_page, "html.parser")

    def _extract_release_tables(self, parsed_page):
         tables = parsed_page.find_all("table", {"class": self.upcoming_album_class})
         return tables
         

    def _parse_confirmed_releases(self, table):
        rows = table.find_all("tr")
        confirmed_releases = []
        current_date = ''
        for row in rows:
            if row.find('th'):
                current_date = row.getText().strip() #set current date to this
            else:
                artist = row.find("td", {"class": "artistName"}).getText().strip()
                album_name = row.find("td",{"class": "albumTitle"}).getText().strip()
                album_notes = row.find("td",{"class": "dataComment"}).getText().strip()
                albumRelease = ConfirmedRelease(artist, album_name, current_date, album_notes)
                confirmed_releases.append(albumRelease)

        return confirmed_releases

    def _parse_anticipated_releases(self,table):
        anticipated_releases = []
        rows=table.find_all("tr")
        for row in rows:
            artist = row.find("td", {"class": "artistName"}).getText().strip()
            album_name = row.find("td",{"class": "albumTitle"}).getText().strip()
            release_date = row.find("td",{"class": "dataComment"}).getText().strip()
            album = AnticipatedRelease(artist,album_name,release_date)
            anticipated_releases.append(album)
        return anticipated_releases
            


