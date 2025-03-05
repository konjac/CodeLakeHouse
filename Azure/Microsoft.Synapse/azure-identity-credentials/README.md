# Alternative for `DefaultAzureCredential`/`ManagedIdentityCredential`

`DefaultAzureCredential`/`ManagedIdentityCredential` provides the ability to acquire token in Azure environments. However, Azure Synapse Analytics is not supported them as it does not initialize required environment context.

In Synapse, a customized implementation of `azure.core.credentials.TokenCredential` can be used as the alternative to make use of [mssparkutils.credentials](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/microsoft-spark-utilities?pivots=programming-language-scala#credentials-utilities). Check [SynapseTokenCredential.py](Azure\Microsoft.Synapse\azure-identity-credentials\SynapseTokenCredential.py) for a sample.

But this is not 100% identical as `mssparkutils.credentials` only supports limited audiences.

Microsoft Fabric Spark is similar but uses [notebookutils.credentials](https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-utilities#credentials-utilities) instead.
