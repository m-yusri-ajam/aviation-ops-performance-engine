import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_aviation_data(records=250):
    tails = [f'A6-XW{chr(i)}' for i in range(ord('A'), ord('F'))]
    vendors = ['Etihad Ground Logistics', 'dnata', 'Swissport']
    delay_reasons = {
        '11': 'Ground Handling',
        '18': 'Catering',
        '41': 'Aircraft Handling',
        '66': 'Late Crew',
        'None': 'On-Time'
    }

    # Mapping Etihad routes for the A350-1000
    route_map = {
        'EY11': {'Orig': 'AUH', 'Dest': 'LHR', 'Dist': 5480},
        'EY101': {'Orig': 'AUH', 'Dest': 'JFK', 'Dist': 11000},
        'EY151': {'Orig': 'AUH', 'Dest': 'ORD', 'Dist': 11500},
        'EY204': {'Orig': 'AUH', 'Dest': 'BOM', 'Dist': 1970},
        'EY37': {'Orig': 'AUH', 'Dest': 'CDG', 'Dist': 5250}
    }
    
    data = []
    start_date = datetime(2026, 3, 1)

    for i in range(records):
        flight_no = random.choice(list(route_map.keys()))
        route = route_map[flight_no]
        tail = random.choice(tails)
        vendor = random.choice(vendors)

        # Scheduling logic (Standard 90-minute Turnaround)
        scheduled_arrival = start_date + timedelta(hours=i*6)
        scheduled_departure = scheduled_arrival + timedelta(minutes=90)

        # Injecting "Turbulence" (Delays)
        delay_minutes = 0
        delay_code = 'None'
        if random.random() > 0.78:
            delay_minutes = random.randint(15, 65)
            delay_code = random.choice(['11', '18', '41', '66'])

        actual_departure = scheduled_departure + timedelta(minutes=delay_minutes)

        # Fuel logic (A350 average uplift for mid-range is ~40,000kg)
        planned_fuel = random.uniform(38000, 42000)

        # Fuel variance in AED
        fuel_variance_kg = random.uniform(-100, 300) if delay_minutes > 0 else random.uniform(-20, 20)
        actual_fuel = planned_fuel + fuel_variance_kg

        data.append({
            'Flight_No': flight_no,
            'Route': f"{route['Orig']}-{route['Dest']}",
            'Tail_Number': tail,
            'Vendor': vendor,
            'Sch_Arrival': scheduled_arrival,
            'Sch_Departure': scheduled_departure,
            'Act_Departure': actual_departure,
            'Delay_Min': delay_minutes,
            'IATA_Code': delay_code,
            'Reason': delay_reasons[delay_code],
            'Planned_Fuel_KG': round(planned_fuel, 2),
            'Actual_Fuel_KG': round(actual_fuel, 2),
            'Fuel_Variance_AED': round(fuel_variance_kg * 4.6, 2) # AED 4.6 per KG
        })
    
    df = pd.DataFrame(data)
    df.to_csv('data/a350_ops_logs.csv', index=False)

    print(f"✈️ Generated {records} A350 operational records in data/a350_ops_logs.csv")

if __name__ == "__main__":
    generate_aviation_data(250)