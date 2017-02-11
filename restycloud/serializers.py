from rest_framework import serializers
from restycloud.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from restycloud.models import AWSCredentials, GcloudCredentials, OpenstackCredentials, RackspaceCredentials, DropBoxCredentials


class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class AWSCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AWSCredentials
        fields = ('id', 'cred_name', 'access_id', 'secret_key', 'assoc_acc', 'meta')


class GcloudCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GcloudCredentials
        fields = ('id', 'cred_name', 'account_type', 'project_id',\
                  'private_key_id', 'private_key', 'client_email',\
                  'client_id', 'auth_uri', 'token_uri',\
                  'auth_provider_x509_cert_url',\
                  'client_x509_cert_url', 'json_meta',\
                  'json_file_path', 'meta')


class OpenstackCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OpenstackCredentials
        fields = ('id', 'cred_name', 'auth_url', 'username', 'password',\
                  'project', 'clouds_yaml', 'assoc_acc', 'meta')


class RackspaceCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RackspaceCredentials
        fields = ('id', 'cred_name', 'username', 'api_key', 'assoc_acc', 'meta')


class DropBoxCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DropBoxCredentials
        fields = ('id', 'cred_name', 'access_token', 'assoc_acc', 'meta')