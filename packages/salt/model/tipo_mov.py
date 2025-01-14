# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tipo_mov',pkey='cod',name_long='tipo_mov',name_plural='tipo_mov',caption_field='tipomov',lookup=True)
        self.sysFields(tbl, id=False)
        tbl.column('cod',size=':3',name_long='codice')
        tbl.column('tipomov',name_long='tipo movimentazione')
        tbl.column('verso',name_long='verso')

    @metadata(mandatory=True)
    def sysRecord_CaricoGen(self):
        return self.newrecord(cod='CAR',tipomov='Carico generico', verso='c')

    @metadata(mandatory=True)
    def sysRecord_ScaricoGen(self):
        return self.newrecord(cod='SCA',tipomov='Scarico generico', verso='s')
    
    @metadata(mandatory=True)
    def sysRecord_Ammanco(self):
        return self.newrecord(cod='AMM',tipomov='Ammanco', verso='s')
    
    @metadata(mandatory=True)
    def sysRecord_MaggiorProd(self):
        return self.newrecord(cod='MAG',tipomov='Maggior prodotto', verso='c')
    
    @metadata(mandatory=True)
    def sysRecord_Trasferimento_out(self):
        return self.newrecord(cod='TRU',tipomov='Trasferimento uscita', verso='s')
    
    @metadata(mandatory=True)
    def sysRecord_Trasferimento_in(self):
        return self.newrecord(cod='TRE',tipomov='Trasferimento entrata', verso='c')
    
    @metadata(mandatory=True)
    def sysRecord_Giroconto_out(self):
        return self.newrecord(cod='GIU',tipomov='Giroconto uscita', verso='s')
    
    @metadata(mandatory=True)
    def sysRecord_Giroconto_in(self):
        return self.newrecord(cod='GIE',tipomov='Giroconto entrata', verso='c')
    
    
