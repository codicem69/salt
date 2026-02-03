#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrdecorator import customizable, metadata

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('tipomov_cod')
        r.fieldcell('descrizione')
        r.fieldcell('totale_movim', format='#,###',totalize=True, dtype='N')
        
    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='tipomov_cod', op='contains', val='', runOnStart=True)


class Form(BaseComponent):
    
    def th_form(self, form):
        bc = form.center.borderContainer()
        self.movimTestata(bc.contentPane(region='top', datapath='.record', height='150px'))
        self.movRighe(bc.contentPane(region='center'))
        
    def movimTestata(self, pane):
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('data')
        fb.field('tipomov_cod',validate_notnull=True)
        fb.field('descrizione',width='100%', colspan=2)
        
    #def movRighe(self, pane):
     #   pane.inlineTableHandler(relation='@righemov', viewResource='ViewFromRighe', picker='movim_id')
 
    def movRighe(self, pane):
        pane.inlineTableHandler(relation='@righemov', viewResource='ViewFromRighe')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', defaultPrompt=dict(title='Nuovo movimento', fields=self.newRecParameters(),
                    doSave=True))

    @customizable
    def th_top_custom(self,top):
        bar = top.bar
        bar.replaceSlots('navigation','navigation,10,5,azioni')

        #bar.consegnato.button('^.etichetta', action="PUBLISH consegnato = {movimento_id:movimento_id}", 
        #                    movimento_id='=#FORM.record.id', disabled='^#FORM.record.in_attesa?=!#v')
        

        trasferimento_fields=[dict(name='deposito_id', table='salt.deposito', lbl='Nuovo Deposito', tag='dbselect',hasDownArrow=True)]
        bar.azioni.button('^.etichetta',  
                            action="PUBLISH trasferimento = {data:data,movimento_id:movimento_id,deposito_id:deposito_id,tipomov:tipomov}", 
                            data='=#FORM.record.data',movimento_id='=#FORM.record.id', deposito_id='=.deposito_id',tipomov='=#FORM.record.tipomov_cod',
                            hidden='^#FORM.record.tipomov_cod?=#v!="TRU"',
                            disabled='^#FORM.record.@movim.id',
                            ask=dict(title='Genera trasferimento',fields=trasferimento_fields, dlg_width='320px'))
        
        giroconto_fields=[dict(name='prodotto_id', table='salt.prodotto', lbl='Nuovo Prodotto', tag='dbselect',hasDownArrow=True),
                          dict(name='deposito_id', table='salt.deposito', lbl='Nuovo Deposito', tag='dbselect',hasDownArrow=True)]
        bar.azioni.button('^.etichetta',  
                            action="PUBLISH trasferimento = {data:data,movimento_id:movimento_id,prodotto_id:prodotto_id,deposito_id:deposito_id,tipomov:tipomov}", 
                            data='=#FORM.record.data',movimento_id='=#FORM.record.id', prodotto_id='=.prodotto_id',deposito_id='=.deposito_id',tipomov='=#FORM.record.tipomov_cod',
                            hidden='^#FORM.record.tipomov_cod?=#v!="GIU"',
                            disabled='^#FORM.record.@movim.id',
                            ask=dict(title='Genera giroconto',fields=giroconto_fields, dlg_width='320px'))
        bar.azioni.dataController("""if (tipomov=='TRU'){var etichetta = 'Genera Trasferimento'}
                                     else if (tipomov=='GIU'){var etichetta = 'Genera Giroconto'}
                                     SET .etichetta = etichetta""",
                                         tipomov="^#FORM.record.tipomov_cod")
        #top.dataRpc(None,self.db.table('salt.movim').confermaMovimento, 
        #                subscribe_consegnato=True, _onResult='this.form.reload();')
#
        top.dataRpc(None,self.db.table('salt.movim').creaTrasferimento, 
                        subscribe_trasferimento=True, _onResult='this.form.reload();')
        
        return bar
    
    def newRecParameters(self):
        return [dict(value='^.data', lbl='Data Movimento',
                    validate_notnull=True, tag='dateTextBox',hasDownArrow=True),
                dict(value='^.tipomov_cod', table='salt.tipo_mov', lbl='Tipo Movimento',condition='$cod!=:cod AND $cod!=:cod2',
                    condition_cod='TRE',condition_cod2='GIE',validate_notnull=True, tag='dbselect', hasDownArrow=True),
                dict(value='^.descrizione', lbl='Descrizione',values='^.tipomov_cod',tag='filteringSelect',
                    validate_notnull=True)]
