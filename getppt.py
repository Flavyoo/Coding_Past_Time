# If you dont have requests installed or BeautifulSoup, install them first
# sudo pip install requests
# pip install bs4

import sys
import os
import stdio
import requests
from bs4 import BeautifulSoup

url = str(sys.argv[1])
# Name of directory to store content in.
directory_name = str(sys.argv[2])
# Path to where directory_name will be stored.
destination_name = str(sys.argv[3])

# Asks for a new directory, and creates one if it does not already exist.
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
# destination director is a path to where the files will placed.
def makdir(directory_name, destination_directory):
    """
    Creates a new directory to store power-points retrieved from the web. Makes sure
    that the name given for the new directory is not the same as the current
    directory.
    """
    dir2 = None
    location = destination_directory + "/" + directory_name
    if os.path.exists(location) == False:
        os.chdir(destination_directory)
        os.mkdir(directory_name)
        return location
    else:
        dir2 = check_dir(directory_name, destination_directory)
    return dir2

def get_ppt(url, directory_name, destination_name):
    content = requests.get(url)
    soup = BeautifulSoup(content.content, "html.parser")
    ppt_tags = soup.find_all('a')
    dest = makdir(directory_name, destination_name)
    print "Getting Files..."
    for link in ppt_tags:
        if link.string == ' ppt':
            name = link["href"].split("/")[-1]
            print str(url) + link["href"][2:]
            with open(dest + "/" + name, "wb") as power_point:
                power_point.write(requests.get(
                    str(url) + link["href"][1:]
                ).content)
                power_point.close
    print "Finished..."



def main():
    get_ppt(url, directory_name, destination_name)

# Execute when ran as a progam, not when imported.
if __name__ == '__main__':
    main()
