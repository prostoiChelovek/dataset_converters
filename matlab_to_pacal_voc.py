import sys

from pascal_voc_writer import Writer
from scipy.io import loadmat

# http://www.vision.caltech.edu/html-files/archive.html

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pass path to .mat file and path to dataset directory")
        exit(1)

    file = sys.argv[1]
    print("File:", file)
    directory = sys.argv[2]
    print("Output:", directory)

    x = loadmat(file)
    arr = x["SubDir_Data"]

    num = 1
    for i in range(0, len(arr[0])):
        cords = []  # x_bot_left y_bot_left x_top_left y_top_left, x_top_right y_top_right x_bot_right y_bot_right
        for j in range(0, len(arr)):
            cords.append(arr[j][i])

        writer = Writer(directory + "/images/" + str(num) + ".jpg", 896, 592)
        writer.addObject('Face', int(cords[2]), int(cords[3]), int(cords[6]), int(cords[7]))
        writer.save(directory + "/annotations/" + str(num) + ".xml")

        print(num)
        num += 1
