from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EncodeURLSerializer


class EncodeURLView(APIView):
    '''
    Представление принимает запрос,
    вызывает необходимый сериализатор,
    возвращает закодированный URL в формате JSON:

    {
        "encoded_url": "https%3A//www.google.ru"
    }

    '''

    def get(self, request):
        serializer = EncodeURLSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        encoded_url = serializer.validated_data['url']

        data = {
            'encoded_url': encoded_url,
        }

        return Response(data)
