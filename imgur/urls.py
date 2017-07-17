from django.conf.urls import url,include


urlpatterns = [
    url(r'^', include('imgur.accounts.urls', namespace='accounts')),
]
