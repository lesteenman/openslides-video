from openslides.mediafile.models import Mediafile

class Video(Mediafile):
    # slide_callback_name = 'openslides_video'
    PRESENTABLE_VIDEO_TYPES = [
            'video/quicktime',
            'video/mp4',
            'video/webm',
            'video/ogg',
            'video/x-flv',
            'application/x-mpegURL',
            'video/MP2T',
            'video/3gpp',
            'video/x-msvideo',
            'video/x-ms-wmv'
            ]

    """
    Subclass of Mediafile to support videos.
    """
