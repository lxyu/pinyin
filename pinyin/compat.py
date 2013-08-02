import sys
py2 = sys.version_info < (3, 0)


if py2:
    str_type = unicode

    def u(s):
        return unicode(s, "utf-8")
else:
    str_type = str

    def u(s):
        return s
