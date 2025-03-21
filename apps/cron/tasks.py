from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
from datetime import datetime

logging.basicConfig(filename='cron.log', level=logging.INFO)
scheduler = AsyncIOScheduler()

async def log_timestamp():
    logging.info(f"Cron job ran successfully at {datetime.now()}")

def setup_cron_jobs():
    scheduler.add_job(log_timestamp, 'interval', hours=6)
    scheduler.start()
