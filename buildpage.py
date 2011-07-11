#
# This script creates a html page with links using HTML5 video tags to
# all files given as arguments.
#
import sys
from string import Template

def getEpisodeName(path):
    return getPathElement(path, 0)

def getPathElement(path, num):
    if path == None:
        return None
    parts = path.split('/')

    if (len(parts) - 1 - num) < 0:
        return "unknown"

    return parts[len(parts) -1 - num]


def writeHtmlFile(file, uri, name):
    with open(file, 'w') as f:

        s = Template("<video src=\"$uri_addr\" controls=\"controls\"> your browser does not support the video tag </video>")

        uri_str = s.substitute(uri_addr=uri, uri_name=name)
        f.write(uri_str)

def writeLink(file, uri, name):
    s = Template('<a href="$uri_addr">$uri_name</a>')
    uri_str = s.substitute(uri_addr=uri, uri_name=name)
    file.write(uri_str)

def writeIndexHtmlFile(filelist):
    with open('index.html', 'w') as f:
        with open(filelist) as f2:
            for path in f2:
                ename = getEpisodeName(path)
                ename = ename.strip()
                html_fname = ename + '.html'
                writeLink(f, html_fname, ename)
                writeHtmlFile(html_fname, path, ename)
                f.write("<BR>\n")

        f.write("</body></html>")


writeIndexHtmlFile(sys.argv[1])
