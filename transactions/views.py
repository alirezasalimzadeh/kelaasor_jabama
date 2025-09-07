import os
import json
from django.http import JsonResponse

def list_transactions(request):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'transactions.json')

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return JsonResponse({"error": "Transactions file not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=500)


    return JsonResponse(data, safe=False)
