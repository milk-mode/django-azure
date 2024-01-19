import os
from django.core.wsgi import get_wsgi_application
from faker import Faker


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azureproject.settings")
application = get_wsgi_application()

from azureapp.models import Person
fake=Faker()

def populate_data():

    for _ in range(10):
        Person.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            
        )
        
if __name__ == "__main__":
    populate_data()