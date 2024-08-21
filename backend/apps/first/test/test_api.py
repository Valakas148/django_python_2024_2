from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.first.models import CarModel

UserModel = get_user_model()
class CarApiTest(APITestCase):
    def setUp(self):
        self.car1 = CarModel.objects.create(
            brand="BMW",
            model="X5",
            price=14000,
            year=2016,
            body_type="SUV"
        )
        self.car2 = CarModel.objects.create(
            brand="Audi",
            model="Q7",
            price=2600,
            year=2014,
            body_type="SUV"
        )

    def _authenticate(self):
        email = 'admin@gmail.com'
        password = '12a@34AF567'
        self.client.post(reverse('user_list_create'), {
            'email': email,
            'password': password,
            'profile': {
                'name': 'Petr',
                'surname': 'Yablonsky',
                'age': 27
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        token = self.client.post(reverse('auth_login'), {
            'email': email,
            'password': password
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.data["access"]}')


    def test_get_all_cars(self):
        res = self.client.get(reverse('car_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(len(data), 2)
        car1 = CarModel.objects.get(pk=self.car1.pk)
        self.assertEqual(car1.brand, "BMW")
        car2 = CarModel.objects.get(pk=self.car2.pk)
        self.assertEqual(car2.brand, "Audi")
        self.assertEqual(CarModel.objects.count(), 2)

    def test_create_car_without_auth(self):
        sample_car = {
            "brand": "Ford",
            "model": "Fusion",
            "price": 8000,
            "year": 2013,
            "body_type": "Sedan"
        }
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('car_list_create'), sample_car)
        count_after = CarModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(count_before, count_after)

    def test_create_car_with_auth(self):
        self._authenticate()
        sample_car = {
            "brand": "Ford",
            "model": "Fusion",
            "price": 8000,
            "year": 2013,
            "body_type": "Sedan"
        }
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('car_list_create'), sample_car)
        count_after = CarModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after, count_before+1)
