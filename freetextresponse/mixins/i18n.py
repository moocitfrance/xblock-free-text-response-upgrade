"""
Mixin i18n logic
"""
from xblock.core import XBlock


@XBlock.needs('i18n')
class I18nXBlockMixin(XBlock):
    """
    Make an XBlock translation-aware
    """

    def _i18n_service(self):
        """
        Provide the XBlock runtime's i18n service
        """
        service = self.runtime.service(self, 'i18n')
        return service

    def ugettext(self, text):
        """
        Call ugettext from the XBlock i18n service
        """
        text = self._i18n_service().ugettext(text)
        return text

    def ngettext(self, *args, **kwargs):
        """
        Call ngettext from the XBlock i18n service
        """
        text = self._i18n_service().ngettext(*args, **kwargs)
        return text
