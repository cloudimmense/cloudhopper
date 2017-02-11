from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

class AWSCredentials(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cred_name = models.CharField(max_length=100, blank=True)
    access_id = models.CharField(max_length=100, blank=False)
    secret_key = models.CharField(max_length=100, blank=False)
    assoc_acc = models.CharField(max_length=100, blank=False)
    meta = models.TextField()

    class Meta:
        ordering = ('created',)


class GcloudCredentials(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cred_name = models.CharField(max_length=100, blank=True)
    account_type = models.CharField(max_length=100, blank=False)
    project_id = models.CharField(max_length=100, blank=False)
    private_key_id = models.CharField(max_length=100, blank=False)
    private_key = models.TextField()
    client_email = models.CharField(max_length=100, blank=False)
    client_id = models.CharField(max_length=100, blank=False)
    auth_uri = models.CharField(max_length=100, blank=False)
    token_uri = models.CharField(max_length=100, blank=False)
    auth_provider_x509_cert_url = models.CharField(max_length=100, blank=False)
    client_x509_cert_url = models.CharField(max_length=100, blank=False)
    json_meta = models.TextField()
    json_file_path = models.CharField(max_length=100, blank=True)
    meta = models.TextField()

    class Meta:
        ordering = ('created',)


class OpenstackCredentials(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cred_name = models.CharField(max_length=100, blank=True)
    auth_url = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    project = models.CharField(max_length=100, blank=False)
    clouds_yaml = models.TextField()
    assoc_acc = models.CharField(max_length=100, blank=False)
    meta = models.TextField()

    class Meta:
        ordering = ('created',)


class RackspaceCredentials(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cred_name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    api_key = models.CharField(max_length=100, blank=False)
    secret_key = models.CharField(max_length=100, blank=False)
    assoc_acc = models.CharField(max_length=100, blank=False)
    meta = models.TextField()
    
    class Meta:
        ordering = ('created',)


class DropBoxCredentials(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cred_name = models.CharField(max_length=100, blank=True)
    access_token = models.CharField(max_length=100, blank=False)
    assoc_acc = models.CharField(max_length=100, blank=False)
    meta = models.TextField()

    class Meta:
        ordering = ('created',)