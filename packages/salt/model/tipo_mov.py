# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tipo_mov',pkey='id',name_long='tipo_mov',name_plural='tipo_mov',caption_field='tipomov',lookup=True)
        self.sysFields(tbl)
        tbl.column('cod',name_long='codice')
        tbl.column('tipomov',name_long='tipo movimentazione')
