from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

# Dimension Tables
class DimDate(Base):
    __tablename__ = "dim_date"
    date_id = Column(Integer, primary_key=True)
    date_value = Column(String, nullable=False)

class DimRegion(Base):
    __tablename__ = "dim_region"
    region_id = Column(Integer, primary_key=True)
    region_name = Column(String, nullable=False)

class DimAgeGroup(Base):
    __tablename__ = "dim_age_group"
    age_id = Column(Integer, primary_key=True)
    age_range = Column(String, nullable=False)

class DimGender(Base):
    __tablename__ = "dim_gender"
    gender_id = Column(Integer, primary_key=True)
    gender_name = Column(String, nullable=False)

class DimPlatform(Base):
    __tablename__ = "dim_platform"
    platform_id = Column(Integer, primary_key=True)
    platform_name = Column(String, nullable=False)

class DimPlacement(Base):
    __tablename__ = "dim_placement"
    placement_id = Column(Integer, primary_key=True)
    placement_name = Column(String, nullable=False)

class DimDeviceType(Base):
    __tablename__ = "dim_device_type"
    device_type_id = Column(Integer, primary_key=True)
    device_type_name = Column(String, nullable=False)

# Fact Table
class FactAdBulletinDaily(Base):
    __tablename__ = "fact_ad_bulletin_daily"
    id = Column(Integer, primary_key=True)
    date_id = Column(Integer, ForeignKey("dim_date.date_id"))
    region_id = Column(Integer, ForeignKey("dim_region.region_id"))
    age_id = Column(Integer, ForeignKey("dim_age_group.age_id"))
    gender_id = Column(Integer, ForeignKey("dim_gender.gender_id"))
    platform_id = Column(Integer, ForeignKey("dim_platform.platform_id"))
    placement_id = Column(Integer, ForeignKey("dim_placement.placement_id"))
    device_type_id = Column(Integer, ForeignKey("dim_device_type.device_type_id"))
    impressions = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    conversions = Column(Integer, nullable=False)
    likes = Column(Integer, nullable=False)