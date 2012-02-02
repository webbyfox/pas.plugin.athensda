"""Class: AthensdaHelper
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

import interface
import plugins

class AthensdaHelper( # -*- implemented plugins -*-
                               ):
    """Multi-plugin

    """

    meta_type = 'athensda Helper'
    security = ClassSecurityInfo()

    def __init__( self, id, title=None ):
        self._setId( id )
        self.title = title



classImplements(AthensdaHelper, interface.IAthensdaHelper)

InitializeClass( AthensdaHelper )
