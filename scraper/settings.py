BOT_NAME = 'faculty'

SPIDER_MODULES = ['scraper.spiders']
DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'root',
            'password': '#nourhany#',
            'database': 'scrape'}

ITEM_PIPELINES = {'scraper.pipelines.faculty_pipeline': 300}

CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_ITEMS = 1
DOWNLOAD_DELAY = 1.0
LOG_LEVEL = 'INFO'
