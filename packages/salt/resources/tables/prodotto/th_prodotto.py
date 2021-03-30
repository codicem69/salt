#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod')
        r.fieldcell('descrizione')
        r.fieldcell('tot_carico_prod')
        r.fieldcell('tot_scarico_prod')
        r.fieldcell('rimanenza_prod')
        
    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cod' )
        fb.field('descrizione' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
