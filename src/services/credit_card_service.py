from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(card_url):

    credential = AzureKeyCredential(Config.KEY)

    document_client = DocumentIntelligenceClient(
        endpoint=Config.ENDPOINT,
        credential=credential
    )

    poller = document_client.begin_analyze_document(
        "prebuilt-creditCard",
        AnalyzeDocumentRequest(url_source=card_url)
    )

    result = poller.result()

    for document in result.documents:
        fields = document.fields

        return {
            "card_name": fields.get("CardHolderName").value_string if fields.get("CardHolderName") else None,
            "card_number": fields.get("CardNumber").value_string if fields.get("CardNumber") else None,
            "expiration_date": fields.get("ExpirationDate").value_string if fields.get("ExpirationDate") else None,
            "bank_name": fields.get("IssuingBank").value_string if fields.get("IssuingBank") else None,
        }

    return None
