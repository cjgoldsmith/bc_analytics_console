from rest_framework.routers import DefaultRouter
from django.conf.urls import url, patterns

import views


router = DefaultRouter()
router.register(
    r'bccredentials', views.BCCredentialViewSet,
    base_name='bccredential')

router.register(
    r'bcaccounts', views.BCAccountViewSet,
    base_name='bcaccount')

router.register(r'users', views.UserViewSet, base_name='user')

urlpatterns = router.urls

urlpatterns += patterns(
    '',
    url('reports/totals/', views.ReportTotals.as_view()))
