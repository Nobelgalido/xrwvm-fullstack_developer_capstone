from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        # Nissan models
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 2},
        {"name": "XTRAIL", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 3},
        {"name": "Altima", "type": "Sedan", "year": 2022,
            "car_make": car_make_instances[0], "dealer_id": 4},
        {"name": "Maxima", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 5},
        {"name": "Frontier", "type": "Truck", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 6},
        {"name": "Titan", "type": "Truck", "year": 2022,
            "car_make": car_make_instances[0], "dealer_id": 7},
        {"name": "370Z", "type": "Coupe", "year": 2021,
            "car_make": car_make_instances[0], "dealer_id": 8},

        # Mercedes models
        {"name": "A-Class", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 9},
        {"name": "C-Class", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 10},
        {"name": "E-Class", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 11},
        {"name": "GLA", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 12},
        {"name": "GLE", "type": "SUV", "year": 2022,
            "car_make": car_make_instances[1], "dealer_id": 13},
        {"name": "GLS", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 14},
        {"name": "S-Class", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 15},
        {"name": "AMG GT", "type": "Coupe", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 1},

        # Audi models
        {"name": "A4", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 2},
        {"name": "A5", "type": "Coupe", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "A6", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 4},
        {"name": "Q3", "type": "SUV", "year": 2022,
            "car_make": car_make_instances[2], "dealer_id": 5},
        {"name": "Q5", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 6},
        {"name": "Q7", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 7},
        {"name": "Q8", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 8},
        {"name": "TT", "type": "Coupe", "year": 2022,
            "car_make": car_make_instances[2], "dealer_id": 9},
        {"name": "R8", "type": "Coupe", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 10},

        # Kia models
        {"name": "Sorrento", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 11},
        {"name": "Carnival", "type": "Wagon", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 12},
        {"name": "Cerato", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 13},
        {"name": "Sportage", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 14},
        {"name": "Stinger", "type": "Sedan", "year": 2022,
            "car_make": car_make_instances[3], "dealer_id": 15},
        {"name": "Seltos", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Soul", "type": "Hatchback", "year": 2022,
            "car_make": car_make_instances[3], "dealer_id": 2},
        {"name": "Forte", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 3},

        # Toyota models
        {"name": "Corolla", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 4},
        {"name": "Camry", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 5},
        {"name": "Kluger", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 6},
        {"name": "RAV4", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 7},
        {"name": "Highlander", "type": "SUV", "year": 2022,
            "car_make": car_make_instances[4], "dealer_id": 8},
        {"name": "Prius", "type": "Hatchback", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 9},
        {"name": "Tacoma", "type": "Truck", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 10},
        {"name": "Tundra", "type": "Truck", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 11},
        {"name": "4Runner", "type": "SUV", "year": 2022,
            "car_make": car_make_instances[4], "dealer_id": 12},
        {"name": "Sienna", "type": "Wagon", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 13},
        {"name": "GR86", "type": "Coupe", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 14},
        {"name": "Avalon", "type": "Sedan", "year": 2022,
            "car_make": car_make_instances[4], "dealer_id": 15},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
