
from playable.models import Sport
from office.models import Office
from util.models import Country
from user.models import User
from payable.models import PayableProfile
from team.models import Team


country_data = [{'name': 'India'}, {'name': 'Pakistan'}, {'name': 'South Africa'}, {'name': 'Australia'}, {'name': 'England'}, {'name': 'France'}, {'name': 'Germany'}, {'name': 'Portugal'}]
for country in country_data:
    Country.objects.create(name=country['name'])

sport_data = [{'name': 'Cricket'}, {'name': 'Football'}, {'name': 'Basketball'}, {'name': 'Hockey'}]
for sport in sport_data:
    Sport.objects.create(name=sport['name'])

team_data = [{'name': 'India',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="India"),
              'image_url': "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1200px-Flag_of_India.svg.png"},
             {'name': 'Pakistan',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="Pakistan"),
              'image_url': "https://cdn.britannica.com/46/3346-004-D3BDE016/flag-symbolism-Pakistan-design-Islamic.jpg"},
             {'name': 'South Africa',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="South Africa"),
              'image_url': "https://cdn.britannica.com/27/4227-004-32423B42/Flag-South-Africa.jpg"},
             {'name': 'Australia',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="Australia"),
              'image_url': "https://cdn.britannica.com/78/6078-004-77AF7322/Flag-Australia.jpg"},
             {'name': 'England',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="England"),
              'image_url': "https://cdn.britannica.com/44/344-004-494CC2E8/Flag-England.jpg"},
             {'name': 'France',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="France"),
              'image_url': "https://cdn.britannica.com/82/682-004-F0B47FCB/Flag-France.jpg"},
             {'name': 'Germany',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="Germany"),
              'image_url': "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/1200px-Flag_of_Germany.svg.png"},
             {'name': 'Portugal',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="Portugal"),
              'image_url': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/255px-Flag_of_Portugal.svg.png"}
             ]
for team in team_data:
    Team.objects.create(name=team['name'], sport=team['sport'], country=team['country'], image_url=team['image_url'])


office_data = [{'name': 'Dunder Mifflin',
                'address': '1725 Slough Ave. Scranton, PA 18501'},
               {'name': 'Friends', 'address': '90 Bedford Street'}]
for office in office_data:
    Office.objects.create(name=office['name'], address=office['address'])


admin_data = [
    {'display_name': 'Pam',
     'first_name': 'Pam',
     'last_name': 'Beesly',
     'email': 'pam@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin'),
     }
]

for admin in admin_data:
    admin = User.objects.create(
        display_name=admin['display_name'],
        first_name=admin['first_name'],
        last_name=admin['last_name'],
        email=admin['email'],
        office=admin['office'],
        office_admin=True
    )
    PayableProfile.objects.create(user=admin)
    admin.set_password('admin')
    admin.save()

user_data = [
    {'display_name': 'Michael',
     'first_name': 'Michael',
     'last_name': 'Scott',
     'email': 'michael@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Jim',
     'first_name': 'Jim',
     'last_name': 'Halpert',
     'email': 'jim@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Dwight',
     'first_name': 'Dwight',
     'last_name': 'Schrute',
     'email': 'dwight@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Kelly',
     'first_name': 'Kelly',
     'last_name': 'Kapoor',
     'email': 'kelly@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Angela',
     'first_name': 'Angela',
     'last_name': 'Martin',
     'email': 'angela@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Ryan',
     'first_name': 'Ryan',
     'last_name': 'Howard',
     'email': 'ryan@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Stanley',
     'first_name': 'Stanley',
     'last_name': 'Hudson',
     'email': 'stanley@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'Kevin',
     'first_name': 'Kevin',
     'last_name': 'Malone',
     'email': 'kevin@dm.com',
     'office': Office.objects.get(name='Dunder Mifflin')}
]

for user in user_data:
    user = User.objects.create(
        display_name=user['display_name'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        email=user['email'],
        office=user['office']
    )
    PayableProfile.objects.create(user=user)
    user.set_password('admin')
    user.save()
