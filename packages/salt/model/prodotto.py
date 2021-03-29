# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto',pkey='id',name_long='prodotto',name_plural='prodotti',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('cod',name_long='codice')
        tbl.column('descrizione',name_long='descrizione')