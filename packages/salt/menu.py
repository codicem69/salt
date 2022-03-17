# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        salt = root.branch(u"salt", tags="")
        salt.thpage(u"movimentazione", table="salt.movim", tags="")
        salt.thpage(u"movim_prodotti", table="salt.movim_righe", tags="", viewResource="ViewMovimentiProd")
        salt.thpage(u"movim_righe", table="salt.movim_righe", tags="")
        salt.thpage(u"prodotti", table="salt.prodotto", tags="")
        salt.lookups(u"Lookup tables", lookup_manager="salt")

