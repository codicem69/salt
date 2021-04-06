# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto',pkey='id',name_long='prodotto',name_plural='prodotti',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('cod',name_long='codice')
        tbl.column('descrizione',name_long='descrizione')
        tbl.formulaColumn('tot_carico_prod',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=#THIS.id AND @tipomov_id.cod='c'"),
                                               dtype='N',name_long='Tot.Carico Prod.')
        
        tbl.formulaColumn('tot_scarico_prod',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=#THIS.id AND @tipomov_id.cod='s'"),
                                               dtype='N',name_long='Tot.Scarico Prod.')
        
        tbl.formulaColumn('rimanenza_prod',"coalesce($tot_carico_prod,0) + coalesce($tot_scarico_prod,0)",dtype='N')
