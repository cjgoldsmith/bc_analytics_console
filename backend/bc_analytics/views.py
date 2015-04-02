from models import BCCredentials, BCAccounts
from .util import make_bc_call,request_url_prefix
from serializers import BCCredentialSerializer, BCAccountSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from django.views.generic import View
from django.contrib.auth.models import User
from django.utils.six import BytesIO

from sanction import Client

class BCCredentialViewSet(viewsets.ModelViewSet):
    queryset = BCCredentials.objects.all()
    serializer_class = BCCredentialSerializer

class BCAccountViewSet(viewsets.ModelViewSet):
    queryset = BCAccounts.objects.all()
    serializer_class = BCAccountSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReportTotals(View):

    def get(self, request):

        for a in BCAccounts.objects.all():
            url = request_url_prefix(a.pub_id)
            url += '?'
        content = "{}"
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        return JsonResponse(data)



