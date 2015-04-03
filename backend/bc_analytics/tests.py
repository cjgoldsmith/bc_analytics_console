import json, sanction
from mock import patch, MagicMock

from django.test import TestCase
from django.test import Client

from .models import BCCredentials
from .util import request_url_prefix
from .util import get_last_month
from .util import make_bc_call

import random


class UtilTestCase(TestCase):
    def setUp(self):
        random.seed()

    def test_request_url_prefix(self):
        account_id = random.randrange(0, 10000)
        up = request_url_prefix(account_id)
        self.assertRegexpMatches(up, repr(account_id))

    def test_get_last_month(self):
        first, last = get_last_month()

    @patch('bc_analytics.util.Client')
    def test_make_bc_call(self, client_c):
        client = MagicMock()
        client.request_token = MagicMock()
        client.request = MagicMock(returns="")
        client_c.return_value = client

        BCCredentials.objects.get_or_create(
            name="TEST",
            client_id="TEST_CLIENT_ID",
            client_secret="TEST_CLIENT_SECRET")

        make_bc_call('/analytics-api/reports/')
        client.request.assert_called_once_with('/analytics-api/reports/')


class ReportAllTestCase(TestCase):

    def testTotals(self):
        c = Client()
        response = c.get('/reports/totals/')
        self.assertEqual(response.status_code, 200)

        # results should always be in json format
        content = json.loads(response.content)
        self.assertEqual(content['totals']['video_view'], 0)
        self.assertEqual(content['totals']['video_impression'], 0)

        first, last = get_last_month()
        self.assertEqual(content['range'][0], first)
        self.assertEqual(content['range'][1], last)