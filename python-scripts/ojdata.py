
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
              'country': Country.objects.get(name="India")},
             {'name': 'Pakistan',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="Pakistan")},
             {'name': 'South Africa',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="South Africa")},
             {'name': 'Australia',
              'sport': Sport.objects.get(name="Cricket"),
              'country': Country.objects.get(name="Australia")},
             {'name': 'England',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="England")},
             {'name': 'France',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="France")},
             {'name': 'Germany',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="Germany")},
             {'name': 'Portugal',
              'sport': Sport.objects.get(name="Football"),
              'country': Country.objects.get(name="Portugal")}
             ]
for team in team_data:
    Team.objects.create(name=team['name'], sport=team['sport'], country=team['country'])


office_data = [{'name': 'Dunder Mifflin',
                'address': '1725 Slough Ave. Scranton, PA 18501'},
               {'name': 'Friends', 'address': '90 Bedford Street'}]
for office in office_data:
    Office.objects.create(name=office['name'], address=office['address'])


admin_data = [
    {'display_name': 'a1',
     'first_name': 'a1',
     'last_name': 'a1',
     'email': 'a1@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin'),
     },
    {'display_name': 'a2',
     'first_name': 'a2',
     'last_name': 'a2',
     'email': 'a2@gmail.com',
     'office': Office.objects.get(name='Friends'),
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
    {'display_name': 'u1',
     'first_name': 'u1',
     'last_name': 'u1',
     'email': 'u1@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u2',
     'first_name': 'u2',
     'last_name': 'u2',
     'email': 'u2@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u3',
     'first_name': 'u3',
     'last_name': 'u3',
     'email': 'u3@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u4',
     'first_name': 'u4',
     'last_name': 'u4',
     'email': 'u4@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u5',
     'first_name': 'u5',
     'last_name': 'u5',
     'email': 'u5@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u6',
     'first_name': 'u6',
     'last_name': 'u6',
     'email': 'u6@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'u7',
     'first_name': 'u7',
     'last_name': 'u7',
     'email': 'u7@gmail.com',
     'office': Office.objects.get(name='Dunder Mifflin')},
    {'display_name': 'x1',
     'first_name': 'x1',
     'last_name': 'x1',
     'email': 'x1@gmail.com',
     'office': Office.objects.get(name='Friends')},
    {'display_name': 'x2',
     'first_name': 'x2',
     'last_name': 'x2',
     'email': 'x2@gmail.com',
     'office': Office.objects.get(name='Friends')},
    {'display_name': 'x3',
     'first_name': 'x3',
     'last_name': 'x3',
     'email': 'x3@gmail.com',
     'office': Office.objects.get(name='Friends')},
    {'display_name': 'x4',
     'first_name': 'x4',
     'last_name': 'x4',
     'email': 'x4@gmail.com',
     'office': Office.objects.get(name='Friends')},
    {'display_name': 'x5',
     'first_name': 'x5',
     'last_name': 'x5',
     'email': 'x5@gmail.com',
     'office': Office.objects.get(name='Friends')},
    {'display_name': 'x6',
     'first_name': 'x6',
     'last_name': 'x6',
     'email': 'x6@gmail.com',
     'office': Office.objects.get(name='Friends')},
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
