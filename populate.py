import os
os.environ.setdefault('DJANGO_SETTINS_MODULE', 'SocialNetwork.settings')
import django
django.setup()
from faker import Faker
import random

fakegen = Faker()

