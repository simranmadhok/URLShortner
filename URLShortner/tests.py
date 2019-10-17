import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.test import APIRequestFactory, APITestCase

from URLShortner.models import OriginalURL, URLid
from URLShortner.views import MiniURLView, RedirectURLView


class MiniURLTestCase(APITestCase):
    """
        Test case for creation of Mini URL with original url as the input
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = 'http://127.0.0.1:8000/urlshortner/mini/'
        self.valid_data = {
            'url': 'https://www.instagram.com/'
        }
        self.view = MiniURLView.as_view()

    def test_shorten_url(self):
        request = self.factory.post(
                redirect(self.uri),
                data=json.dumps(self.valid_data),
                content_type='application/json'
        )
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

class RedirectURLTestCase(APITestCase):
    """
        Test case for redirection to the original url on invocation of shortend url
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = 'http://127.0.0.1:8000/urlshortner/0o303'
        self.original_url = 'https://www.instagram.com/'
        self.original_url_obj = OriginalURL.objects.create(original_url='https://www.instagram.com/')
        self.url_id_obj = URLid.objects.create(original_url = self.original_url_obj, url_id = 195)
        self.view = RedirectURLView.as_view()

    def test_url_redirection(self):
        request = self.factory.get(self.uri)
        response = self.view(request, miniURL='0o303')
        self.assertRedirects(response, self.original_url, status_code=302, target_status_code=200, fetch_redirect_response=False)
