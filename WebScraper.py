from bs4 import BeautifulSoup
import requests
import os
import sys

    """
    Takes three command line inputs. the url of the website to scrape, name of
    the directory to create, and the directory to store the new directory into.
    """

url = str(sys.argv[1])
name = str(sys.argv[2])
direc = str(sys.argv[3])

def makdir(name, direc):
    """
    Creates a new directory to store photos retrieved from the web. Makes sure
    that the name given for the new directory is no the same as the current
    directory.
    """
    cudir = os.getcwd()
    if name != cudir:
        folder = os.chdir(direc)
        os.mkdir(name)
    else:
        os.mkdir(name)
    return name

def get_images(url, name, direc):
    con = requests.get(url)
    soup = BeautifulSoup(con.content, "html.parser")
    dest = makdir(name, direc)
    print "Retrieving Images..."
    for im in soup.find_all("img"):
        urlimage = im.get("src")
        name = im.get("alt")
        nname = name.replace("- ", "")
        newname = nname.replace(" ", "_") + ".jpg"
        with open(dest + "/" + newname, "wb") as fil:
            fil.write(requests.get(urlimage).content)
            fil.close
    print "Finished..."
