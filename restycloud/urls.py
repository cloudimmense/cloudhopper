from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restycloud import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^credentials/aws/$', views.AWSCredentialList.as_view()),
    url(r'^credentials/aws/(?P<pk>[0-9]+)/$', views.AWSCredentialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)