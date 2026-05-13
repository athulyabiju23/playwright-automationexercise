# generates fake user data for signup tests
# using faker so each test run uses a fresh email
# (site rejects duplicate emails)

from faker import Faker
import random
import string

fake = Faker()


def generate_user():
    # returns a dict with all fields needed for signup
    return {
        "name": fake.first_name(),
        "email": _random_email(),
        "password": "Test@1234",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile": fake.phone_number(),
        "company": fake.company(),
        "day": str(random.randint(1, 28)),
        "month": str(random.randint(1, 12)),
        "year": str(random.randint(1980, 2005)),
    }


def _random_email():
    # random string to avoid duplicate email errors
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{rand}@testmail.com"