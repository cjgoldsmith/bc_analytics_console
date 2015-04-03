import datetime

from .models import BCCredentials

from sanction import Client


def request_url_prefix(account):
    """
    Builds prefix to brightcove api calls
    :param account: numeric account id
    :return: url string
    """
    return '/analytics-api/videocloud/accounts/{0}/'.format(account)


def make_bc_call(request_url):
    """
    Uses stored credentials to try and make Brightcove API calls
    :param request_url:
    :return:
    """
    token_request_url = "https://oauth.brightcove.com/v3/access_token"
    resource_base = "https://data.brightcove.com/"

    for credential in BCCredentials.objects.all():
        content = None
        try:
            client = Client(
                token_endpoint=token_request_url,
                resource_endpoint=resource_base,
                client_id=credential.client_id,
                client_secret=credential.client_secret, )
            client.request_token(grant_type='client_credentials')
            content = client.request(request_url)
            break
        except Exception as e:
            pass

        return content


def get_last_month():
    """
    Retrieves string representation for last month's
    start and end dates.
    :return:
    """
    today = datetime.date.today()
    first = datetime.date(day=1, month=today.month, year=today.year)
    last_month = first - datetime.timedelta(days=1)
    return (
        last_month.strftime('%Y-%m-') + '01',
        last_month.strftime('%Y-%m-%d'))
