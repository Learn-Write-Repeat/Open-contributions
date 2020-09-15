# Introduction to pytube library 
- We know YouTube is very popular video sharing platform in the entire world.
- At times we wants to download a video which we can play in offline mode.
For that, we download any online youtube downloader or any sites that saves the video into our computer.
- Our work is done, but while adoptiong this way we come across many multiple sites which gets open in our background which is unsafe.
- But have you ever think of creating our own program to download youtube videos?
-  Python program with fewer number of lines of code which makes our job easier.
- It has a library named as ‘pytube’ to download youtube videos directly.
>What is pytube library in python?

#### ***pytube*** is a lightweight, dependency-free Python library which is used for downloading videos from the web.
>Why pytube to be adopted?
- No Third-Party Dependencies
- Extensively Documented Source Code
- Ability to Capture Thumbnail URL
- Caption Track Support
- Outputs Caption Tracks to .srt format (SubRip Subtitle)
- Command-line Interfaced Included
- Makes pipelining easy

## Installation
Installation is easy when you have **pip** via **pypi**. In the Terminal or Command Prompt, type the following command to install pytube.

	 $ pip install pytube3
 
 ## Lets get started!!!
 *Let’s start by importing the youtube class:*
 
	from pytube import YouTube	

*Now get any link from the youtube you want to download*:

	yt = YouTube('https://www.youtube.com/watch?v=WvhQhj4n6b8')
*The pytube API makes all information intuitive to access. For example, this is how you would get the video's title:*

	>>>yt.title
		What is Python? | Introduction to Python | Python Programming For Beginners | Edureka



*We can also get the thumbnail url of the video:*

	>>>yt.thumbnail_url
		https://i.ytimg.com/vi/WvhQhj4n6b8/maxresdefault.jpg

*Now, we need to select the media format. Pytube module provides different media formats to download video which we wish to:*

	>>>stream = yt.streams.all()
		[<Stream: itag="18" mime_type="video/mp4" res="360p"fps="30fps" vcodec="avc1.42001E" acode
	c="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" re
	s="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video
	">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028"
	progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" f
	ps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="v
	ideo/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">]


*The video will be downloaded into your destination path:*

	>>>stream.download('**specific location**')
*The video will be downloaded into your current directory:*

	>>>stream.download()

> **The above steps explains breifly to use the python library pytube easily to download multiple videos from the youtube.**
