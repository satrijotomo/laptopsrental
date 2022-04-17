from django.test import TestCase
from django.urls import reverse
from laptops.models import Laptop
import pytest


def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
@pytest.fixture
def new_laptop(db):
    laptop = Laptop.objects.create(
        laptopmodel='GoodLaptop',
        serialno='ZXY1234XX',
        image_path='/f/laptop',
        description='Tutorial on how to apply pytest to a Django application',
        owner=True
    )
    return laptop

def test_search_laptops(new_laptop):
    assert Laptop.objects.filter(title='GoodLaptop').exists()