"""new_view module defines the NewView view"""

from django.http import HttpRequest, HttpResponseBadRequest
from django.views.generic import View
from django.shortcuts import redirect
from shortner.models import Link


class NewView(View):
    """NewView is responsible for the creation of new shortened links"""

    def post(self, request: HttpRequest):
        """post handles post requests to /new"""
        username = request.session.get('username')
        if not username:
            return redirect('signin')

        if 'long-url' not in request.POST:
            return redirect('homepage', fname=username)

        long_urls = request.POST['long-url'].split(',')
        custom_stubs = request.POST.get('custom-stub', '').split(',')  # Get custom stubs and split by comma

        # Ensure custom_stubs is trimmed to match the long_urls length
        custom_stubs = [stub.strip() for stub in custom_stubs]
        custom_stubs = custom_stubs[:len(long_urls)]  # Trim the list to match long URLs

        for index, long_url in enumerate(long_urls):
            long_url = long_url.strip()
            if not long_url:
                continue

            link = Link(long_url=long_url, username=username)

            # Use custom_stub only for the corresponding URL
            if index < len(custom_stubs) and custom_stubs[index]:
                custom_stub = custom_stubs[index]
                # Check if the custom stub already exists
                if Link.objects.filter(stub=custom_stub).exists():
                    return HttpResponseBadRequest(f"Custom stub '{custom_stub}' is already in use.")
                link.save_custom(custom_stub)
            else:
                link.save()
import csv
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse
from django.views.generic import View
from django.shortcuts import redirect
from shortner.models import Link


class NewView(View):
    """NewView is responsible for the creation of new shortened links"""

    def post(self, request: HttpRequest):
        """post handles post requests to /new"""
        username = request.session.get('username')
        if not username:
            return redirect('signin')

        if 'long-url' in request.POST:  # Handle manual URL submissions
            long_urls = request.POST['long-url'].split(',')
            custom_stubs = request.POST.get('custom-stub', '').split(',')

            # Ensure custom_stubs is trimmed to match the long_urls length
            custom_stubs = [stub.strip() for stub in custom_stubs]
            custom_stubs = custom_stubs[:len(long_urls)]  # Trim the list to match long URLs

            for index, long_url in enumerate(long_urls):
                long_url = long_url.strip()
                if not long_url:
                    continue

                link = Link(long_url=long_url, username=username)

                # Use custom_stub only for the corresponding URL
                if index < len(custom_stubs) and custom_stubs[index]:
                    custom_stub = custom_stubs[index]
                    # Check if the custom stub already exists
                    if Link.objects.filter(stub=custom_stub).exists():
                        return HttpResponseBadRequest(f"Custom stub '{custom_stub}' is already in use.")
                    link.save_custom(custom_stub)
                else:
                    link.save()

        elif request.FILES.get('file'):  # Handle CSV file uploads
            uploaded_file = request.FILES['file']
            if uploaded_file.name.endswith('.csv'):
                # Process the CSV file
                try:
                    csv_reader = csv.DictReader(uploaded_file.read().decode('utf-8').splitlines())
                    existing_stubs = set(Link.objects.values_list('stub', flat=True))

                    for row in csv_reader:
                        long_url = row.get('link', '').strip()
                        custom_stub = row.get('stub', '').strip()

                        if long_url:  # Proceed if there's a long URL
                            link = Link(long_url=long_url, username=username)

                            if custom_stub:
                                if custom_stub in existing_stubs:
                                    return HttpResponseBadRequest(f"Custom stub '{custom_stub}' is already in use.")
                                existing_stubs.add(custom_stub)
                                link.save_custom(custom_stub)
                            else:
                                link.save()

                except Exception as e:
                    return HttpResponseBadRequest(f"Error processing file: {str(e)}")
            else:
                return HttpResponseBadRequest("Uploaded file is not a CSV.")

        return redirect('list')
