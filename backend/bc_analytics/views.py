from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import BCCredentials, BCAccounts
from .util import make_bc_call, request_url_prefix, get_last_month
from .serializers import BCCredentialSerializer,\
    BCAccountSerializer, UserSerializer


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
    """
    Shows totals for the previous month.
    """

    def get(self, request):

        results = {
            'accounts': {},
            'totals': {},
        }

        total_views = 0
        total_impressions = 0
        start, finish = get_last_month()
        results['accounts'] = {}
        results['totals'] = {}

        for a in BCAccounts.objects.all():
            url = request_url_prefix(a.pub_id)
            url += "report/?dimensions=account&from={0}&to={1}&offset=0&fields=all&sort=engagement_score&format=json".format(start, finish)
            content = make_bc_call(url)
            results['accounts'][a.name] = content['summary']
            results['accounts'][a.name]['name'] = a.name
            total_views += content['summary']['video_view']
            total_impressions += content['summary']['video_impression']

        results['totals']['video_view'] = total_views
        results['totals']['video_impression'] = total_impressions
        results['range'] = (start, finish)

        return JsonResponse(results)
