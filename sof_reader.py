import sys

from scipy.io import loadmat


# https://sites.google.com/view/sof-dataset


class Face_metadata:
    def __init__(self, metadata_obj):
        self.id = metadata_obj[0][0][0][0]
        self.seq = metadata_obj[1][0][0][0]
        self.gender = metadata_obj[2][0][0][0]
        self.age = metadata_obj[3][0][0]
        self.lightning = metadata_obj[4][0][0]
        self.view = metadata_obj[5][0][0]
        self.cropped = metadata_obj[6][0][0]
        self.emotion = metadata_obj[7][0][0]
        self.year = metadata_obj[8][0][0]
        self.part = metadata_obj[9][0][0]
        self.glasses = metadata_obj[10][0][0]
        self.headscarf = metadata_obj[11][0][0]
        self.illumination = metadata_obj[16][0][0]
        self.filename = metadata_obj[17][0][0][0]
        self.landmarks = metadata_obj[12][0]
        self.estimated_landmarks = metadata_obj[13][0]
        self.face_ROI = metadata_obj[14][0]
        self.glasses_ROI = metadata_obj[15][0]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass path to .mat file")
        exit(1)

    file = sys.argv[1]
    print("File:", file)

    x = loadmat(file)
    for current_metadata in x["metadata"][0]:
        metadata = Face_metadata(current_metadata)
        print(metadata.filename)

'''
    print("ID:", current_metadata[0][0][0][0])
    print("Sequence:", current_metadata[1][0][0][0])
    print("Gender:", current_metadata[2][0][0][0])
    print("Age:", current_metadata[3][0][0])
    print("Lightning:", current_metadata[4][0][0])
    print("View:", current_metadata[5][0][0])
    print("Is cropped:", current_metadata[6][0][0])
    print("Emotion:", current_metadata[7][0][0])
    print("Year:", current_metadata[8][0][0])
    print("Part:", current_metadata[9][0][0])
    print("Glasses type:", current_metadata[10][0][0])
    print("Wears headscarf:", current_metadata[11][0][0])
    print("Is illumination good:", current_metadata[16][0][0])
    print("Filename:", current_metadata[17][0][0][0])
    print("Landmarks:", current_metadata[12][0])
    print("Estimated landmarks:", current_metadata[13][0])
    print("Face ROI:", current_metadata[14][0])
    print("Glasses ROI:", current_metadata[15][0])
'''
