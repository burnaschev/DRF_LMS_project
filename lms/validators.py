from rest_framework.serializers import ValidationError

you_tube = 'https://www.youtube.com'


def validator_scam_url(value):
    if you_tube not in value.lower():
        raise ValidationError('Можно добавлять только ссылки на Youtube')
