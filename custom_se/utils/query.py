from typing import List
from elasticsearch_migrate.registry import Document


def query_docs(doc: Document, fields: List[str],
               highlight_fields: List[str] = None,
               query: str = None,
               page: int = 1,
               page_size: int = 10):
    s = doc.search()
    if query:
        s = s.query('multi_match', query=query, fields=fields)
    if highlight_fields:
        s = s.highlight_options(order='score').highlight(*highlight_fields)
    s = s[(page-1)*page_size: page*page_size]
    res = s.execute().to_dict()
    return {
        'results': res.pop('hits'),
        'page': page,
        'page_size': page_size
    }
