import logging
from apscheduler.schedulers.background import BackgroundScheduler
from app.tasks.jobs import execute_scraping

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def start_scheduler():
    try:
        scheduler.add_job(
            execute_scraping,
            trigger = 'cron',
            hour = 6,
            minute = 0,
            id = 'executar_scraping'
        )
        scheduler.start()
    except Exception as e:
        logger.info(f'Falha : {e}')