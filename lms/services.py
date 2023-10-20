import requests

from config.settings import STRIPE_TEST_SECRET_KEY, STRIPE_API


def create_payment_intent(amount, currency='USD'):
    headers = {'Authorization': f'Bearer {STRIPE_TEST_SECRET_KEY}'}
    params = {'amount': amount, 'currency': currency}
    response = requests.post(STRIPE_API, headers=headers, params=params)
    data = response.json()
    return data['id']


def retrieve_payment_intent(payment_id):
    headers = {'Authorization': f'Bearer {STRIPE_TEST_SECRET_KEY}'}
    response = requests.get(f'{STRIPE_API}/{payment_id}', headers=headers)

    return response.json()
