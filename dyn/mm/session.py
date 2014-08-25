# -*- coding: utf-8 -*-
"""This module implements an interface to a DynECT REST Session. It provides
easy access to all other functionality within the dynect library via
methods that return various types of DynECT objects which will provide their
own respective functionality.
"""
import locale
# API Libs
from ..core import SessionEngine
from ..compat import urlencode, pathname2url, json, prepare_for_loads
from .errors import *

__author__ = 'jnappi'


class MMSession(SessionEngine):
    """Base object representing a Message Management API Session"""
    __metakey__ = 'a577c742-6dce-49ae-9b1f-dce6477fa646'
    _valid_methods = ('GET', 'POST')
    uri_root = '/rest/json'

    def __init__(self, apikey, host='emailapi.dynect.net', port=443, ssl=True):
        """Initialize a Dynect Rest Session object and store the provided
        credentials

        :param host: DynECT API server address
        :param port: Port to connect to DynECT API server
        :param ssl: Enable SSL
        :param apikey: your unique Email API key
        """
        super(MMSession, self).__init__(host, port, ssl)
        self.apikey = apikey
        self.content_type = 'application/x-www-form-urlencoded'
        self._conn = None
        self._encoding = locale.getdefaultlocale()[-1] or 'UTF-8'
        self.connect()

    def _prepare_arguments(self, args, method, uri):
        """Prepare MM arguments which need to be packaged differently depending
        on the specified HTTP method
        """
        args, content, uri = super(MMSession, self)._prepare_arguments(args,
                                                                       method,
                                                                       uri)
        if 'apikey' not in args:
            args['apikey'] = self.apikey

        if method == 'GET':
            if '%' not in uri:
                uri = pathname2url(uri)
            uri = '?'.join([uri, urlencode(args)])
            return {}, '', uri
        return args, urlencode(args), uri

    def _handle_response(self, response, uri, method, raw_args, final):
        """Handle the processing of the API's response"""
        body = response.read()
        ret_val = json.loads(prepare_for_loads(body, self._encoding))
        return self._process_response(ret_val['response'], method, final)

    def _process_response(self, response, method, final=False):
        """Process an API response for failure, incomplete, or success and
        throw any appropriate errors

        :param response: the JSON response from the request being processed
        """
        status = response['status']
        reason = response['message']
        self.logger.debug(status)
        if status == 200:
            return response['data']
        elif status == 451:
            raise EmailKeyError(reason)
        elif status == 452:
            raise EmailInvalidArgumentError(reason)
        elif status == 453:
            raise EmailObjectError(reason)
