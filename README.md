# txt2vottjson

**txt2vottjson** is a tool to improve efficiency of object tagging.

1. Pre-Label: Get bounding boxes via YOLOv5 and save result in txt:

```
width
height
type(not type id) x_center y_center w h  
```

for example:

```
4000
3000
car 3252 1175 3873 1566 
car 2056 528 2188 650 
car 1937 650 2085 831 
car 2092 415 2186 491 
car 1974 346 2045 405 
car 1899 373 1973 444 
car 1862 330 1925 389 
car 1863 303 1919 349 
```

2. Save both image and txt in two separated directory
3. Run `txt2vottjson.py`
4. Move the JSON file just created to the same level of the image directory
5. Open the image directory with VoTT
6. Manually adjust some bounding boxes with errors



### Prerequisite:

Please use VoTT v1.7.2 https://github.com/microsoft/VoTT/releases/tag/v1.7.2

VoTT v2.0.0 and above use different JSON file. This script is not designed for that.

```bash
sudo apt-get update
sudo apt-get install python3-tk
```



### To change default object type:

Please edit line 31

```python
raw_dict = {"frames": {}, "framerate": "1", "inputTags": "person,bicycle,tricycle,car,bus,truck",
            "tag_colors": ["#f409a2", "#ff4900", "#0ed29a", "#0500a6", "#32dc00", "#cac800"]}
```



### Contributor: [Lei1205](https://github.com/lei1205)

