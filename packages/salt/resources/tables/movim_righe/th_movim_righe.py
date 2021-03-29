#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita')
        r.fieldcell('movim_id')

    def th_order(self):
        return 'prodotto_id'

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')

class ViewFromRighe(BaseComponent):

    def th_struct(self, struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id', edit=True)
        r.fieldcell('quantita', edit=True)
        r.fieldcell('tipomov_id', edit=True)
        

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('prodotto_id' )
        fb.field('quantita' )
        fb.field('movim_id' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
