import elasticsearch
from rest_framework import viewsets, request, response, exceptions
from utils.query import query_docs
from ..docs import Page
from ..serializer import PageSerializer


class PageViewSets(viewsets.ViewSet):

    serializer_class = PageSerializer
    model_class = Page

    def get_object(self, pk):
        try:
            return self.model_class.get(id=pk)
        except elasticsearch.exceptions.NotFoundError:
            raise exceptions.NotFound('Document with ID(%(pk)s) not found' % {'pk': pk})

    def list(self, req: request.Request):
        query = req.query_params.get('query', None)
        page = req.query_params.get('page', 1)
        page_size = req.query_params.get('page_size', 10)
        ret = query_docs(Page, ['title', 'content'], query, page, page_size)
        results = ret.pop('results')
        ret['results'] = [
            self.serializer_class(ins).data for ins in results
        ]
        return response.Response(ret)

    def create(self, req: request.Request):
        serializer = self.serializer_class(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, req: request.Request, pk=None):
        serializer = self.serializer_class(self.get_object(pk))
        return response.Response(serializer.data)

    def update(self, req: request.Request, pk=None):
        ins = self.get_object(pk)
        serializer = self.serializer_class(self.get_object(pk))
        serializer.update(ins, req.data)
        return response.Response(serializer.data)

    def partial_update(self, req: request.Request, pk=None):
        ins = self.get_object(pk)
        serializer = self.serializer_class(self.get_object(pk))
        serializer.update(ins, req.data, partial=True)
        return response.Response(serializer.data)

    def destroy(self, req: request.Request, pk=None):
        ins = self.get_object(pk)
        ins.delete()
        return response.Response()

