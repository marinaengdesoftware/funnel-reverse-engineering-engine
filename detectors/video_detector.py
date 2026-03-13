def detect_video_platform(html):

    videos = []

    if "vimeo.com" in html:
        videos.append("Vimeo")

    if "youtube.com" in html:
        videos.append("YouTube")

    if "wistia" in html:
        videos.append("Wistia")

    return videos
