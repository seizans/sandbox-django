# coding=utf8

from django.core.urlresolvers import resolve


class JsonSchemaValidateMiddleware(object):

    def process_request(self, request):
        print request.path_info
        resolver_match = resolve(request.path_info)
        print resolver_match.url_name
        print resolver_match.func
        print resolver_match.view_name
        print resolver_match.namespace
        print resolver_match.namespaces

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_response(self, request, response):
        return response
