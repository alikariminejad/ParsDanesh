from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.core.cache import cache
from django.conf import settings

CACHE_TTL = getattr(settings, "CACHE_TTL", 10000)


class HealthCheckView(APIView):
    def get(self, request, format=None):
        try:
            user_counts = User.objects.count()
            cache_key = "User_counts"
            counts = user_counts
            cache.set(cache_key, counts, CACHE_TTL)
            new_counts = cache.get("User_counts")
            return Response({"users": new_counts, "status": "ok", "database": "connected", "redis": "connected"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)