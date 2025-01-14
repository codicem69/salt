# encoding: utf-8
from gnr.core.gnrdecorator import metadata,public_method
from gnr.core.gnrlang import GnrException

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('movim',pkey='id',name_long='movimentazione',name_plural='movimentazione',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='data_mov')
        tbl.column('tipomov_cod',size=':3',name_long='tipo mov', batch_assign=True).relation('tipo_mov.cod',relation_name='mov_tip', mode='foreignkey', onDelete='raise')
        tbl.column('verso', size='1', name_long='Verso movimento')
        tbl.column('descrizione',name_long='descrizione')#,values='scarico,ammanco,maggior prodotto,carico')
        tbl.column('totale_movim', dtype='I', name_long='totale movimento')
        tbl.column('movimento_id', size='22', group='_', name_long='!![it]Trasferimento').relation(
                        'movim.id', one_one='*', mode='foreignkey', onDelete='cascade')
        
    def ricalcolaTotali(self,movim_id=None):
            with self.recordToUpdate(movim_id) as record:
                totale_movim = self.db.table('salt.movim_righe'
                                                            ).readColumns(columns="""SUM($quantita) AS totale_movim""",
                                                                                    where='$movim_id=:m_id',m_id=movim_id)
                record['totale_movim'] = totale_movim        
    
    def trigger_onInserting(self, record):
        self.setDefaultValues(record)

    def setDefaultValues(self, record):
        record['verso'] = self.db.table('salt.tipo_mov').readColumns(
                                record['tipomov_cod'], columns='$verso')

    @public_method
    def creaTrasferimento(self, data=None,movimento_id=None, deposito_id=None,prodotto_id=None, **kwargs):
        if kwargs['tipomov']=='TRU':
            movimento_rec = self.record(movimento_id).output('bag')
            movimento_tipo = 'TRU' if movimento_rec['tipomov_cod'] == 'TRE' else 'TRE'
            trasferimento = self.newrecord(data=data,movimento_id=movimento_id,verso='c', 
                                tipomov_cod=movimento_tipo,descrizione='TRE carico')
            self.insert(trasferimento)

            movimenti_righe = self.db.table('salt.movim_righe').query(where='$movim_id=:mov_id', 
                                                mov_id=movimento_id).fetch()
            if not movimenti_righe:
                    raise GnrException('Inserire prima la riga quantità')

            for movimento_riga in movimenti_righe:
                quantita = movimento_riga['quantita']
                trasferimento_riga = self.db.table('salt.movim_righe').newrecord(prodotto_id=movimento_riga['prodotto_id'], 
                                    movim_id=trasferimento['id'], movimento_riga_id=movimento_riga['id'], 
                                    deposito_id=deposito_id, quantita= - (quantita))

                self.db.table('salt.movim_righe').insert(trasferimento_riga)
        
        if kwargs['tipomov']=='GIU':
            movimento_rec = self.record(movimento_id).output('bag')
            movimento_tipo = 'GIU' if movimento_rec['tipomov_cod'] == 'GIE' else 'GIE' 
            trasferimento = self.newrecord(data=data,movimento_id=movimento_id,verso='c', 
                                tipomov_cod=movimento_tipo,descrizione='GIR carico')
            self.insert(trasferimento)

            movimenti_righe = self.db.table('salt.movim_righe').query(where='$movim_id=:mov_id', 
                                                mov_id=movimento_id).fetch()
            if not movimenti_righe:
                    raise GnrException('Inserire prima la riga quantità')

            for movimento_riga in movimenti_righe:
                quantita = movimento_riga['quantita']
                trasferimento_riga = self.db.table('salt.movim_righe').newrecord(prodotto_id=prodotto_id, 
                                    movim_id=trasferimento['id'], movimento_riga_id=movimento_riga['id'], 
                                    deposito_id=deposito_id, quantita= - (quantita))
                self.db.table('salt.movim_righe').insert(trasferimento_riga)
        
        self.db.commit()
    
        