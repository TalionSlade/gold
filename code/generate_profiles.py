from faker import Faker

fake = Faker()

results = fake.json(
    num_rows=100,
    data_columns=[
        ("first_name", "first_name")
    ]
)

with open("results.json","w") as f:
    f.write(results)