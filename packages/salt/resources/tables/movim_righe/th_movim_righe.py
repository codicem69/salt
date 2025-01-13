#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita',width='7em', totalize=True)
        r.fieldcell('movim_id')
        r.fieldcell('movim_carico', totalize=True)
        r.fieldcell('movim_scarico', totalize=True)

        r.fieldcell('rimanenza')
        
    def th_order(self):
        return 'data'

    def th_query(self):
        return dict(column='@prodotto_id.cod', op='contains', val='', runOnStart=True)
    #def th_query(self):
     #   return dict(column='prodotto_id', op='contains', val='')
    def th_options(self):
        return dict(widget='dialog', readOnly=True) 
    def th_top_toolbarsuperiore(self, top):
        top.slotToolbar('*,sections@prodotto_id,*', childname='superiore', _position='<bar')    


class ViewMovimentiProd(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita',width='7em', totalize=True, zoom=True)
        r.fieldcell('movim_id')
        r.fieldcell('movim_carico', totalize=True)
        r.fieldcell('movim_scarico', totalize=True)
        #r.fieldcell('somma', totalize=True)
        
    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='data', op='lesseq', val='', runOnStart=True)
        #con op='lesseq' valore minore uguale a (si puo verificare nell'inspector sotto la voce query where)

    #def th_query(self):
     #   return dict(column='prodotto_id', op='contains', val='')
    
    def th_options(self):
        return dict(widget='dialog', readOnly=True) 
    
    def th_top_toolbarsuperiore(self, top):
        top.slotToolbar('*,sections@prodotto_id,*', childname='superiore', _position='<bar')   

    #def th_queryBySample(self):
    #    return dict(fields=[dict(field='@movim_id.data', lbl='data_mov',width='10em'),
    #                        dict(field='@movim_id.descrizione', lbl='descrizione',width='10em')],
    #                        cols=2)

    def th_queryBySample(self):
        return dict(fields=[dict(field='@movim_id.data', lbl='data_minore_uguale',width='10em', op='lesseq', val=''),
                            dict(field='@movim_id.data', lbl='data_maggiore_uguale',width='10em', op='greatereq', val=''),
                            dict(field='@movim_id.data', lbl='data_mov',width='10em'),
                            dict(field='@movim_id.descrizione', lbl='descrizione',width='10em')],
                            cols=4, isDefault=True)

class ViewFromRighe(BaseComponent):

    def th_struct(self, struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id',hasDownArrow=True, edit=True)
        r.fieldcell('quantita',width='8em', edit=True, validate_notnull=True)
        r.fieldcell('tipomov_cod',validate_notnull=True, edit=True)
        
    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', defaultPrompt=dict(title='Nuovo movimento', fields=self.newRecParameters(),
                    doSave=True))

    def newRecParameters(self):
        return [dict(value='^.tipomov_cod', table='salt.tipo_mov', lbl='Tipo Movimento',
                    validate_notnull=True, tag='dbselect', hasDownArrow=True),
                dict(value='^.prodotto_id', table='salt.prodotto', lbl='Prodotto',
                    validate_notnull=True, tag='dbselect', hasDownArrow=True),
                    dict(value='^.quantita', lbl='Quantità',dtype='I',tag='numberTextBox',
                    validate_notnull=True)]

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('prodotto_id', hasDownArrow=True )
        fb.field('quantita',validate_notnull=True )

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
