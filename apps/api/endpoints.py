from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import AdMetricsFilter
from core.database import get_db
from core.models import FactAdBulletinDaily, DimDate
from core.db_utils import db_utils

async def get_ad_metrics(filters: AdMetricsFilter = Depends(), db: Session = Depends(get_db)):
    try:
        query_filters = {}
        
        # Handle date range filtering
        if filters.start_date or filters.end_date:
            date_query = db.query(DimDate.date_id)
            if filters.start_date:
                date_query = date_query.filter(DimDate.date_value >= filters.start_date)
            if filters.end_date:
                date_query = date_query.filter(DimDate.date_value <= filters.end_date)
            date_ids = [d.date_id for d in date_query.all()]
            if not date_ids:
                raise HTTPException(status_code=404, detail="No data found for the given date range")
            query_filters["date_id"] = date_ids  # Pass the list to query_filters

        # Add other filters
        for field in ["region_id", "platform_id", "age_id", "gender_id", "placement_id", "device_type_id"]:
            if getattr(filters, field):
                query_filters[field] = getattr(filters, field)

        # Fetch data using db_utils.fetch_many
        results = db_utils.fetch_many(
            db=db,
            model=FactAdBulletinDaily,
            limit=filters.limit,
            offset=filters.offset,
            **query_filters
        )
        
        if not results:
            raise HTTPException(status_code=404, detail="No metrics found for the given filters")
            
        return [{"id": r.id, "impressions": r.impressions, "clicks": r.clicks, "cost": r.cost,
                "conversions": r.conversions, "likes": r.likes} for r in results]
                
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing request: {str(e)}")