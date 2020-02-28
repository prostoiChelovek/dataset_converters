# Datasets tools
This is a bunch of simple python scripts to convert between different datasets` annotation formats.

## Usage

### Caltech to pascalVoc
    python matlab_to_pacal_voc.py <path to .xml file> <path to output directory>
This script converts [Caltech dataset\`s](http://www.vision.caltech.edu/html-files/archive.html) annotations from matlab array to pascalVoc.  
It will save .xml file for every image to `annotations` directory in `<path to output directory>`.

### Yolo to pascalVov
    python yolo_to_voc.py <path to directory with annotations in yolo format> <path to output direcotry> <path to directory with images>
Currently this script supports only one class and you can change it on 49 line.

### PascalVoc to COCO
    python pascalVoc2coco.py <path to direcoty with pascalVoc annotations> <path to output json file>
This script converts annotations from pascalVoc format to coco.  
You can change info about your dataset in script.

### SoF to json
    python sof_to_json.py <path to .mat input file> <path to json output file>
This script converts [SoF annotations](https://sites.google.com/view/sof-dataset) from matlab array to json in this format:  

    [
        {
            "id": "AbdA",
            "sequence": "00001",
            "gender": "m",
            "age": 31,
            "lightning": "i",
            "view": "f",
            "cropped": false,
            "emotion": 1,
            "year": 2016,
            "part": "2",
            "glasses": 1,
            "headscarf": false,
            "illumination": true,
            "filename": "AbdA_00001_m_31_*",
            "landmarks": [17 elemts: {"x": x, "y": y}],
            "estimated_landmarks": [17 bools],
            "face_ROI": {"x": x, "y": y, "width": width, "height": height},
            "glasses_ROI": {"x": x, "y": y, "width": width, "height": height}
          }
        }
    ]

### Rename pascalVoc images
    python rename_pscalVoc_images.py <directory with pascalVoc annotations>
This script will rename images with annotations in pascalVoc format with numbers.  
Maybe it is useless but it makes dataset look prettier.
