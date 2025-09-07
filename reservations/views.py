import os
import json
import jdatetime
from django.http import JsonResponse


def list_my_reservations(request):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'reservations.json')


    try:
        with open(file_path, 'r') as f:
            my_reservations = json.load(f)
    except FileNotFoundError:
        return JsonResponse({"error": "Reservations file not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=500)


    today = jdatetime.date.today()

    today_jalali_tuple = (today.year, today.month, today.day)


    for reservation in my_reservations:
        year, month, day = map(int, reservation["date"].split("-"))
        date_tuple = (year, month, day)
        if date_tuple == today_jalali_tuple:
            reservation["status"] = 0
        elif date_tuple > today_jalali_tuple:
            reservation["status"] = 1
        else:
            reservation["status"] = -1

    return JsonResponse(my_reservations, safe=False)
