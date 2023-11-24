from pytube import YouTube


async def download_video(url, user_id):
    youtubeObject = YouTube(url)
    filesize = youtubeObject.streams.get_highest_resolution().filesize
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    if round(filesize / 1024 / 1024) <= 50:
        try:
            filename = f"user_video_{user_id}"
            youtubeObject.download(filename=filename)
            return filename
        except:
            return False
    else:
        return "50mb"

