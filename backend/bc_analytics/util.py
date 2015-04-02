from .models import BCCredentials
from sanction import Client

def request_url_prefix(account):
    '''
    Builds prefix to brightcove api calls
    :param account: numeric account id
    :return: url string
    '''
    return '/analytics-api/videocloud/accounts/{1}/report/'.format(account)

def make_bc_call(request_url):
    '''
    Uses stored credentials to try and make Brightcove API calls
    :param request_url:
    :return:
    '''
    token_request_url = "https://oauth.brightcove.com/v3/access_token"
    resource_base = "https://data.brightcove.com/"

    for credential in BCCredentials.objects.all():
        try:
            client = Client(
                token_endpoint=token_request_url,
                resource_endpoint = resource_base,
                client_id = credential.client_id,
                client_secret = credential.client_secret, )
            client.request_token(grant_type='client_credentials')
            continue
        except Exception:
            pass

    client.request(request_url)
