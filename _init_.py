import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = "https://uniqueapim.azure-api.net/seaapi/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "messages": [
            { "role": "user", "content": "Hello" }
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=body)
    return func.HttpResponse(
        response.text,
        status_code=response.status_code,
        mimetype="application/json"
    )