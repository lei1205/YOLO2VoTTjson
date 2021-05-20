import os
import sys
import cv2
import json

argument = sys.argv[1:]
print(len(argument))
if len(argument) < 2 or len(argument) > 3:
    print("Example: python test.py ./pic/ ./txt/ ./pic.json")
    sys.exit(1)
elif len(argument) == 2:
    pic_dir = argument[0]
    txt_dir = argument[1]
    json_des = argument[0].split('/')[1] + ".json"
elif len(argument) == 3:
    pic_dir = argument[0]
    txt_dir = argument[1]
    json_des = argument[2]
print(pic_dir,txt_dir,json_des)

# get all pic filename
pic_filelists = os.listdir(pic_dir)
if pic_filelists == []:
    print("No Picture input!")
    exit()
# get all txt filename
txt_filelists = os.listdir(txt_dir)
if txt_filelists == []:
    print("No txt input!")
    exit()

# 8 object types
index = {0:"Heavy-Vehicle",1:"Midsize-Vehicle",2:"Compact-Vehicle",3:"Car",4:"None-Vehicle",5:"Pedestrian",6:"Large-Bus",7:"Light-Bus"}
raw_dict = {"frames": {}, "framerate": "1", "inputTags": "Heavy-Vehicle,Midsize-Vehicle,Compact-Vehicle,Car,None-Vehicle,Pedestrian,Large-Bus,Light-Bus",
            "tag_colors": ["#0ce28f","#950bb1","#0017ff","#39a400","#c53f00","#c2f20c","#2c009b","#008acb"]}
    
# for all filename
for file in txt_filelists:    
    
    try:
        print('Reading ' + file.split('.txt')[0])
        f = open(txt_dir + file, 'r')
        s = f.read().split()
        image = cv2.imread(pic_dir + file.split('.txt')[0] + '.jpg')
        size = image.shape
        w = size[1]
        h = size[0]
    except Exception as e:
        print("Make sure txt and pic is corresponding!")
        sys.exit()
    # if txt is empty, skip
    if not s:
        continue

    pic_info = []
    xy_info = {}
    bbox_info = {"width": int(w), "height": int(h)}
    # for all bounding boxes
    for i2 in range(int(len(s)/5)):
        t1 = float(s[i2 * 5 + 1])
        t2 = float(s[i2 * 5 + 2])
        t3 = float(s[i2 * 5 + 3])
        t4 = float(s[i2 * 5 + 4])
        xy_info["x1"] = int((t1*int(w)*2-t3*int(w))/2)
        xy_info["y1"] = int((t2*int(h)*2-t4*int(h))/2)
        xy_info["x2"] = int((t1*int(w)*2+t3*int(w))/2)
        xy_info["y2"] = int((t2*int(h)*2+t4*int(h))/2)
        bbox_info["box"] = xy_info.copy()
        bbox_info["type"] = "rect"
        bbox_info["tags"] = [index[int(s[i2 * 5])]]
        pic_info.append(bbox_info.copy())
    raw_dict["frames"][file.split('.txt')[0] + '.jpg'] = pic_info

# white JSON
with open(json_des, "w") as f:
    json.dump(raw_dict, f)
    print("Result saved as " + json_des)
