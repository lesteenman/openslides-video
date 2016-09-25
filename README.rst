========================================
Openslides Video
========================================

Note for OpenSlides 2.0
=======================
This functionality will be included in the main OpenSlides repository soon (as of 25-09-2016) as core functionality. Therefore, this plugin is not necessary for OpenSlides 2.

Overview
========
This plugin adds support for showing videos through OpenSlides.

Requirements
============
 - OpenSlides 1.7.x

Install
=======
I. Installation on Windows (with OpenSlides portable version)
-------------------------------------------------------------

1. Get the latest Video plugin release from:

   https://github.com/lesteenman/openslides-video

2. Move the plugin directory (openslides_video, instead of the main
   folder/repository) to:

    '<path-to-openslides-portable>/openslides/plugins/'

3. Start openslides.exe.

II. Installation on GNU/Linux and MacOSX
----------------------------------------
1. Setup and activate a virtual environment::

    $ virtualenv .virtualenv

    $ source .virtualenv/bin/activate

2. Install OpenSlides and VoteCollector plugin from the Python Package Index (PyPI)::

    $ pip install openslides git+https://github.com/lesteenman/openslides-video

    OpenSlides and all required python packages will be installed.

3. Start OpenSlides::

    $ openslides

Using the plugin
================

After the plugin is installed, you can add the video widget to the dashboard. If you
upload any supported video file (which is most types of video) and set it as
'presentable', it will show up in the list of this widget.

To start a video, simply click the 'present' icon next to the video you want to play.
Next, click the 'play' icon. When you do so, the video will automatically enter
fullscreen mode, and remain in this mode until you pause the video.

To restart a video, simply click the present button again.

License and Author
==================
This plugin is Free/Libre Open Source Software and distributed under the
MIT License, see LICENSE file. The plugin was made by Erik Steenman
(https://github.com/lesteenman).

Changelog
=========
Version 1.0.0 (2016-02-26)
--------------------------
* First release of this plugin for OpenSlides 1.7.x.
