from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restycloud.models import Snippet
from restycloud.models import * 
from restycloud.serializers import SnippetSerializer
from restycloud.serializers import AWSCredentialsSerializer
from restycloud.serializers import GcloudCredentialsSerializer
from restycloud.serializers import DropBoxCredentialsSerializer
from restycloud.serializers import OpenstackCredentialsSerializer
from restycloud.serializers import RackspaceCredentialsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = SnippetSerializer


    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = SnippetSerializer
    
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
    serializer_class = SnippetSerializer


    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AWSCredentialList(APIView):
    """
    List all credentials, or create a new credentials.
    """
    serializer_class = AWSCredentialsSerializer

    def get(self, request, format=None):
        creds = AWSCredentials.objects.all()
        serializer = AWSCredentialsSerializer(creds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AWSCredentialsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AWSCredentialDetail(APIView):
    """
    Retrieve, update or delete a AWSCredential instance.
    """
    serializer_class = AWSCredentialsSerializer

    def get_object(self, pk):
        try:
            return AWSCredentials.objects.get(pk=pk)
        except AWSCredentials.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = AWSCredentialsSerializer(cred)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = AWSCredentialsSerializer(cred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cred = self.get_object(pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GcloudCredentialList(APIView):
    """
    List all credentials, or create a new Gcloud credentials.
    """
    serializer_class = GcloudCredentialsSerializer

    def get(self, request, format=None):
        creds = GcloudCredentials.objects.all()
        serializer = GcloudCredentialsSerializer(creds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GcloudCredentialsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GcloudCredentialDetail(APIView):
    """
    Retrieve, update or delete a Gcloud Credential instance.
    """
    serializer_class = GcloudCredentialsSerializer

    def get_object(self, pk):
        try:
            return GcloudCredentials.objects.get(pk=pk)
        except GcloudCredentials.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = GcloudCredentialsSerializer(cred)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = GcloudCredentialsSerializer(cred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cred = self.get_object(pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class OpenstackCredentialList(APIView):
    """
    List all credentials, or create a new Gcloud credentials.
    """
    serializer_class = OpenstackCredentialsSerializer
    
    def get(self, request, format=None):
        creds = OpenstackCredentials.objects.all()
        serializer = OpenstackCredentialsSerializer(creds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OpenstackCredentialsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpenstackCredentialDetail(APIView):
    """
    Retrieve, update or delete a Gcloud Credential instance.
    """
    serializer_class = OpenstackCredentialsSerializer
    
    def get_object(self, pk):
        try:
            return OpenstackCredentials.objects.get(pk=pk)
        except OpenstackCredentials.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = OpenstackCredentialsSerializer(cred)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = OpenstackCredentialsSerializer(cred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cred = self.get_object(pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RackspaceCredentialList(APIView):
    """
    List all credentials, or create a new Rackspace credentials.
    """
    serializer_class = RackspaceCredentialsSerializer
    
    def get(self, request, format=None):
        creds = RackspaceCredentials.objects.all()
        serializer = RackspaceCredentialsSerializer(creds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RackspaceCredentialsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RackspaceCredentialDetail(APIView):
    """
    Retrieve, update or delete a Gcloud Credential instance.
    """
    serializer_class = RackspaceCredentialsSerializer
    
    def get_object(self, pk):
        try:
            return RackspaceCredentials.objects.get(pk=pk)
        except RackspaceCredentials.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = RackspaceCredentialsSerializer(cred)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = RackspaceCredentialsSerializer(cred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cred = self.get_object(pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DropBoxCredentialList(APIView):
    """
    List all credentials, or create a new DropBox credentials.
    """
    serializer_class = DropBoxCredentialsSerializer
    
    def get(self, request, format=None):
        creds = DropBoxCredentials.objects.all()
        serializer = DropBoxCredentialsSerializer(creds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DropBoxCredentialsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DropBoxCredentialDetail(APIView):
    """
    Retrieve, update or delete a DropBox Credential instance.
    """
    serializer_class = DropBoxCredentialsSerializer
    
    def get_object(self, pk):
        try:
            return DropBoxCredentials.objects.get(psk=pk)
        except DropBoxCredentials.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = DropBoxCredentialsSerializer(cred)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cred = self.get_object(pk)
        serializer = DropBoxCredentialsSerializer(cred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cred = self.get_object(pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)