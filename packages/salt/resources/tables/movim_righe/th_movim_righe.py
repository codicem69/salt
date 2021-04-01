#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita',width='7em', totalize=True)
        r.fieldcell('movim_id')
        r.fieldcell('movim_carico', totalize=True)
        r.fieldcell('movim_scarico', totalize=True)
        #r.fieldcell('somma', totalize=True)
        
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

class ViewFromRighe(BaseComponent):

    def th_struct(self, struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id',hasDownArrow=True, edit=True)
        r.fieldcell('quantita', edit=True)
        r.fieldcell('tipomov_id', edit=True)
        

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('prodotto_id', hasDownArrow=True )
        fb.field('quantita' )
        fb.field('movim_id' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
