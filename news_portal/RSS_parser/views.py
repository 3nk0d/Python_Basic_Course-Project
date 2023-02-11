from django.shortcuts import render

# Create your views here.


def rss_jobs(request):
    render(request, 'rss_jobs')
