from django.shortcuts import render

from rest_framework import views, response, status


class PerevalApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        return response.Response(data={'message': 'success'}, status=status.HTTP_200_OK)