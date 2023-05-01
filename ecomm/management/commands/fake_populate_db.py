from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker
import faker_commerce
import random
from ecomm.models import (
    ProductCategory,
    Product,
    Discount,
    Cart
)


class Command(BaseCommand):
    help = "Populate the database with some fake data with Faker"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process! "))

        # if get_user_model().objects.filter(username='admin').exists():
        #     self.stdout.write(self.style.Success("Database has already been populated. Cancelling the operation..."))
        #     return

        """
            Create Superuser
        """
        if not get_user_model().objects.filter(username='admin').exists():

            admin = get_user_model().objects.create_superuser(
                username='admin',
                # email='admin@mail.com',
                password='admin'
            )
            # admin.first_name = "admin"
            # admin.last_name = "admin"
            # admin.save()

            """
                Create User
            """
            arif = get_user_model().objects.create_user(
                username="ArifBhai",
                email="arifcse21@gmail.com",
                password="very_strong_pass_l0l"
            )
            arif.first_name = "Abdullah"
            arif.last_name = "Arif"
            arif.save()

        fake = Faker()
        fake.add_provider(faker_commerce.Provider)

        """
            Create Product Category
        """
        self.stdout.write(self.style.SUCCESS("Inserting product category started..."))
        titles = [fake.ecommerce_category() for _ in range(10)]     # Generate titles from faker_commerce provider
        descs = [fake.text() for _ in range(10)]            # Generate descriptions from faker

        cats = [ProductCategory(title=x, desc=y) for x, y in zip(titles, descs)]    # titles and descs should be same length for parallel looping
        ProductCategory.objects.bulk_create(cats)       # bulk_create to create multiple objects

        self.stdout.write(self.style.SUCCESS("Inserting product category finished!"))

        """
            Create Discounts
        """
        self.stdout.write(self.style.SUCCESS("Inserting discounts started..."))
        names = [fake.ecommerce_category() for _ in range(10)]  # Generate titles from faker_commerce provider
        descs = [fake.text() for _ in range(10)]  # Generate descriptions from faker

        discounts = [Discount(name=x, desc=y, discount_percent=10) for x, y in zip(names, descs)]
        Discount.objects.bulk_create(discounts)

        self.stdout.write(self.style.SUCCESS("Inserting discounts finished!"))

        """
            Create Products
        """
        self.stdout.write(self.style.SUCCESS("Inserting products started..."))
        titles = [fake.ecommerce_category() for _ in range(10)]  # Generate titles from faker_commerce provider
        descs = [fake.text() for _ in range(10)]  # Generate descriptions from faker

        products = [Product(
            title=x,
            desc=y,
            category=ProductCategory.objects.get(id=random.randint(1, 10)),
            stock=20,
            price=fake.ecommerce_price(),
            currency="BDT",
            discount=Discount.objects.get(id=random.randint(1, 10))
        ) for x, y in
                zip(titles, descs)]  # titles and descs should be same length for parallel looping
        Product.objects.bulk_create(products)  # bulk_create to create multiple objects

        self.stdout.write(self.style.SUCCESS("Inserting products finished!"))

        # """
        #     Create Cart
        # """
        # self.stdout.write(self.style.SUCCESS("Inserting cart started..."))
        # products_pk = [list(set([random.randint(1, 10) for j in range(random.randint(1, 10))])) for i in range(10)]
        #
        # cats = [Product(
        #     product=random.choice(products_pk),       # if the product field is a many-to-many field
        #     desc=y,
        #     category=random.randint(1, 10),
        #     stock=20,
        #     price=fake.ecommerce_price(),
        #     currency="BDT",
        #     discount=random.randint(1, 10)
        # ) for x, y in
        #     zip(titles, descs)]  # titles and descs should be same length for parallel looping
        # ProductCategory.objects.bulk_create(cats)  # bulk_create to create multiple objects
        #
        # self.stdout.write(self.style.SUCCESS("Inserting cart finished!"))
        #

        self.stdout.write(self.style.SUCCESS("Database population process finished! "))
