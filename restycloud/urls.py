from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restycloud import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^credentials/aws/$', views.AWSCredentialList.as_view()),
    url(r'^credentials/aws/(?P<pk>[0-9]+)/$', views.AWSCredentialDetail.as_view()),
    url(r'^credentials/openstack/$', views.OpenstackCredentialList.as_view()),
    url(r'^credentials/openstack/(?P<pk>[0-9]+)/$', views.OpenstackCredentialDetail.as_view()),
    url(r'^credentials/gcloud/$', views.GcloudCredentialList.as_view()),
    url(r'^credentials/gcloud/(?P<pk>[0-9]+)/$', views.GcloudCredentialDetail.as_view()),
    url(r'^credentials/rackspace/$', views.RackspaceCredentialList.as_view()),
    url(r'^credentials/rackspace/(?P<pk>[0-9]+)/$', views.RackspaceCredentialDetail.as_view()),
    url(r'^credentials/dropbox/$', views.DropBoxCredentialList.as_view()),
    url(r'^credentials/dropbox/(?P<pk>[0-9]+)/$', views.DropBoxCredentialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)