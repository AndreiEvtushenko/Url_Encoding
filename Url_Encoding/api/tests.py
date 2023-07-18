from http import HTTPStatus

from django.test import Client, TestCase


class UrlEncodingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_encoding_correct_response(self):
        """Проверяет соответствие запроса и ответа"""

        base_root = '/encode_url/'

        data_urls = {
            'https://www.google.ru': HTTPStatus.OK,
            'https://www.facebook.com': HTTPStatus.OK,
            'example.com': HTTPStatus.BAD_REQUEST,
            'www.google.com': HTTPStatus.BAD_REQUEST,
            'http:/google.com': HTTPStatus.BAD_REQUEST,
        }

        for url, expected_status in data_urls.items():
            with self.subTest(url=url):
                response = self.client.get(f'{base_root}?url={url}')
                self.assertEqual(response.status_code, expected_status)
