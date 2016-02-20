from openslides.utils.widgets import Widget
from openslides.mediafile.models import Mediafile

from .models import Video

class VideoPresentationWidget(Widget):
    name = 'video_presentations'
    verbose_name = 'Videos'
    required_permission = 'core.can_manage_projector'
    default_column = 1
    default_weight = 76
    template_name = 'openslides_video/widget.html'

    def get_context_data(self, **context):
        videos = Mediafile.objects.filter(
                filetype__in=Video.PRESENTABLE_VIDEO_TYPES,
                is_presentable=True)
        return super(VideoPresentationWidget, self).get_context_data(
                videos=videos,
                **context)
