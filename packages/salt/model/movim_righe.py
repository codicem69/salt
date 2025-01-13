# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('movim_righe',pkey='id',name_long='movim_righe',name_plural='movim_righe',caption_field='prodotto_id')
        self.sysFields(tbl)
        tbl.column('movim_id',size='22',name_long='movimentazione').relation('movim.id',relation_name='righemov', mode='foreignkey', onDelete='cascade')
        tbl.column('prodotto_id',size='22',name_long='prodotto',indexed=False).relation('prodotto.id',relation_name='prodmovrig', mode='foreignkey', onDelete='raise')
        tbl.column('tipomov_cod',size=':1',name_long='tipo mov').relation('tipo_mov.cod',relation_name='tipomovrighe', mode='foreignkey', onDelete='raise')
        tbl.column('quantita',dtype='I',name_long='Quantità Kg.',name_short='Qt. Kg.')
        tbl.aliasColumn('data', '@movim_id.data', name_long='data_mov')
        tbl.formulaColumn('somma_carico',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=@prodotto_id.id AND @tipomov_cod.cod='c'"),
                                               dtype='N',name_long='Tot.Carico Prod.')
        tbl.formulaColumn('somma_scarico',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=@prodotto_id.id AND @tipomov_cod.cod='c'"),
                                                  dtype='N',name_long='Tot.Scarico Prod.')                                       
        tbl.formulaColumn('movim_carico',"CASE WHEN (@tipomov_cod.cod='c') THEN ($quantita) ELSE 0 END", 
                                                dtype='N',name_long='Movimentazione Carico')
        tbl.formulaColumn('movim_scarico',"CASE WHEN (@tipomov_cod.cod='s') THEN ($quantita) ELSE 0 END", 
                                                dtype='N', name_long='Movimentazione Scarico')                                         
        tbl.formulaColumn('rimanenza',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where='$prodotto_id=@prodotto_id.id'),# AND $data<=:datatemp',datatemp='2021-03-18'),                                  
                                                  dtype='N',name_long='rimanenza')
        
        #tbl.formulaColumn('rimanenza','$movim_carico+$movim_scarico') 
        #tbl.formulaColumn('somma',"""SELECT SUM( "quantita" ) OVER ( PARTITION BY "cod" ORDER BY "data" ) FROM "salt"."salt_movim_righe" "salt_movim_righe", "salt"."salt_movim" "salt_movim", "salt"."salt_prodotto" "salt_prodotto" WHERE "salt_movim_righe"."movim_id" = "salt_movim"."id" AND "salt_movim_righe"."prodotto_id" = "salt_prodotto"."id" ORDER BY "salt_movim"."data" ASC""",
        #                       dtype='N', name_long="scarico progressivo")                                      
        
    def aggiornaMovim(self,record):
        movim_id = record['movim_id']
        self.db.deferToCommit(self.db.table('salt.movim').ricalcolaTotali,
                                    movim_id=movim_id,
                                    _deferredId=movim_id)

    def trigger_onInserted(self,record=None):
        self.aggiornaMovim(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        self.aggiornaMovim(record)

    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.aggiornaMovim(record)                                

    def trigger_onInserting(self, record):
        self.setDefaultValues(record)
        verso = self.db.table('salt.tipo_mov').readColumns(record['tipomov_cod'], columns='$cod')
        segno = (-1) if verso == 's' else 1 
        record['quantita'] = record['quantita'] * segno


    def setDefaultValues(self, record):
        record['quantita'] = record['quantita'] or 0