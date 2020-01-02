from typing import List
from elasticsearch_migrate.registry import Document


def query_docs(doc: Document, fields: List[str], query: str = None, page: int=1, page_size: int=10):
    s = doc.search()
    if query:
        s = s.query('multi_match', query=query, fields=fields)
    s = s[(page-1)*page_size: page*page_size]
    res = s.execute()
    return {
        'total': {
            'value': res.hits.total.value,
            'relation': res.hits.total.relation
        },
        'page': page,
        'page_size': page_size,
        'results': res.hits
    }
