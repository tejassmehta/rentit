from django.core.exceptions import FieldDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from listings.models import *
import os
import csv
import limehome.settings as settings
from datetime import datetime
class Command(BaseCommand):
    help = 'Prints all book titles in the database'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(settings.BASE_DIR, 'listings', 'management', 'commands','flipkart_com-ecommerce_sample.csv')) as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    print(row)
                    raw_date = datetime.strptime(row[1][:19], "%Y-%m-%d %H:%M:%S")
                    obj, created = Listing_FK.objects.update_or_create(
                    uniq_id = row[0],
                    crawl_timestamp = raw_date,
                    product_url = row[2],
                    product_name = row[3],
                    product_category_tree = row[4],
                    pid = row[5],
                    retail_price = row[6],
                    discounted_price = row[7],
                    image = row[8],
                    is_FK_Advantage_product = row[9],
                    description = row[10],
                    product_rating = row[11],
                    overall_rating = row[12],
                    brand = row[13],
                    product_specifications = row[14],
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
            return

        self.stdout.write(self.style.SUCCESS('Successfully printed all Book titles'))
        return