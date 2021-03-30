# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('movim_righe',pkey='id',name_long='movim_righe',name_plural='movim_righe',caption_field='prodotto_id')
        self.sysFields(tbl)
        tbl.column('movim_id',size='22',name_long='movimentazione').relation('movim.id',relation_name='righemov', mode='foreignkey', onDelete='cascade')
        tbl.column('prodotto_id',size='22',name_long='prodotto').relation('prodotto.id',relation_name='prodmovrig', mode='foreignkey', onDelete='raise')
        tbl.column('tipomov_id',size='22',name_long='tipo mov').relation('tipo_mov.id',relation_name='tipomovrighe', mode='foreignkey', onDelete='raise')
        tbl.column('quantita',dtype='I',name_long='Quantità Kg.',name_short='Qt. Kg.')
