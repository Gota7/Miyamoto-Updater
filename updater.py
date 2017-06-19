import os
import sys
import urllib.request
import platform
import getopt
import zipfile
import shutil
import glob

miyamotoUpdater_path = os.path.dirname(os.path.realpath(sys.argv[0])).replace("\\", "/")

miyamoto_path = miyamotoUpdater_path

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def main(argv):

    print("Fetching Latest release.txt")
    #Get links to downloads
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/Gota7/Miyamoto/master/release.txt", miyamotoUpdater_path + "/newestRelease.txt")

    newVersionValues = []

    with open(miyamotoUpdater_path + '/newestRelease.txt', 'r') as txt:
        for line in txt.readlines():
            newVersionValues.append(line.rstrip())

    print("Done")
    print("Newest Version Is Version " + newVersionValues[1])
    os.remove(miyamotoUpdater_path + '/newestRelease.txt')

    print("Making Temporary folders")
    if not os.path.isdir(miyamoto_path+"/TEMP"):
        os.mkdir(miyamoto_path+"/TEMP")
        os.chdir(miyamoto_path+"/TEMP")
        os.mkdir("src")
        os.mkdir("release")
        os.chdir(miyamoto_path)

    if os.path.isdir(miyamoto_path+"/linuxTools"):
            shutil.rmtree(miyamoto_path+"/linuxTools")
    if os.path.isdir(miyamoto_path+"/Tools"):
            shutil.rmtree(miyamoto_path+"/Tools")
    if os.path.isdir(miyamoto_path+"/macTools"):
            shutil.rmtree(miyamoto_path+"/macTools")
    if os.path.isdir(miyamoto_path+"/miyamotodata"):
            shutil.rmtree(miyamoto_path+"/miyamotodata")
    if os.path.isdir(miyamoto_path+"/miyamotoextras"):
            shutil.rmtree(miyamoto_path+"/miyamotoextras")
    if os.path.isdir(miyamoto_path+"/miyamotoData"):
            shutil.rmtree(miyamoto_path+"/miyamotoData")
    if os.path.isdir(miyamoto_path+"/miyamotoExtras"):
            shutil.rmtree(miyamoto_path+"/miyamotoExtras")
    if os.path.isdir(miyamoto_path+"/__pycache__"):
            shutil.rmtree(miyamoto_path+"/__pycache__")
    if os.path.isdir(miyamoto_path+"/miyamotoextras"):
            shutil.rmtree(miyamoto_path+"/miyamotoextras")

    #Get arguments.
    if "-r" in sys.argv:
        print("Updating Release of Miyamoto")

        if platform.system() == 'Windows':
            print("Updating Source of Miyamoto")

            print("Beginning Download")
            urllib.request.urlretrieve (newVersionValues[7], miyamotoUpdater_path + "/TEMP/release/release.zip")
            print("Finished Download")

        elif platform.system() == 'Linux':
            print("Updating Source of Miyamoto")

            print("Beginning Download")
            urllib.request.urlretrieve (newVersionValues[9], miyamotoUpdater_path + "/TEMP/release/release.zip")
            print("Finished Download")
        elif platform.system() == 'Darwin':
            print("Updating Source of Miyamoto")

            print("Beginning Download")
            urllib.request.urlretrieve (newVersionValues[11], miyamotoUpdater_path + "/TEMP/release/release.zip")
            print("Finished Download")

        print("Extracting Miyamoto Source")
        zip_ref = zipfile.ZipFile(miyamotoUpdater_path + "/TEMP/release/release.zip", 'r')
        zip_ref.extractall(miyamotoUpdater_path + "/TEMP/release/Miyamoto-master")
        zip_ref.close()
        print("Finished Extracting")

        print("Installing New Miyamoto")
        src_files = miyamotoUpdater_path + "/TEMP/release/Miyamoto-master"
        copytree(src_files, miyamoto_path)
        print("Finished Installing")

        print("Cleaning Up Junk Files")
        shutil.rmtree(src_files)
        os.remove(miyamotoUpdater_path + "/TEMP/release/release.zip")
        print("Finished Cleaning")

        print("Miyamoto has been updated successfully! Restart Miyamoto to apply changes.")

    elif "-s" in sys.argv:
        print("Updating Source of Miyamoto")

        print("Beginning Download")
        urllib.request.urlretrieve (newVersionValues[13], miyamotoUpdater_path + "/TEMP/src/src.zip")
        print("Finished Download")

        print("Extracting Miyamoto Source")
        zip_ref = zipfile.ZipFile(miyamotoUpdater_path + "/TEMP/src/src.zip", 'r')
        zip_ref.extractall(miyamotoUpdater_path + "/TEMP/src")
        zip_ref.close()
        print("Finished Extracting")

        print("Installing New Miyamoto")
        src_files = miyamotoUpdater_path + "/TEMP/src/Miyamoto-master"
        copytree(src_files, miyamoto_path)
        print("Finished Installing")

        print("Cleaning Up Junk Files")
        shutil.rmtree(src_files)
        os.remove(miyamotoUpdater_path + "/TEMP/src/src.zip")
        if os.path.isdir(miyamoto_path+"/TEMP"):
            shutil.rmtree(miyamoto_path+"/TEMP")
        print("Finished Cleaning")

        print("Miyamoto has been updated successfully! Restart Miyamoto to apply changes.")

    else:
        print("Miyamoto-Updater can update source or release. Use -r or -s to specify")

if __name__ == "__main__":
    main(sys.argv[1:])
