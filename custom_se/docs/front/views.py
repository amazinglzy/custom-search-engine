from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponseBadRequest

# Create your views here.
from utils.query import query_docs
from ..docs import Page
from ..serializer import PageSerializer, QueryPageSerializer


class QueryPageView(View):

    def get(self, req: HttpRequest):
        data = QueryPageSerializer(data=req.GET)
        if not data.is_valid(False):
            return HttpResponseBadRequest(data.error_messages)
        data = data.save()
        query_results = query_docs(Page, ['title', 'content'], data['query'], data['page'], data['page_size'])
        results = query_results.pop('results')
        query_results['results'] = [PageSerializer(ins).data for ins in results]
        return render(req, 'index.html', context=query_results)
