from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
        '',
        url(r'^video/play/$',
            views.VideoPlayView.as_view(),
            name='play_video'),
        url(r'^video/pause/$',
            views.VideoPauseView.as_view(),
            name='pause_video')
        )
