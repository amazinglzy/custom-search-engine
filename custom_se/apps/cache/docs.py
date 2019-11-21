from elasticsearch_dsl import Document, Text, Date, Keyword


class Page(Document):
    title = Text(fields={'raw': Keyword()})
    content = Text()
    refreshed_at = Date()
