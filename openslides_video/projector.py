from django.utils.translation import ugettext as _

from openslides.core.exceptions import ProjectorException
from openslides.utils.projector import ProjectorElement, ProjectorRequirement

from .models import Mediafile
from .views import MediafileViewSet


class OpenslidesVideoSlide(ProjectorElement):
    """
    Slide definitions for video model.
    """
    name = 'openslides_video/video'

    def get_context(self):
        try:
            Mediafile.objects.get(pk=self.config_entry.get('id'))
        except Mediafile.DoesNotExist:
            raise ProjectorException(_('File does not exist.'))

    def get_requirements(self, config_entry):
        pk = config_entry.get('id')
        if pk is not None:
            yield ProjectorRequirement(
                view_class=MediafileViewSet,
                view_action='retrieve',
                pk=str(pk))
