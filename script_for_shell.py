import csv
from django.contrib.auth.models import User

file_path = 'data/usuario_migrar.csv'

with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter='|')
    next(reader)
    for row in reader:
        user_name = row[0]
        user_correo = row[3]
        user_clave = row[0] + str('Password')
        last_name = row[2]
        first_name = row[1]

        user = User.objects.create_user(username=user_name, email=user_correo, password=user_clave)
        user.is_active = True
        user.is_staff = False
        user.last_name = last_name
        user.first_name = first_name
        user.save()
