from django.contrib import admin
from django.urls import path
from tweets.views import home_page, tweet_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('view/<int:tweet_id>', tweet_detail_view),
]
