from django.conf import settings
from django.template.loader import render_to_string

from inplaceeditform.fields import AdaptorForeingKeyField, AdaptorCommaSeparatedManyToManyField


class AdaptorAutoCompleteProvider(object):

    def install_ajax_select(self):
        if 'ajax_select' in settings.INSTALLED_APPS:
            lookup = self.config.get('lookup', None)
            auto_field = self.auto_complete_field
            if lookup and auto_field:
                return True
        return False

    def get_field(self):
        field = super(AdaptorAutoCompleteProvider, self).get_field()
        if self.install_ajax_select():
            lookup = self.config.get('lookup', None)
            auto_field = self.auto_complete_field
            field.field = auto_field(lookup, required=field.field.required)
        return field

    def render_media_field(self,
            template_name="inplaceeditform_extra_fields/autocomplete/render_media_field.html",
            extra_context=None):
        if self.install_ajax_select():
            return super(AdaptorAutoCompleteProvider, self).render_media_field(template_name, extra_context)
        return super(AdaptorAutoCompleteProvider, self).render_media_field()


    def render_value_edit(self):
        value = super(AdaptorAutoCompleteProvider, self).render_value_edit()
        if self.install_ajax_select():
            return render_to_string('inplaceeditform_extra_fields/autocomplete/render_value.html',
                                    {'value': value,
                                    'MEDIA_URL': settings.MEDIA_URL,
                                    'is_ajax': self.request.is_ajax()})
        return super(AdaptorAutoCompleteProvider, self).render_value_edit()


class AdaptorAutoCompleteForeingKeyField(AdaptorAutoCompleteProvider, AdaptorForeingKeyField):

    @property
    def auto_complete_field(self):
        try:
            from ajax_select.fields import AutoCompleteSelectField
            return AutoCompleteSelectField
        except ImportError:
            return None

    @property
    def name(self):
        return 'auto_fk'


class AdaptorAutoCompleteManyToManyField(AdaptorAutoCompleteProvider, AdaptorCommaSeparatedManyToManyField):

    @property
    def auto_complete_field(self):
        try:
            from ajax_select.fields import AutoCompleteSelectMultipleField
            return AutoCompleteSelectMultipleField
        except ImportError:
            return None

    @property
    def name(self):
        return 'auto_m2m'

    def get_value_editor(self, value):
        return [pk for pk in value.split("|") if pk]