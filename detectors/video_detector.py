def detect_video_platform(html):

    html = html.lower()

    videos = []

    if "vimeo.com" in html:
        videos.append("Vimeo")

    if "youtube.com" in html:
        videos.append("YouTube")

    if "wistia" in html:
        videos.append("Wistia")

    if "bunnycdn" in html:
        videos.append("Bunny Video")

    return videos
