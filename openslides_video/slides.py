from django.template.loader import render_to_string

from openslides.config.api import config
from openslides.projector.api import register_slide, SlideError

from openslides.mediafile.models import Mediafile
from .models import Video


def openslides_video_presentation_as_slide(**kwargs):
    """
    Return the html code for a presentation of a Mediafile.
    At the moment, only the presentation of pdfs is supported.
    """
    file_pk = kwargs.get('pk', None)
    page_num = kwargs.get('page_num', 1)

    try:
        video = Mediafile.objects.get(
            pk=file_pk,
            filetype__in=Video.PRESENTABLE_VIDEO_TYPES,
            is_presentable=True)
    except Mediafile.DoesNotExist:
        raise SlideError
    context = {'video': video}
    return render_to_string('openslides_video/video_slide.html', context)


register_slide('openslides_video', openslides_video_presentation_as_slide, Mediafile)
