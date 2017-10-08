# If you dont have requests installed or BeautifulSoup install them first"
from bs4 import BeautifulSoup
import requests
import os
import sys

"""
Takes three command line inputs. the url of the website to scrape, name of
the directory to create, and the path to the directory to store the new
directory and the files in.
"""

url = str(sys.argv[1])
namedir = str(sys.argv[2])
direc = str(sys.argv[3])

# Asks for a new directory, and creates if it does alreay exist.
def check_dir(d, dest_name):
    namedir2 = d
    if os.path.exists(dest_name + "/" + d):
        print "The directory name already exists. Provide a new name."
        namedir2 = raw_input("New name. ")
        check_dir(namedir2, destination_name);
    else:
        os.chdir(dest_name)
        os.mkdir(namedir2)
    return dest_name + "/" + namedir2

# Makes a directory "directory_name" in the destination_directory.
# destination director is a path to where you want the files placed.
def makdir(directory_name, destination_directory):
    """
    Creates a new directory to store power-points retrieved from the web. Makes sure
    that the name given for the new directory is not the same as the current
    directory.
    """
    current_dir = os.getcwd()
    dir2 = None
    location = destination_directory + "/" + directory_name
    if os.path.exists(location) == False:
        os.chdir(destination_directory)
        os.mkdir(directory_name)
        return location
    else:
        dir2 = check_dir(directory_name, destination_directory)
    return dir2


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
