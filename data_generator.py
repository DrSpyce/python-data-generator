# data_generator.py
import json
import os
from faker import Faker
from resources_generator import generate_patient, generate_practitioner, generate_appointment


def generate_data(resource_type, count, output_dir):
    fake = Faker()

    resource_generators = {
        'Patient': generate_patient,
        'Practitioner': generate_practitioner,
        'Appointment': generate_appointment,
    }

    if resource_type not in resource_generators:
        print(f"Invalid resource type: {resource_type}")
        return

    for i in range(count):
        data = resource_generators[resource_type](fake)
        file_name = f"{resource_type.lower()}_{i + 1}.json"
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)


def main():
    output_dir = "output_data"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Data Generator Menu:")
    print("1. Patient")
    print("2. Practitioner")
    print("3. Appointment")

    resource_type = input("Choose a resource type (1-3): ")
    count = int(input("Enter the number of resources to generate: "))

    generate_data(
        resource_type={
            '1': 'Patient',
            '2': 'Practitioner',
            '3': 'Appointment',
        }[resource_type],
        count=count,
        output_dir=output_dir
    )


if __name__ == "__main__":
    main()
