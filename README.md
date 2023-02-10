# YOLO2VoTTjson
**YOLO2VoTTjson** is a tool to improve efficiency of object tagging.
## Prerequisite:

Please use [VoTT v1.7.2](https://github.com/microsoft/VoTT/releases/tag/v1.7.2).
  
VoTT v2.0.0 and above use different JSON file. This script is not designed for that.

**`YOLO2VoTTjson.py`** is dependent on **opencv-python**.
  
```
pip install opencv-python
``` 
    

## YOLO2VoTTjson V2 Instruction
**`YOLO2VoTTjson.py`** needs Raw YOLO txt.

**Run:**
  
Save pictures and txt in two separated folders. Then run the script with command like this：

picture folder, yolo txt folder, json file destination (optional)
```
python YOLO2VoTTjson.v2.py ./pic ./txt ./pic.json
```
  
The last parameter is optional. If ignored json file will be saved along with `YOLO2VoTTjson.py`. 

**For VoTT to read json:**
  
You should put json file, which has same filename as the picture folder, in the same level directory with the picture folder.
  
  
**To change default object type:**
  
Please edit line 32

```
# 8 object types
index = {0:"CarType0",1:"CarType1",2:"CarType2",3:"CarType3",4:"CarType4",5:"CarType5",6:"CarType6",7:"CarType7"}
raw_dict = {"frames": {}, "framerate": "1", "inputTags": "CarType0,CarType1,CarType2,CarType3,CarType4,CarType5,CarType6,CarType7",
          "tag_colors": ["#0ce28f","#950bb1","#0017ff","#39a400","#c53f00","#c2f20c","#2c009b","#008acb"]}
```


