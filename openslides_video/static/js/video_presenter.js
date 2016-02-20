video = {};
function updateVideoStatus() {
    var video_element = $('#video');
    if (video_element[0]) video_element = video_element[0];

    if (projector['video_playing']) {
        video_element.play();
    } else {
        video_element.pause();
    }

    var fullscreen = projector['video_fullscreen'];
    content = $('#content');
    presentation = $('#presentation');
    footer = $('#footer');
    body = $('body');
    if (fullscreen) {
        content.addClass('fullscreen');
        presentation.addClass('fullscreen');
        footer.addClass('black');
        body.addClass('black');
    } else {
        content.removeClass('fullscreen');
        presentation.removeClass('fullscreen');
        footer.removeClass('black');
        body.removeClass('black');
    }
}

projector['control_video'] = function(args) {
    projector['video_playing'] = args[0];
    projector['video_fullscreen'] = args[1];
    updateVideoStatus();
};

$(document).ready(function() {
    updateVideoStatus();
});
