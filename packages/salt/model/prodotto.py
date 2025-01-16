# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto',pkey='id',name_long='prodotto',name_plural='prodotti',caption_field='descrizione',group_giac_dep='Giacenza Depositi')
        self.sysFields(tbl)
        tbl.column('cod',name_long='codice')
        tbl.column('descrizione',name_long='descrizione')
        tbl.formulaColumn('tot_carico_prod',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=#THIS.id AND @movim_id.@tipomov_cod.verso='c'"),
                                               dtype='N',name_long='Tot.Carico Prod.')
        
        tbl.formulaColumn('tot_scarico_prod',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=#THIS.id AND @movim_id.@tipomov_cod.verso='s'"),
                                               dtype='N',name_long='Tot.Scarico Prod.')
        
        tbl.formulaColumn('rimanenza_prod',"coalesce($tot_carico_prod,0) + coalesce($tot_scarico_prod,0)",dtype='N')
 
        
    def formulaColumn_giac(self):
        depositi = self.db.table('salt.deposito').query().fetch()
        result = []
        for r in depositi:
            result.append(
                dict(name=f'qta_{r["id"]}', select=dict(table='salt.movim_righe',
                 columns='coalesce(SUM($quantita),0)', where='$prodotto_id=#THIS.id AND $deposito_id=:dep',
                 dep=r['id']), dtype='N', name_long=f'Giacenza {r["codice"]}',
                 group='giac_dep'))
        #print(x)
        return result    
        
    #def formulaColumn_giacenze(self):
    #    depositi = self.db.table('salt.deposito').query().fetch()
    #    tbl_totali = self.db.table('salt.giacenza_prodotto_deposito')
    #    result = []
    #    for deposito in depositi:
    #        dep = deposito['codice']
    #        for colname,col in tbl_totali.columns.items():
    #            colattr = col.attributes
    #            if colname.startswith('quantita'):
    #                newcol = dict(name='{colname}_{dep}'.format(colname=colname, dep=dep),
    #                                dtype=colattr['dtype'], 
    #                                select=dict(columns='${colname}'.format(colname=colname),
    #                                        where="($prodotto_id=#THIS.id AND $deposito_id='%s')" % deposito['id'],
    #                                        table='salt.giacenza_prodotto_deposito'),
    #                                name_long='{name_long} {dep}'.format(name_long=colattr['name_long'], dep=dep))
    #                result.append(newcol)
    #    
    #    return result