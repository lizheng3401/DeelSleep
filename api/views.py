import os
import csv

from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse
from rest_framework.response import Response

from sleep.models import Sleep
from DS.settings import MEDIA_ROOT, BASE_DIR

# Create your views here.

class SleepData(APIView):
    def get_object(self, pk):
        try:
            return Sleep.objects.get(pk=pk)
        except Sleep.DoesNotExist:
            raise Http404

    def str2float(self, line):
        result = []
        for p in line:
            result.append(float(p))
        return result

    def get(self, request, pk, format=None):
        sleepData = self.get_object(pk=pk)
        url = BASE_DIR + os.path.join(MEDIA_ROOT, sleepData.data.url)
        resp = {}
        with open(url, "r") as csvfile:
            reader = csv.reader(csvfile)
            i = 0
            for line in reader:
                if i == 0:
                    key = line
                else:
                    resp[key[i - 1]] = self.str2float(line)
                i += 1
        return JsonResponse(resp, safe=False)
