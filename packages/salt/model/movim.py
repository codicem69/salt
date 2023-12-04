# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('movim',pkey='id',name_long='movimentazione',name_plural='movimentazione',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='data_mov')
        tbl.column('descrizione',name_long='descrizione',values='scarico,maggior prodotto,carico')
        tbl.column('totale_movim', dtype='I', name_long='totale movimento')

    def ricalcolaTotali(self,movim_id=None):
            with self.recordToUpdate(movim_id) as record:
                totale_movim = self.db.table('salt.movim_righe'
                                                            ).readColumns(columns="""SUM($quantita) AS totale_movim""",
                                                                                    where='$movim_id=:m_id',m_id=movim_id)
                record['totale_movim'] = totale_movim        
 
                              
                                               
