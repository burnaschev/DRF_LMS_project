from django.core.exceptions import ValidationError


def validator_scam_url(value):
    yt_base_url = 'https://www.youtube.com'
    if yt_base_url not in value.lower():
        raise ValidationError('Можно добавлять только ссылки на Youtube')
