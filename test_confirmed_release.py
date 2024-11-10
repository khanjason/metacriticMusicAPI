from album_release import *
import pytest, json, datetime
from sqlalchemy import null

def test_convert_date():
    release = ConfirmedRelease("ye", "ye", "1 JUNE 2018", "")
    expected_date = '2018-06-01'
    result = release.convert_date()
    assert str(result) == expected_date

def run_all_tests():
    test_convert_date()

run_all_tests()
