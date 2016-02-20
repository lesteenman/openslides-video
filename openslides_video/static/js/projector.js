(function() {
    'use strict';

    angular.module('OpenSlidesApp.openslides_video.projector', ['OpenSlidesApp.openslides_video'])

    .config([
        'slidesProvider',
        function(slidesProvider) {
            slidesProvider.registerSlide('openslides_video/video', {
                template: 'static/templates/openslides_video/video_slide.html'
            });
        }
    ]);

    // .controller('Slide
    // );
})();
