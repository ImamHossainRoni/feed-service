from faker import Faker


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_fake_facilities(self, n=100):
        """Generate fake facility data"""
        facilities = []
        for _ in range(n):
            facilities.append([
                self.fake.company(),
                self.fake.phone_number()[:12],
                self.fake.url(),
                float(self.fake.latitude()),
                float(self.fake.longitude()),
                self.fake.country(),
                self.fake.city(),
                self.fake.state_abbr(),
                self.fake.postcode(),
                self.fake.street_address()
            ])
        return facilities
