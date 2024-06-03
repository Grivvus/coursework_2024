import random
import hashlib

from mimesis import Person, Generic
from mimesis.locales import Locale

p = Person(Locale.RU)
g = Generic(Locale.RU)
alpha = "q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * . ,".split()
with open("users.sql", "w+") as file:
    for i in range(5):
        full_name = p.full_name().split()
        email = p.email()
        random.shuffle(alpha)
        pswd = "".join(alpha[:9])
        pswd_enc = pswd.encode("utf-8")
        md5 = hashlib.md5(pswd_enc)
        password = md5.hexdigest()
        phone = str(g.person.phone_number("##########"))
        address = str(
            g.address.street_name()) + " " + str(g.address.street_number()
        )
        file.write('insert into public."user" ("first_name", "second_name", "phone_number", \
"email", "password")\n')
        file.write(f"values ('{full_name[0]}', '{full_name[1]}', {phone}, \
'{email}', '{password}');\n")
        file.write(f"-- pswd '{pswd}'\n")
