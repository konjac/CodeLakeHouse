from azure.core.credentials import TokenCredential, AccessToken

import datetime
class SynapseTokenCredential(TokenCredential):
    def __init__(self, audience_key: str, linked_service_name: str = None):
        # audience is the resource you want to access in https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/microsoft-spark-utilities?pivots=programming-language-scala#get-token
        self.audience_key = audience_key
        self.linked_service_name = linked_service_name

    def get_token(self, *scopes, **kwargs):
        # don't use `scopes` parameter. use audience_key instead.
        if self.linked_service_name != None:
            token = mssparkutils.credentials.getToken(self.audience_key, self.linked_service_name)
        else:
            token = mssparkutils.credentials.getToken(self.audience_key)
        return AccessToken(token, datetime.datetime.now(datetime.timezone.utc).timestamp()+1800)

# Example usage. If you want to use linked service name, you can pass it as the second parameter. 
credential = SynapseTokenCredential('Storage')

from azure.storage.blob import BlobServiceClient
# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url="https://your_account.blob.core.windows.net", credential=credential)