# dashboard/views.py
import json
import requests
from django.shortcuts import render
from django.http import HttpResponseServerError

API_URL = "https://kisagold-be.onrender.com/api/dashboard/dashboard"

def dashboard_view(request):
    try:
        resp = requests.get(API_URL, timeout=15)
        resp.raise_for_status()
        payload = resp.json()
        dates = payload['dates']           # list tanggal
        data  = payload['data']            # dict platform → { tanggal: {...} }
    except Exception as e:
        return HttpResponseServerError("Gagal fetch data: %s" % e)

    # Dump jadi string JSON agar bisa di‐inject ke JS dengan aman
    context = {
        'dates_json': json.dumps(dates),
        'data_json' : json.dumps(data),
    }
    return render(request, 'dashboard/charts.html', context)
