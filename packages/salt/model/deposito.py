#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('deposito', pkey='id', name_long='!![it]Deposito', name_plural='!![it]Deposito', 
                                caption_field='nome', lookup=True)
        self.sysFields(tbl)
        
        tbl.column('codice', size='7', name_long='!![it]Codice', unmodifiable=True, dtype='T')
        tbl.column('nome', size=':50', name_long='!![it]Nome')

    def trigger_onInserting(self, record):
        if len(record['codice'])>7 or not record['codice'].isupper():
            record['codice'] = record['nome'][:7].upper()