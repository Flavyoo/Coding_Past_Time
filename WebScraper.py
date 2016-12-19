from bs4 import BeautifulSoup
import requests
import os
import sys

"""
Takes three command line inputs. the url of the website to scrape, name of
the directory to create, and the path to the directory to store the new
directory with the photos into. Script created for imaxxbp.com.
"""

url = str(sys.argv[1])
namedir = str(sys.argv[2])
direc = str(sys.argv[3])

def makdir(namedir, direc):
    """
    Creates a new directory to store photos retrieved from the web. Makes sure
    that the name given for the new directory is not the same as the current
    directory.
    """
    cudir = os.getcwd()
    if namedir != cudir and os.path.exists(direc + "/" + namedir) == False:
        folder = os.chdir(direc)
        os.mkdir(namedir)
    else:
        dir2 = check_dir(namedir)
    return dir2

def check_dir(d):
    namedir2 = d
    if os.path.exists(direc + "/" + d):
        print "The directory name already exists. Provide a new name."
        namedir2 = raw_input("New name. ")
        check_dir(namedir2);
    else:
        os.mkdir(namedir2)
    return namedir2


def get_images(url, namedir, direc):
    con = requests.get(url)
    soup = BeautifulSoup(con.content, "html.parser")
    dest = makdir(namedir, direc)
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


if __name__ == '__main__':
	get_images(url, namedir, direc)
