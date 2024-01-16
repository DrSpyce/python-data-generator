def generate_patient(fake):
    return {
        "resourceType": "Patient",
        "id": fake.uuid4(),
        "name": {"given": fake.first_name(), "family": fake.last_name()},
        "gender": fake.random_element(["male", "female", "other"]),
        "birthDate": fake.date_of_birth().strftime('%Y-%m-%d'),
        "address": {"street": fake.street_address(), "city": fake.city(), "state": fake.state(), "zip": fake.zipcode()}
    }


def generate_practitioner(fake):
    return {
        "resourceType": "Practitioner",
        "id": fake.uuid4(),
        "name": {"given": fake.first_name(), "family": fake.last_name()},
        "address": {"street": fake.street_address(), "city": fake.city(), "state": fake.state(), "zip": fake.zipcode()},
        "qualification": {"code": fake.random_element(["MD", "DO", "NP"]), "system": fake.url()}
    }


def generate_appointment(fake):
    return {
        "resourceType": "Appointment",
        "id": fake.uuid4(),
        "status": fake.random_element(["booked", "confirmed", "done"]),
        "class": fake.random_element(["ambulatory", "acute"]),
        "description": fake.sentence(),
        "start": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "end": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "created": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
    }
