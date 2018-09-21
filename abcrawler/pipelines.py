# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
import sys
from abcrawler.models import QuoteItem,db_connect,create_quotes_table

class AbcrawlerPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_quotes_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        quote = QuoteItem(**item)

        # if isinstance(item, items.QuoteItem):
        #     quote=QuoteItem(**item)

        try:
            session.add(quote)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
