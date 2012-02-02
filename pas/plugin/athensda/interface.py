from Products.PluggableAuthService import interfaces
  
#class IAthensdaHelper(interfaces):
#    """interface for AthensdaHelper."""
 
from zope.interface import Interface

from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate

class IAthensdaHelper(Interface):
    """ Marker interface.
    """

manage_addAthensdaHelperForm = PageTemplateFile(
    'dir/caAdd', globals(), __name__='manage_addAthensdaHelperForm')


def addAthensdaHelper( dispatcher
                       , id
                       , title=None
                       , REQUEST=None
                       ):
    """ Add a Athens Auth Helper to a Pluggable Auth Service. """
    sp = AthensdaHelper(id, title)
    dispatcher._setObject(sp.getId(), sp)

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect( '%s/manage_workspace'
                                      '?manage_tabs_message='
                                      'AthensdaHelper+added.'
                                    % dispatcher.absolute_url() )

