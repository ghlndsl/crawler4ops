# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tbcrawler'

SPIDER_MODULES = ['tbcrawler.spiders']
NEWSPIDER_MODULE = 'tbcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
ITEM_PIPELINES = [
    'tbcrawler.pipelines.TiebaPipeline',
]
