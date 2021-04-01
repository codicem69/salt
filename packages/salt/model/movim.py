# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('movim',pkey='id',name_long='movimentazione',name_plural='movimentazione',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='data_mov')
        tbl.column('descrizione',name_long='descrizione')
 
                              
                                               
