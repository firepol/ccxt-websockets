# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.liquid import liquid


class qryptos (liquid):

    def describe(self):
        return self.deep_extend(super(qryptos, self).describe(), {
            'id': 'qryptos',
            'name': 'QRYPTOS',
        })