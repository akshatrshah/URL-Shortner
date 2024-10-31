from django.http.request import HttpRequest
from django.views.generic import View
from django.shortcuts import redirect, render

from shortner.models import Link


class StatsView(View):
    """NewView is responsible for creation of new shortened links"""

    def get(self, request: HttpRequest):
        """post handles post requests to /new"""
        username = request.session['username']
        # import pdb; pdb.set_trace()
        context = dict()
        if username == '':
            redirect('signin')
        list_of_links = Link.objects.filter(username=username).order_by('-ctr') # pylint: disable=no-member
        context['list_of_links'] = []
        for link_obj in list_of_links:
            x = dict()
            x['long_url'] = link_obj.long_url
            x['short_url'] = request.build_absolute_uri('/') +\
                'stub/' + link_obj.stub
            x['special_code'] = link_obj.special_code
            x['ctr'] = link_obj.ctr
            context['list_of_links'].append(x)
        context['list_of_links'] = sorted(context['list_of_links'],
                                          key=lambda d: d['ctr'], reverse=True)
        return render(request, "homepages/urlstats.html", context=context)
