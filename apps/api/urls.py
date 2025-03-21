from fastapi import APIRouter
from .endpoints import get_ad_metrics

router = APIRouter()

router.get("/ad-metrics/")(get_ad_metrics)