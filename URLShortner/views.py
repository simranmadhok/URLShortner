import json
import random

from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView

from URLShortner.models import OriginalURL, URLid


class MiniURLView(APIView):
    def post(self, request):
        input_json=json.loads(request.body)
        url_to_shorten = input_json['url']

        # check if the original url already exists in the database inorder to retrieve its shortned url
        if OriginalURL.objects.filter(original_url = url_to_shorten).exists():
            ref_id_obj = URLid.objects.get(original_url = OriginalURL.objects.get(original_url = url_to_shorten))
            ref_id = int(str(ref_id_obj.url_id))
            url_output = self.encode_func(ref_id)
        else:
            ref_id = random.getrandbits(8)
            ou_obj = OriginalURL.objects.create(original_url = url_to_shorten)
            URLid.objects.create(original_url = ou_obj, url_id = str(ref_id))
            url_output = self.encode_func(ref_id)
            ref_id+=1
        host = 'http://127.0.0.1:8000/'
        url_output = host + 'urlshortner/' + str(url_output)
        return HttpResponse(json.dumps(url_output), content_type="application/json")

    def encode_func(self, ref_id):
        # usage of python oct() to convert 'integer' type to 'octal' value
        return oct(ref_id)

class RedirectURLView(APIView):
    def get(self, request, miniURL):
        ref_id = self.decode_func(miniURL)
        ref_id_obj = URLid.objects.get(url_id=ref_id)
        url_output = str(ref_id_obj.original_url)
        return redirect(url_output)

    def decode_func(self, miniURL):
        # usage of python int() to convert 'octal' value of base 8 to 'integer' value
        return int(miniURL, 8)
