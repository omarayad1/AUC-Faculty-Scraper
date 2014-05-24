BOT_NAME = 'faculty'

SPIDER_MODULES = ['scraper.spiders']
DATABASE = {'drivername': 'postgres',
            'host': 'ec2-54-243-50-213.compute-1.amazonaws.com',
            'port': '5432',
            'username': 'eiactalswujtqs',
            'password': '47eSaSTSZKWrOgh_DeK6nFtzEH',
            'database': 'd8ohn4nft64tao'}

ITEM_PIPELINES = {'scraper.pipelines.faculty_pipeline': 300}

CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_ITEMS = 1
DOWNLOAD_DELAY = 1.0
LOG_LEVEL = 'INFO'
