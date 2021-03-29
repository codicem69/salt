#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='salt package',sqlschema='salt',sqlprefix=True,
                    name_short='Salt', name_long='salt', name_full='Salt')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
