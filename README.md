# YOLO2VoTTjson
**YOLO2VoTTjson** is a tool to improve efficiency of object tagging.
## Prerequisite:
* **VoTT:**
  
  Please use [VoTT v1.7.2](https://github.com/microsoft/VoTT/releases/tag/v1.7.2).
  VoTT v2.0.0 and above use different JSON file. This script is not designed for that.

* **`YOLO2VoTTjson.v2.py`** is dependent on **opencv-python**.
  
  ```
  pip install opencv-python
  ``` 

* `YOLO2VoTTjson.v1.py` is dependent on **tkinter**. 
  
  * If you are running python on Windows, generally speaking you don't need to install this package specifically.
  
  * For those who runing python on Ubuntu:
    ```       
    sudo apt-get update
    sudo apt-get install python3-tk
    ```         

## YOLO2VoTTjson V2
**`YOLO2VoTTjson.v2.py`** no longer needs special formatted txt. Raw YOLO txt is allowed.
* **Run:**
  
  Save pictures and txt in two separated folders. Then run the script with command like this：
  ```
  python YOLO2VoTTjson.v2.py ./pic/ ./txt/ ./pic.json
  ```
  Note that make sure the end "/" is included. 
  
  The last parameter is optional. If ignored json file will be saved along with `YOLO2VoTTjson.v2.py`. 

* **For VoTT to read json:**
  
  You should put the json file, which has same filename as the picture folder, in the same level directory with the picture folder.
  
  
* **To change default object type:**
  
  Please edit line 32

  ```
  # 8 object types
  index = {0:"Heavy-Vehicle",1:"Midsize-Vehicle",2:"Compact-Vehicle",3:"Car",4:"None-Vehicle",5:"Pedestrian",6:"Large-Bus",7:"Light-Bus"}
  raw_dict = {"frames": {}, "framerate": "1", "inputTags": "Heavy-Vehicle,Midsize-Vehicle,Compact-Vehicle,Car,None-Vehicle,Pedestrian,Large-Bus,Light-Bus",
            "tag_colors": ["#0ce28f","#950bb1","#0017ff","#39a400","#c53f00","#c2f20c","#2c009b","#008acb"]}
  ```

## YOLO2VoTTjson V1 (Not Recommended)

1. Pre-Label: Get bounding boxes via YOLO and save result in txt with **special format** like this:

            
        width
        height
        type(not type id) x1 y1 x2 y2 
            

   For example:
   
            
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
            

2. Save pictures and txt in two separated folders
3. Run `YOLO2VoTTjson.v1.py`
4. Move the JSON file just created to the same level of the picture folder
5. Open the picture folder with VoTT






