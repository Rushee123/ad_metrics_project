from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class AdMetricsFilter(BaseModel):
    start_date: Optional[date] = Field(None, description="Start date of the metrics range (YYYY-MM-DD)")
    end_date: Optional[date] = Field(None, description="End date of the metrics range (YYYY-MM-DD)")
    region_id: Optional[int] = Field(None, description="ID of the region to filter by")
    platform_id: Optional[int] = Field(None, description="ID of the platform to filter by")
    age_id: Optional[int] = Field(None, description="ID of the age group to filter by")
    gender_id: Optional[int] = Field(None, description="ID of the gender to filter by")
    placement_id: Optional[int] = Field(None, description="ID of the placement to filter by")
    device_type_id: Optional[int] = Field(None, description="ID of the device type to filter by")
    limit: int = Field(default=100, ge=1, le=1000, description="Maximum number of results to return")
    offset: int = Field(default=0, ge=0, description="Number of results to skip (for pagination)")

    class Config:
        schema_extra = {
            "example": {
                "start_date": "2025-03-01",
                "end_date": "2025-03-05",
                "region_id": 1,
                "platform_id": 2,
                "limit": 5,
                "offset": 0
            }
        }