import email
import os
import pandas as pd
from pepper.settings import BASE_DIR
from utils.models import City, Country
from restaurant.models import Cuisine, Restaurant
from users.models import User, Role

csv_file_path = os.path.join(os.path.dirname(BASE_DIR), "databuilder/python-scripts/file1.csv")

df_master = pd.read_csv(csv_file_path)

country_india = Country(name="India")
country_india.save()

df_city = df_master[["city", "city_id"]].drop_duplicates()

for i, item in df_city.iterrows():
    city = City(name=item["city"], city_id=item["city_id"], country=country_india)
    city.save()


cuisine_combined_list = []
for i in list(df_master["cuisines"]):
    cuisine_combined_list += i.split(', ')
cuisine_list = list(set(cuisine_combined_list))

for c in cuisine_list:
    cuisine = Cuisine(name=c)
    cuisine.save()

for i, row in df_master.iterrows():
    online_delivery = True if row["has_online_delivery"] == 1 else False
    city_instance = City.objects.filter(name=row["city"]).first()
    restaurant = Restaurant(name=row["name"], zomato_id=row["id"], address=row["address"], latitude=row["latitude"],
                            longitude=row["longitude"], image_url=row["featured_image"], do_online_delivery=online_delivery, city=city_instance)
    restaurant.save()
    for c in row["cuisines"].split(', '):
        restaurant_cusines = Cuisine.objects.filter(name=c).first()
        restaurant.cuisines.add(restaurant_cusines)

for i in range(4):
    role = Role(id=i)
    role.save()


user = User(first_name='demo', last_name='manager', email='manager@pd.com')
user.set_password('admin')
user.save()
user.roles.add(Role.objects.filter(id=0).first())

user = User(first_name='demo', last_name='sales', email='sales@pd.com')
user.set_password('admin')
user.save()
user.roles.add(Role.objects.filter(id=1).first())

user = User(first_name='demo', last_name='inventory', email='inventory@pd.com')
user.set_password('admin')
user.save()
user.roles.add(Role.objects.filter(id=2).first())

user = User(first_name='demo', last_name='customer', email='customer@pd.com')
user.set_password('admin')
user.save()
user.roles.add(Role.objects.filter(id=3).first())
