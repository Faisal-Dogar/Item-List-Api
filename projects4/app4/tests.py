from django.test import TestCase

# python manage.py shell

# Import the Item model and create some sample items
from app4.models import Item

Item.objects.create(name='Item 1', description='Description of Item 1')
Item.objects.create(name='Item 2', description='Description of Item 2')
Item.objects.create(name='Item 3', description='Description of Item 3')

