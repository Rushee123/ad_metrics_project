from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from core.models import (
    DimDate, DimRegion, DimAgeGroup, DimGender, 
    DimPlatform, DimPlacement, DimDeviceType, FactAdBulletinDaily
)
from datetime import datetime, timedelta
import random

# Create tables if not already created
Base.metadata.create_all(bind=engine)

def insert_test_data():
    db = SessionLocal()
    try:
        # Insert 100 dates (March 1, 2025 to June 9, 2025)
        start_date = datetime(2025, 3, 1)
        dates = [DimDate(date_id=i+1, date_value=(start_date + timedelta(days=i)).strftime("%Y-%m-%d")) 
                 for i in range(100)]
        db.add_all(dates)

        # Insert sample dimension data
        regions = [
            DimRegion(region_id=1, region_name="North"),
            DimRegion(region_id=2, region_name="South"),
            DimRegion(region_id=3, region_name="East")
        ]
        age_groups = [
            DimAgeGroup(age_id=1, age_range="18-24"),
            DimAgeGroup(age_id=2, age_range="25-34"),
            DimAgeGroup(age_id=3, age_range="35-44")
        ]
        genders = [
            DimGender(gender_id=1, gender_name="Male"),
            DimGender(gender_id=2, gender_name="Female")
        ]
        platforms = [
            DimPlatform(platform_id=1, platform_name="Google Ads"),
            DimPlatform(platform_id=2, platform_name="Facebook Ads"),
            DimPlatform(platform_id=3, platform_name="Twitter Ads")
        ]
        placements = [
            DimPlacement(placement_id=1, placement_name="Banner"),
            DimPlacement(placement_id=2, placement_name="Sidebar"),
            DimPlacement(placement_id=3, placement_name="In-feed")
        ]
        device_types = [
            DimDeviceType(device_type_id=1, device_type_name="Mobile"),
            DimDeviceType(device_type_id=2, device_type_name="Desktop"),
            DimDeviceType(device_type_id=3, device_type_name="Tablet")
        ]

        db.add_all(regions + age_groups + genders + platforms + placements + device_types)

        # Commit dimension data first to ensure foreign keys are available
        db.commit()

        # Insert 100 fact rows with random metrics
        fact_data = []
        for i in range(1, 101):  # 1 to 100
            fact_data.append(FactAdBulletinDaily(
                date_id=i,  # Links to dim_date
                region_id=random.randint(1, 3),
                age_id=random.randint(1, 3),
                gender_id=random.randint(1, 2),
                platform_id=random.randint(1, 3),
                placement_id=random.randint(1, 3),
                device_type_id=random.randint(1, 3),
                impressions=random.randint(500, 5000),  # Random impressions between 500 and 5000
                clicks=random.randint(10, 200),         # Random clicks between 10 and 200
                cost=round(random.uniform(5.0, 100.0), 2),  # Random cost between 5 and 100
                conversions=random.randint(1, 50),      # Random conversions between 1 and 50
                likes=random.randint(10, 300)           # Random likes between 10 and 300
            ))
        db.add_all(fact_data)

        # Final commit
        db.commit()
        print("Successfully inserted 100 rows of test data")

    except Exception as e:
        db.rollback()
        print(f"Error inserting data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    insert_test_data()