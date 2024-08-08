# Scrapy settings for training_scrapy project
#
BOT_NAME = "training_scrapy"

SPIDER_MODULES = ["training_scrapy.spiders"]
NEWSPIDER_MODULE = "training_scrapy.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    # Имя файла для сохранения данных теперь указываем здесь,
    # а не при вызове паука из консоли.
    'quotes_text_%(time)s.csv': {
        # Формат файла.
        'format': 'csv',
        # Поля, данные из которых будут выведены в файл, и их порядок.
        # Выведем в этот файл только два поля из трёх.
        'fields': ['text', 'tags'],
        # Если файл с заданным именем уже существует, то
        # при значении False данные будут дописываться в существующий файл;
        # при значении True существующий файл будет перезаписан.
        'overwrite': True
    },
    # И ещё один файл.
    'quotes_author.csv': {
        'format': 'csv',
        # В этот файл попадёт только список авторов.
        'fields': ['author'],
        'overwrite': True
    },
}
