import pandas as pd

# -------------------------------
# 1. Create Sample Data (No CSV needed)
# -------------------------------
traffic_data = {
    "id": [1, 2, 3, 4],
    "location": ["Signal A", "Signal B", "Signal C", "Signal D"],
    "vehicle_count": [120, 200, 150, 250],
    "avg_speed": [45, 30, 40, 25],
    "time": ["08:00", "09:00", "10:00", "11:00"]
}

environment_data = {
    "id": [1, 2, 3, 4],
    "location": ["Zone A", "Zone B", "Zone C", "Zone D"],
    "temperature": [32, 30, 33, 35],
    "air_quality_index": [120, 90, 140, 160],
    "time": ["08:00", "09:00", "10:00", "11:00"]
}

traffic_df = pd.DataFrame(traffic_data)
env_df = pd.DataFrame(environment_data)

# -------------------------------
# 2. Display Raw Data
# -------------------------------
print("\n--- Traffic Data ---")
print(traffic_df)

print("\n--- Environmental Data ---")
print(env_df)

# -------------------------------
# 3. Traffic Analysis
# -------------------------------
print("\n--- High Traffic Areas ---")
high_traffic = traffic_df.sort_values(by="vehicle_count", ascending=False)
print(high_traffic)

# -------------------------------
# 4. Environmental Analysis
# -------------------------------
print("\n--- Poor Air Quality Areas (AQI > 100) ---")
poor_air = env_df[env_df["air_quality_index"] > 100]
print(poor_air)

# -------------------------------
# 5. Data Warehouse Concept (Merge)
# -------------------------------
warehouse_df = pd.merge(traffic_df, env_df, on="id")

print("\n--- Combined Smart City Data (Warehouse) ---")
print(warehouse_df)

# -------------------------------
# 6. Smart Insights
# -------------------------------
print("\n--- Smart Insights ---")

for index, row in warehouse_df.iterrows():
    if row["vehicle_count"] > 180 and row["air_quality_index"] > 120:
        print(f"⚠️ Critical Area: {row['location_x']} - High Traffic & Poor Air Quality")

    elif row["vehicle_count"] > 180:
        print(f"🚗 Traffic Congestion at {row['location_x']}")

    elif row["air_quality_index"] > 120:
        print(f"🌫 Poor Air Quality at {row['location_y']}")

# -------------------------------
# 7. Summary
# -------------------------------
print("\n--- Summary ---")
print("Total Locations:", len(warehouse_df))
print("Average Traffic:", warehouse_df["vehicle_count"].mean())
print("Average AQI:", warehouse_df["air_quality_index"].mean())=85