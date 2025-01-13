# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tipo_mov',pkey='cod',name_long='tipo_mov',name_plural='tipo_mov',caption_field='tipomov',lookup=True)
        self.sysFields(tbl, id=False)
        tbl.column('cod',size=':1',name_long='codice')
        tbl.column('tipomov',name_long='tipo movimentazione')

    @metadata(mandatory=True)
    def sysRecord_Carico(self):
        return self.newrecord(cod='c',tipomov='carico')

    @metadata(mandatory=True)
    def sysRecord_Scarico(self):
        return self.newrecord(cod='s',tipomov='scarico')