import os
import csv

from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse

from sleep.models import Sleep


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
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        url = BASE_DIR + str(sleepData.data.url).replace("/","\\")
        resp = {}
        with open(url, "r") as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                resp.setdefault("time", []).append(float(line[0]))
                resp.setdefault("heart", []).append(float(line[1]))
                resp.setdefault("breath", []).append(float(line[2]))

        return JsonResponse(resp, safe=False)
