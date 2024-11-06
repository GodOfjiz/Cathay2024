import pandas as pd
import random
from datetime import datetime, timedelta


# Generate 100 additional rows starting from 2024-12-01
start_date = datetime(2024, 12, 1)
airports = ['JFK', 'LAX', 'ORD', 'DFW', 'MIA', 'BOS']
aircraft_models = ['Boeing 777', 'Airbus A320', 'Boeing 737', 'Boeing 787', 'Airbus A321', 'Boeing 757']
flight_classes = ['First_Class', 'Business_Class', 'Economy_Class']

df = {}
# Generate additional rows
for i in range(100):
    ticket_id = i + 1
    departure_airport = random.choice(airports)
    arrival_airport = random.choice([airport for airport in airports if airport != departure_airport])
    aircraft_model = random.choice(aircraft_models)

    # Incrementing the date by one day for each row
    departure_time = start_date + timedelta(days=i)
    arrival_time = departure_time + timedelta(hours=random.randint(2, 5))  # Random flight duration between 2 to 5 hours

    flight_class = random.choice(flight_classes)
    price = random.randint(200, 1500)  # Random price between 200 and 1500

    # Append the new row to the dataframe
    df[i] = {
        'Ticket_Id': ticket_id,
        'Departure_Airport': departure_airport,
        'Arrival_Airport': arrival_airport,
        'Aircraft_Model': aircraft_model,
        'Departure_Time': departure_time.strftime('%Y-%m-%d %H:%M'),
        'Arrival_Time': arrival_time.strftime('%Y-%m-%d %H:%M'),
        'Flight_Class': flight_class,
        'Price (USD)': price
    }

df = pd.DataFrame(df)
# Display the updated DataFrame
print(df[0])