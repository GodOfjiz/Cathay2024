import pandas as pd
import random
from datetime import datetime, timedelta

# Generate 100 additional rows starting from 2024-12-01
start_date = datetime(2024, 12, 1)
airports = ['LAX', 'KIX', 'MIA', 'HKG']
departure_airport = airports * 25
arrival_airport = airports[::-1] * 25
aircraft_models = ['CX5250', 'CX3250', 'CX3550', 'CX5550'] * 25
flight_classes = ['First_Class', 'Business_Class', 'Premium_Economy_Class','Economy_Class'] * 25

df = {}
# Generate additional rows
for i in range(100):
    ticket_id = i + 1

    # Incrementing the date by one day for each row
    departure_time = start_date + timedelta(days=i)
    arrival_time = departure_time + timedelta(hours=random.randint(2, 5))  # Random flight duration between 2 to 5 hours
    price = random.randint(200, 1500)  # Random price between 200 and 1500

    # Append the new row to the dataframe
    df[i] = {
        'Ticket_Id': ticket_id,
        'Departure_Airport': departure_airport[i],
        'Arrival_Airport': arrival_airport[i],
        'Aircraft_Model': aircraft_models[i],
        'Departure_Time': departure_time.strftime('%Y-%m-%d %H:%M'),
        'Arrival_Time': arrival_time.strftime('%Y-%m-%d %H:%M'),
        'Flight_Class': flight_classes[i],
        'Price (USD)': price
    }

df = pd.DataFrame.from_dict(df, orient='index')

# Define the function to retrieve flight information
def retrieve_flight_info(departure_airport, arrival_airport, flight_date, flight_class):
    # Convert flight_date to datetime object
    flight_date = datetime.strptime(flight_date, '%Y-%m-%d')

    # Filter the DataFrame
    filtered_flights = df[
        (df['Departure_Airport'] == departure_airport) &
        (df['Arrival_Airport'] == arrival_airport) &
        (pd.to_datetime(df['Departure_Time']).dt.date == flight_date.date()) &
        (df['Flight_Class'] == flight_class)
    ]

    # Select relevant columns
    return filtered_flights

