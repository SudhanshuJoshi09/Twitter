from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Tweet 

# Create your views here.
def home_page(request, *args, **kwargs):
    """ Home Page """

    return HttpResponse('<h1>Hello, World! </h1>')

# Creating Detail View.
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """ Shows Detailed View of the Tweet. """

    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        print('Check once the tweet seem\'s to have gone missing')
        raise Http404

    return HttpResponse(f'hello, {tweet_id} - {obj.content}')