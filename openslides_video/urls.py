from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
        '',
        url(r'^video_import/$',
            views.VideoImportView.as_view(),
            name="video_import"),
        url(r'^video_list/$',
            views.VideoListView.as_view(),
            name="video_list"),
        url(r'^video/play/$',
            views.VideoPlayView.as_view(),
            name='play_video'),
        url(r'^video/pause/$',
            views.VideoPauseView.as_view(),
            name='pause_video')
        )
