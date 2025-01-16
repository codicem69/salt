#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod',width='4em')
        r.fieldcell('descrizione',width='6em')
        r.fieldcell('tot_carico_prod', totalize=True, format='#,###')
        r.fieldcell('tot_scarico_prod', totalize=True, format='#,###')
        depositi = self.db.table('salt.deposito').query().fetch()
        for deposito in depositi:
            dep = deposito['id']
            dep_name = deposito['codice']
            cset = r.columnset(dep_name, name=dep_name)
            cset.cell('qta_{dep}'.format(dep=dep), dtype='L', name='Giacenza', width='6em', format='#,###', totalize=True)  
        #r.fieldcell('rimanenza_prod',width='10em', totalize=True)
        
    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cod' )
        fb.field('descrizione' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
