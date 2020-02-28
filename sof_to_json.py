import json
import sys

from scipy.io import loadmat


# https://sites.google.com/view/sof-dataset


class Face_metadata:
    def __init__(self, metadata_obj):
        # this format sucks
        self.id = metadata_obj[0][0][0][0]
        self.seq = metadata_obj[1][0][0][0]
        self.gender = metadata_obj[2][0][0][0]
        self.age = int(metadata_obj[3][0][0])
        self.lightning = metadata_obj[4][0][0]
        self.view = metadata_obj[5][0][0]
        self.cropped = bool(metadata_obj[6][0][0])
        self.emotion = int(metadata_obj[7][0][0])
        self.year = int(metadata_obj[8][0][0])
        self.part = metadata_obj[9][0][0]
        self.glasses = int(metadata_obj[10][0][0])
        self.headscarf = bool(metadata_obj[11][0][0])
        self.illumination = bool(metadata_obj[16][0][0])
        self.filename = metadata_obj[17][0][0][0]
        self.landmarks = metadata_obj[12][0].astype(int).tolist()
        self.estimated_landmarks = metadata_obj[13][0].astype(bool).tolist()
        self.face_ROI = metadata_obj[14][0].astype(int).tolist()
        self.glasses_ROI = metadata_obj[15][0].astype(int).tolist()

    def to_json(self):
        return {
            "id": self.id,
            "sequence": self.seq,
            "gender": self.gender,
            "age": self.age,
            "lightning": self.lightning,
            "view": self.view,
            "cropped": self.cropped,
            "emotion": self.emotion,
            "year": self.year,
            "part": self.part,
            "glasses": self.glasses,
            "headscarf": self.headscarf,
            "illumination": self.illumination,
            "filename": self.filename,
            "landmarks": self.landmarks,
            "estimated_landmarks": self.estimated_landmarks,
            "face_ROI": self.face_ROI,
            "glasses_ROI": self.glasses_ROI
        }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pass path to .mat file and path to output .json file")
        exit(1)

    file = sys.argv[1]
    print("File:", file)
    out = sys.argv[2]
    print("Output:", out)

    json_data = []

    x = loadmat(file)
    for current_metadata in x["metadata"][0]:
        metadata = Face_metadata(current_metadata)
        json_data.append(metadata.to_json())

    with open(out, 'w') as outfile:
        json.dump(json_data, outfile, indent=2)
