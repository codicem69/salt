# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('movim_righe',pkey='id',name_long='movim_righe',name_plural='movim_righe',caption_field='prodotto_id')
        self.sysFields(tbl)
        tbl.column('movim_id',size='22',name_long='movimentazione').relation('movim.id',relation_name='righemov', mode='foreignkey', onDelete='cascade')
        tbl.column('prodotto_id',size='22',name_long='prodotto',indexed=False).relation('prodotto.id',relation_name='prodmovrig', mode='foreignkey', onDelete='raise')
        tbl.column('tipomov_id',size='22',name_long='tipo mov').relation('tipo_mov.id',relation_name='tipomovrighe', mode='foreignkey', onDelete='raise')
        tbl.column('quantita',dtype='I',name_long='Quantità Kg.',name_short='Qt. Kg.')
        tbl.aliasColumn('data', '@movim_id.data', name_long='data_mov')
        tbl.formulaColumn('somma_carico',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=@prodotto_id.id AND @tipomov_id.cod='c'"),
                                               dtype='N',name_long='Tot.Carico Prod.')
        tbl.formulaColumn('somma_scarico',select=dict(table='salt.movim_righe',
                                                  columns='SUM($quantita)',
                                                  where="$prodotto_id=@prodotto_id.id AND @tipomov_id.cod='c'"),
                                                  dtype='N',name_long='Tot.Scarico Prod.')                                       
        tbl.formulaColumn('movim_carico',"CASE WHEN (@tipomov_id.cod='c') THEN ($quantita) ELSE 0 END", 
                                                dtype='N',name_long='Movimentazione Carico')
        tbl.formulaColumn('movim_scarico',"CASE WHEN (@tipomov_id.cod='s') THEN ($quantita) ELSE 0 END", 
                                                dtype='N', name_long='Movimentazione Scarico')                                         
        #tbl.formulaColumn('somma',select=dict(table='salt.movim_righe',
        #                                          columns='SUM($quantita)',
        #                                          where="$prodotto_id=@prodotto_id.id AND @tipomov_id.cod='c'"),
        #                                       dtype='N',name_long='Tot.Carico Prod.')
        #tbl.formulaColumn('rimanenza','$movim_carico+$movim_scarico') 
        #tbl.formulaColumn('somma',"""SELECT SUM( "quantita" ) OVER ( PARTITION BY "cod" ORDER BY "data" ) FROM "salt"."salt_movim_righe" "salt_movim_righe", "salt"."salt_movim" "salt_movim", "salt"."salt_prodotto" "salt_prodotto" WHERE "salt_movim_righe"."movim_id" = "salt_movim"."id" AND "salt_movim_righe"."prodotto_id" = "salt_prodotto"."id" ORDER BY "salt_movim"."data" ASC""",
        #                       dtype='N', name_long="scarico progressivo")                                      
        