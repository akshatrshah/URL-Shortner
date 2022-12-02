from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect, render
import json

from shortner.models import Link

class ListUrlsView(View):
    """NewView is responsible for creation of new shortened links"""

    def get(self, request: HttpRequest):
        """post handles post requests to /new"""
        username = request.session['username']
        context = dict()
        if username == '':
            redirect('signin')
        list_of_links = Link.objects.filter(username=username)
        context['list_of_links'] = []
        for linkObj in list_of_links:
            x = dict()
            x['long_url'] = linkObj.long_url
            x['stub'] = linkObj.stub
            context['list_of_links'].append(x)

        return render(request, "authentication/index.html", context=context)
