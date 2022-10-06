# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        user=self.db.currentEnv.get('user')

        if user != 'admin':
            salt = root.branch(u"salt", tags="")
            salt.thpage(u"movimentazione", table="salt.movim", tags="")
            salt.thpage(u"movim_prodotti", table="salt.movim_righe", tags="", viewResource="ViewMovimentiProd")
            salt.thpage(u"movim_righe", table="salt.movim_righe", tags="")
            salt.thpage(u"prodotti", table="salt.prodotto", tags="")
            salt.lookups(u"Lookup tables", lookup_manager="salt")
        else:
            salt = root.branch(u"salt", tags="")
            salt.packageBranch('Amministrazione sistema',pkg='adm')
            salt.packageBranch('System',pkg='sys')
            salt.thpage(u"movimentazione", table="salt.movim", tags="")
            salt.thpage(u"movim_prodotti", table="salt.movim_righe", tags="", viewResource="ViewMovimentiProd")
            salt.thpage(u"movim_righe", table="salt.movim_righe", tags="")
            salt.thpage(u"prodotti", table="salt.prodotto", tags="")
            salt.lookups(u"Lookup tables", lookup_manager="salt")

