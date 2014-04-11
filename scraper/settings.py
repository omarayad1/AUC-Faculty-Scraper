BOT_NAME = 'faculty'

SPIDER_MODULES = ['scraper.spiders']
DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'root',
            'password': '#nourhany#',
            'database': 'scrape'}

ITEM_PIPELINES = ['scraper.pipelines.faculty_pipeline']
