import urllib.request

class data_manage(object):

    global f

    def __init__(self, url):
        self.url = url
        global f
        try:
            f = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
        else:
            print("aaaaaa")

    def get_httpcode(self):
        global f
        # if f is None:
        return f.getcode()
        # else:
        #     return "url is not right"

    def get_htmlcontent(self):
        global f
        if f:
            return "%s" % f.readlines()
        else:
            return "url is not right"

    def get_linknum(self):
        global f
        if f:
            text = self.get_htmlcontent()
            num = 0
            if text.startswith("<a href="):
                num += 1
            return num
        else:
            return "url is not right"


if __name__ == "__main__":
    manage = data_manage("http:1234")
    # print(manage.get_httpcode())
    # print(manage.get_htmlcontent())
    # print(manage.get_linknum())

