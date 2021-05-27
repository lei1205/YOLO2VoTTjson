import json
import os
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()

pic_path = filedialog.askdirectory(title="Pictures Directory: ")
# get all pic filename
for pic_files in os.walk(pic_path):
    pass

# pic input check
pic_files[2].sort()
if pic_files == (pic_path, [], []):
    print("No Picture input!")
    exit()

txt_path = filedialog.askdirectory(title="txt Directory:")
#  get all txt filename
for txt_files in os.walk(txt_path):
    pass

# txt input check
txt_files[2].sort()
if txt_files == (txt_path, [], []):
    print("No txt input!")
    exit()

# 6 object types
raw_dict = {"frames": {}, "framerate": "1", "inputTags": "person,bicycle,tricycle,car,bus,truck",
            "tag_colors": ["#f409a2", "#ff4900", "#0ed29a", "#0500a6", "#32dc00", "#cac800"]}

# for all filename
for i in range(len(txt_files[2])):
    try:
        f = open(txt_files[0] + "/" + txt_files[2][i], 'r')
        s = f.read().split()
    except Exception as e:
        print("Please select correct txt directory!")
    # is txt is empty, skip
    if not s:
        continue

    pic_info = []
    xy_info = {}
    bbox_info = {"width": int(s[0]), "height": int(s[1])}

    # for all bounding boxes
    for i2 in range(int((len(s) - 1) / 5)):
        xy_info["x1"] = int(s[i2 * 5 + 3])
        xy_info["y1"] = int(s[i2 * 5 + 4])
        xy_info["x2"] = int(s[i2 * 5 + 5])
        xy_info["y2"] = int(s[i2 * 5 + 6])
        bbox_info["box"] = xy_info.copy()
        bbox_info["type"] = "rect"
        bbox_info["tags"] = [s[i2 * 5 + 2]]
        pic_info.append(bbox_info.copy())
    raw_dict["frames"][pic_files[2][i]] = pic_info

# white JSON
with open("./" + pic_path.split('/')[-1] + ".json", "w") as f:
    json.dump(raw_dict, f)
    print("Result saved as " + pic_path.split('/')[-1] + ".json")
