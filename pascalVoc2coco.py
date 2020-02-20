import glob
import json
import sys
import xml.dom.minidom
from os.path import join

data = {}

info = {
    "description": "Caltech faces dataset",
    "url": "http://www.vision.caltech.edu/html-files/archive.html",
    "version": "1.0",
    "year": 1999,
    "contributor": "Markus Weber",
    "date_created": "1999/1/1"
}

licenses = {}

data["info"] = info
data["images"] = []
data["annotations"] = []
data["categories"] = []
data["licenses"] = licenses

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass path to directory with .xml annotations")
        exit(1)

    directory = sys.argv[1]
    print("Directory:", directory)

    files = glob.glob(directory + "/*.xml")
    print("Found %i files" % len(files))

    for file in files:
        file_path = join(directory, file)

        try:
            doc = xml.dom.minidom.parse(file_path)
        except:
            print("Cannot parse", file_path, ", skipping")
            continue

        filename = doc.getElementsByTagName("filename")[0].firstChild.nodeValue
        size_el = doc.getElementsByTagName("size")[0]
        width = size_el.getElementsByTagName("width")[0].firstChild.nodeValue
        height = size_el.getElementsByTagName("height")[0].firstChild.nodeValue
        img_id = filename.split(".")[0]

        image = {
            "license": 1,
            "file_name": filename,
            "width": int(width),
            "height": int(height),
            "id": int(img_id),
            "coco_url": "",
            "flickr_url": "",
            "date_captured": "2013-11-14 17:02:52",
        }

        annotation = {
            "image_id": img_id,
            "file_name": filename,
            "segments_info": []
        }

        object_elems = doc.getElementsByTagName("object")
        segment_id = 1
        for object_el in object_elems:
            name = object_el.getElementsByTagName("name")[0].firstChild.nodeValue
            bndbox_el = object_el.getElementsByTagName("bndbox")[0]
            x_min = int(bndbox_el.getElementsByTagName("xmin")[0].firstChild.nodeValue)
            y_min = int(bndbox_el.getElementsByTagName("ymin")[0].firstChild.nodeValue)
            x_max = int(bndbox_el.getElementsByTagName("xmax")[0].firstChild.nodeValue)
            y_max = int(bndbox_el.getElementsByTagName("ymax")[0].firstChild.nodeValue)

            width = abs(x_max - x_min)
            height = abs(y_max - y_min)

            category = next((x for x in data["categories"] if x["name"] == name), None)
            if category is None:
                data["categories"].append({
                    "id": len(data["categories"]),
                    "name": name,
                    "supercategory": name
                })
                category = data["categories"][len(data["categories"]) - 1]

            annotation["segments_info"].append({
                "id": segment_id,
                "category_id": category["id"],
                "area": width * height,
                "bbox": [x_min, y_min, width, height],
                "iscrowd": 0
            })
            data["annotations"].append(annotation)
            segment_id += 1

        print(annotation)

        data["images"].append(image)

    with open('../data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
