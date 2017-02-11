from rest_framework import serializers
from restycloud.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from restycloud.models import AWSCredentials


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class AWSCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSCredentials
        fields = ('id', 'cred_name', 'access_id', 'secret_key', 'assoc_acc', 'meta')