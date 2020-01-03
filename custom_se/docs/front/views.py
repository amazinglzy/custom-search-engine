from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponseBadRequest

# Create your views here.
from utils.query import query_docs
from ..docs import Page
from ..serializer import QueryPageSerializer, PageHighlightSerializer


class QueryPageView(View):

    def get_pagination(self, instance):
        """
        Return:
            [
                {
                    'type': 'previous',
                    'disabled': True,
                },
                {
                    'type': 'middle',
                    'current': True,
                    'page': 1,
                },
                {
                    'type': 'last',
                    'disabled': True,
                }
            ]
        """
        def get_previous_page(current_page):
            page = current_page - 1
            return {
                'type': 'previous',
                'disabled': page <= 0,
                'page': page,
            }

        def get_middle_page(page, current_page):
            return {
                'type': 'middle',
                'active': page == current_page,
                'page': page
            }

        def get_last_page(current_page, total_pages):
            page = current_page + 1
            return {
                'type': 'last',
                'disabled': page > total_pages,
                'page': page
            }

        current_page = instance['page']
        page_size = instance['page_size']
        total_results = instance['results']['total']['value']
        total_pages = total_results // page_size + (0 if total_results % page_size == 0 else 1)
        ret = [get_previous_page(current_page)]

        page_res = 10
        page = max(1, current_page - page_res // 2)
        while page_res > 0 and page <= total_pages:
            ret.append(get_middle_page(page, current_page))
            page += 1
            page_res -= 1
        ret.append(get_last_page(current_page, total_pages))
        return ret

    def get(self, req: HttpRequest):
        data = QueryPageSerializer(data=req.GET)
        if not data.is_valid(False):
            return HttpResponseBadRequest(data.error_messages)
        data = data.save()
        query_results = query_docs(Page,
                                   ['title', 'content'],
                                   ['title', 'content'],
                                   data['query'],
                                   data['page'],
                                   data['page_size'])
        context = {
            'query': data['query'],
            'total': query_results['results']['total'],
            'results': [PageHighlightSerializer(ins).data for ins in query_results['results']['hits']],
            'pagination': self.get_pagination(query_results)
        }
        return render(req, 'index.html', context=context)
