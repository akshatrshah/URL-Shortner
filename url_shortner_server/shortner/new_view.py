"""new_view module defines the NewView view"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
import json

from shortner.models import Link


class NewView(View):
    """NewView is responsible for creation of new shortened links"""

    def post(self, request: HttpRequest):
        """post handles post requests to /new"""
        # httpBody = json.loads(request.body)
        username = request.session['username']
        if username == '':
            redirect('signin')
        long_url = ''
        if 'long-url' in request.POST:
            long_url = request.POST["long-url"]
            custom_stub = None
            if 'custom-stub' in request.POST and request.POST['custom-stub'] != '':
                custom_stub = request.POST["custom-stub"]
        else:
            redirect('homepage', fname=username)
        link = Link(long_url)
        link.username = username
        if custom_stub is not None:
            link.save_custom(custom_stub)
        else:
            link.save()
        return redirect('list')
