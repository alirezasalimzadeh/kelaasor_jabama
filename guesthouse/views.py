import os
import json
import jdatetime
from .holidays import is_holiday, adjust_price
from django.http import JsonResponse


def hotels(request):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'hotels.json')

    try:
        with open(file_path, 'r') as f:
            hotels = json.load(f)
    except FileNotFoundError:
        return JsonResponse({"error": "Transactions file not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=500)


    weekday = jdatetime.date.today().weekday()
    holiday = is_holiday()

    for hotel in hotels:
        hotel["price"] = adjust_price(hotel["price"], weekday,holiday)

    return JsonResponse(hotels, safe=False)


