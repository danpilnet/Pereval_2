from rest_framework import views, response, status

from .serializers import PerevalSerialzer


class PerevalApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer_data = PerevalSerialzer(request.data).data
        return response.Response(data={'message': f'{serializer_data}'}, status=status.HTTP_200_OK)