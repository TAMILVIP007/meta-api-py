from requests import get


class META():
    def __init__(self):
        self.url = "https://metavoid.vercel.app/api"

    def  animeimage(self, anime_name, nsfw=None):
        try:
            if nsfw:
                url = f"{self.url}/animeimage/nsfw/{anime_name}"
            url = f"{self.url}/animeimage/sfw/{anime_name}"
            response = get(url, timeout=5)
            return response.json()
        except  Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def yt_info(self, yt_url):
        try:
            url = f"{self.url}/ytdl?link={yt_url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def wallpaper(self, query):
        try:
            url = f"{self.url}/wall/alphacoders?search={query}&page=1"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def truth(self):
        try:
            url = f"{self.url}/truth"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def dare(self):
        try:
            url = f"{self.url}/dare"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def vanitas(self, user):
        try:
            url = f"{self.url}/vanitas/user={user}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def wiki(self, query, lang="en"):
        try:
            if lang:
                url = f"{self.url}/wiki?search={query}&lang={lang}" 
            url = f"{self.url}/wiki?search={query}&lang=en"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def insta_dl(self, url):
        try:
            url = f"{self.url}/igdl?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def fb_dl(self, url):
        try:
            url = f"{self.url}/fbdl?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def twitter_dl(self, url):
        try:
            url = f"{self.url}/twitter?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def translate(self, text, lang=None):
        try:
            if lang:
                url = f"{self.url}/translate/text={text}/language={lang}" 
            url = f"{self.url}/translate/text={text}/language=en"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
