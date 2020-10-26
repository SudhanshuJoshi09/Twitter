import random
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from .models import Tweet 
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_page(request, *args, **kwargs):
    """ Home Page """

    return render(request, 'pages/home.html', context={})

def tweet_create_view(request, *args, **kwargs):
    """ Create Tweet. """

    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) # 201 --> Item created.
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    
    return render(request, 'components/form.html', context={"form": form})

# Creating List View.
def tweet_list_view(request, *args, **kwargs):
    """
    REST API
    Consume by Javascript/iOS/Android/Swift
    returns JSON data
    """

    qs = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in qs]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)

# Creating Detail View.
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API
    Consume by Javascript/iOS/Android/Swift
    returns JSON data
    """

    data = {
        'id': tweet_id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)