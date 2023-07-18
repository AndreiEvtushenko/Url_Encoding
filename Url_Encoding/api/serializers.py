from urllib.parse import quote

from django.core.validators import URLValidator

from rest_framework import serializers


class EncodeURLSerializer(serializers.Serializer):
    '''Сериалайзер для проверки корректности URL адреса'''

    url = serializers.CharField(validators=[URLValidator()])

    def validate_url(self, value):
        '''Возвращает закодированный URL адрес'''

        encoded_url = quote(value)
        return encoded_url
