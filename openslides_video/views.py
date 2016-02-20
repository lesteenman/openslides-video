from openslides.utils.views import (View, TemplateView, AjaxView)
from openslides.projector.api import get_active_slide
from openslides.utils.tornado_webserver import ProjectorSocketHandler

class VideoControlView(AjaxView):
    def get_ajax_context(self, *args, **kwargs):
        return {
            'video_playing': self.active_slide['video_playing'],
            'video_fullscreen': self.active_slide['video_fullscreen']
        }

    def update_video_state(self, active_slide):
        ProjectorSocketHandler.send_updates(
            {'calls': {'control_video': [
                active_slide['video_playing'],
                active_slide['video_fullscreen']
            ]}})

class VideoPlayView(VideoControlView):
    """
    Play current video
    """
    def get(self, request, *args, **kwargs):
        self.active_slide = get_active_slide()
        if self.active_slide['callback'] == 'openslides_video':
            self.active_slide['video_playing'] = True
            self.active_slide['video_fullscreen'] = True
            self.update_video_state(self.active_slide)
            response = super(VideoPlayView, self).get(self, request, *args, **kwargs)
        else:
            response = HttpResponse()
        return response

class VideoPauseView(VideoControlView):
    """
    Pause current video
    """
    def get(self, request, *args, **kwargs):
        self.active_slide = get_active_slide()
        if self.active_slide['callback'] == 'openslides_video':
            self.active_slide['video_playing'] = False
            self.active_slide['video_fullscreen'] = False
            self.update_video_state(self.active_slide)
            response = super(VideoPauseView, self).get(self, request, *args, **kwargs)
        else:
            response = HttpResponse()
        return response
