import glob
import sys
from os.path import join

from PIL import Image
from pascal_voc_writer import Writer

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Pass path to directory with .txt annotations and path to output directory and path to directory with "
              "images")
        exit(1)

    directory = sys.argv[1]
    print("Directory:", directory)
    output = sys.argv[2]
    print("Output:", directory)
    images_dir = sys.argv[3]
    print("Imaged directory:", images_dir)

    files = glob.glob(directory + "/*.txt")
    print("Found %i files" % len(files))

    for filename in files:
        file_path = join(directory, filename)
        file_id = file_path.split("/")[-1].split(".txt")[0]


        try:
            with open(file_path, 'r') as file:
                img = Image.open("{}/{}.jpg".format(images_dir, file_id))
                w, h = img.size

                writer = Writer(images_dir + "/" + str(file_id) + ".jpg", w, h)
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    data = line.split()

                    bbox_width = float(data[3]) * w
                    bbox_height = float(data[4]) * h
                    center_x = float(data[1]) * w
                    center_y = float(data[2]) * h

                    x_min = int(center_x - bbox_width / 2)
                    y_min = int(center_y - bbox_height / 2)
                    x_max = int(center_x + bbox_width / 2)
                    y_max = int(center_y + bbox_height / 2)

                    writer.addObject('Face', x_min, y_min, x_max, y_max)
                writer.save(output + "/" + str(file_id) + ".xml")
        except Exception as e:
            print("Skipping:", filename, ":", str(e))
