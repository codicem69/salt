# encoding: utf-8

from gnr.app.gnrdbo import TotalizeTable
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method,extract_kwargs

#Tabella di Totalizzazione: definire attributi pkey_columns, totalize_maintable, poi costruire la pkey "codekey"
#In movimento_riga, specificare totalizer_nomeapiacere='mag_light.giacenza_prodotto_deposito'
class Table(TotalizeTable):
    def config_db(self,pkg):
        tbl = pkg.table('giacenza_prodotto_deposito', pkey='codekey', pkey_columns='prodotto_id,deposito_id',
                        name_long='!!Giacenze',
                        caption_field='prodotto_id',
                        totalize_maintable='salt.movim_righe')
        self.sysFields(tbl,id=False, ins=False, upd=False, ldel=False,user_ins=False)

        tbl.column('codekey',size=':45',group='zz',name_long='key')
        tbl.column('prodotto_id', size='22', name_long='Prodotto', group='_', totalize_key=True).relation('salt.prodotto.id',
                                                                mode='foreignkey',
                                                                relation_name='giacenza',
                                                                onDelete='cascade')
        tbl.column('deposito_id', size='22', name_long='Deposito', totalize_key=True).relation('salt.deposito.id',
                                                                mode='foreignkey',
                                                                relation_name='giacenze_prodotti',
                                                                onDelete='cascade')         
        tbl.column('quantita', dtype='I', name_long = 'Quantità disponibile', totalize_value=True)


    def totalize_realign_sql(self,empty=False):
        if empty:
            self.empty()
            self.db.commit()
        if self.countRecords():
            return

        sql = """
            INSERT INTO salt.salt_giacenza_prodotto_deposito (codekey,prodotto_id,deposito_id,quantita,_refcount)
            (SELECT prodotto_id||'_'||deposito_id,
                prodotto_id,
                deposito_id,
                sum(quantita),
                count(*)

            FROM salt.salt_movim_righe
            GROUP BY prodotto_id, deposito_id) ;
        """

        self.db.execute(sql)
        self.db.commit()
