
from faker import Faker
fake = Faker("pl_PL")
for _ in range(5):
    name = fake.name()
    job = fake.job()
    mail =fake.email()
    adr = fake.address()
    wizytowka=[name,job,mail,adr]
    print(wizytowka)
"""
    print(fake.name())
    print(fake.job())
    print(fake.email())
    print(fake.address())
    print("------")
"""
