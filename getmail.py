# This file is part of the account_invoice_helpdesk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['GetmailServer']


class GetmailServer(metaclass=PoolMeta):
    __name__ = 'getmail.server'

    @classmethod
    def __setup__(cls):
        super(GetmailServer, cls).__setup__()
        value = ('invoice', 'Invoice')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)
