#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    salt = root.branch('salt')
    salt.thpage('movim_righe',table='salt.movim_righe')
    salt.thpage('movim_prodotti',table='salt.movim_righe', viewResource='ViewMovimentiProd')
    salt.thpage('movimentazione',table='salt.movim')
    salt.thpage('prodotti',table='salt.prodotto')
    salt.lookups('Lookup tables',lookup_manager='salt')
