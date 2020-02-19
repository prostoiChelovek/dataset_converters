import glob
import sys
import xml.dom.minidom
from os import rename
from os.path import join, split, splitext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass path to directory with .xml annotations")
        exit(1)

    directory = sys.argv[1]
    print("Directory:", directory)

    files = glob.glob(directory + "/*.xml")
    print("Found %i files" % len(files))

    num = 1
    for file in files:
        file_path = join(directory, file)

        try:
            doc = xml.dom.minidom.parse(file_path)
        except:
            continue

        filename_el = doc.getElementsByTagName("filename")[0].firstChild
        path_el = doc.getElementsByTagName("path")[0].firstChild
        filename = filename_el.nodeValue
        path = path_el.nodeValue

        parent_dir = split(path)[0]
        _, file_extension = splitext(filename)
        new_name = str(num) + file_extension
        new_path = join(parent_dir, new_name)

        path_el.nodeValue = new_path

        rename(path, new_path)

        path_el.nodeValue = new_path
        filename_el.nodeValue = new_name

        with open(file_path, 'w') as f:
            f.write(doc.toxml())

        rename(file_path, join(directory, str(num) + ".xml"))

        num += 1
