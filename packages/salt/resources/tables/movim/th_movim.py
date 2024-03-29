#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('descrizione')
        r.fieldcell('totale_movim')
        
    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='', runOnStart=True)


class Form(BaseComponent):
    
    def th_form(self, form):
        bc = form.center.borderContainer()
        self.movimTestata(bc.contentPane(region='top', datapath='.record', height='150px'))
        self.movRighe(bc.contentPane(region='center'))
        
    def movimTestata(self, pane):
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('data')
        fb.field('descrizione',validate_notnull=True,tag='comboBox', width='25em')
        
    #def movRighe(self, pane):
     #   pane.inlineTableHandler(relation='@righemov', viewResource='ViewFromRighe', picker='movim_id')
 
    def movRighe(self, pane):
        pane.inlineTableHandler(relation='@righemov', viewResource='ViewFromRighe',
                                picker='prodotto_id')
   #def th_options(self):
   #    return dict(dialog_height='400px', dialog_width='600px', defaultPrompt=dict(title='Nuovo movimento', fields=self.newRecParameters(),
   #                doSave=True))

   #def newRecParameters(self):
   #    return [dict(value='^.tipo_mov_id', table='salt.tipo_mov', lbl='Tipo Movimento',
   #                validate_notnull=True, tag='dbselect', hasDownArrow=True)]
