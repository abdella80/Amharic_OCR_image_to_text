from django.shortcuts import redirect, render

# Create your views here.
import requests
from django.shortcuts import render


API_URL = "http://127.0.0.1:8000/ocr"

def home(request):

    extracted_text = ""

    if request.method == "POST":

        image = request.FILES['image']

        files = {
            'file': image
        }

        response = requests.post(
            API_URL,
            files=files
        )

        data = response.json()

        extracted_text = data.get(
            "extracted_text",
            ""
        )

    return render(
        request,
        'index.html',
        {
            'text': extracted_text
        }
    )

