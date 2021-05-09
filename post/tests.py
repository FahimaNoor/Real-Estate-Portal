import unittest
from django.test import TestCase
from post.models import ApartmentModel, PostModel
from django.contrib.auth.models import User


class ApartmentModelTest(TestCase):

    def setUp(self):
        ApartmentModel.objects.create(location='dhaka', apartment_type='duplex', description='3 rooms', utilities='kitchen', money='2500')
        ApartmentModel.objects.create(location='khulna', apartment_type='sss', description='', utilities='zzzz', money=0)

    def test_location(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertEqual(apartment1.location, 'dhaka')
        self.assertEqual(apartment2.location, 'khulna')

    def test_apartment_type(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertEqual(apartment1.apartment_type, 'duplex')
        self.assertEqual(apartment2.apartment_type, 'sss')

    def test_description(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertEqual(apartment1.description, '3 rooms')
        self.assertEqual(apartment2.description, '')

    def test_utilities(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertEqual(apartment1.utilities, 'kitchen')
        self.assertEqual(apartment2.utilities, 'zzzz')

    def test_picture(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertFalse(apartment1.picture)
        self.assertFalse(apartment2.picture)

    def test_money(self):
        apartment1 = ApartmentModel.objects.get(apartment_id=1)
        apartment2 = ApartmentModel.objects.get(apartment_id=2)
        self.assertEqual(apartment1.money, 2500)
        self.assertEqual(apartment2.money, 0)


class PostModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='qqq', password='1234', email='ppp@qqq.com')
        apartment = ApartmentModel.objects.create(location='kkk', apartment_type='sss', description='p', utilities='zz', money=5)
        PostModel.objects.create(post_header='dxfgc', apartment_id=apartment, email=user, phone=456, is_sell_post='Rent')

    def test_post_header(self):
        post_1 = PostModel.objects.get(post_id=1)
        self.assertEqual(post_1.post_header, 'dxfgc')

    def test_is_sell_post(self):
        post_1 = PostModel.objects.get(post_id=1)
        self.assertEqual(post_1.is_sell_post, 'Rent')
        self.assertNotEqual(post_1.is_sell_post, 'Sell')
