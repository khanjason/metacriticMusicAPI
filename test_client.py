from sqlalchemy import null
from client import *
import pytest, json, datetime

@pytest.mark.first
def test_initialise():
    client = AlbumReleasesClient()
    pytest.client = client
    assert pytest.client != null

def test_fetch_anticipated_albums():
    result = pytest.client.fetch_anticipated_album_releases()
    assert len(result) != 0 

def test_fetch_confirmed_albums():
    result = pytest.client.fetch_confirmed_album_releases()
    assert len(result) != 0 

def run_all_tests():
    test_initialise()
    test_fetch_anticipated_albums()
    test_fetch_confirmed_albums()

run_all_tests()
