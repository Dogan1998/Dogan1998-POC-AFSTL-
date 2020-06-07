# tests.py
import requests
from unittest import TestCase
from unittest.mock import patch

def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True

    elif r.status_code == 404:
        return False
        
class FetchTests(TestCase):
    def test_returns_true_if_url_found(self):
        with patch('requests.get') as mock_request:
            url = 'http://localhost:5008/api/1/docs/'

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200

            self.assertTrue(url_exists(url))

    def test_returns_false_if_url_not_found(self):
        with patch('requests.get') as mock_request:
                url = 'http://localhost:5008/api/1/docss/'

                # set a `status_code` attribute on the mock object
                # with value 404
                mock_request.return_value.status_code = 404

                self.assertFalse(url_exists(url))