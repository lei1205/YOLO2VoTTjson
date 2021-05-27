# YOLO2VoTTjson
**YOLO2VoTTjson** is a tool to improve efficiency of object tagging.
## Prerequisite:
* **VoTT:**
  
  Please use [VoTT v1.7.2](https://github.com/microsoft/VoTT/releases/tag/v1.7.2).
  VoTT v2.0.0 and above use different JSON file. This script is not designed for that.

* `YOLO2VoTTjson.v1.py` is dependent on **tkinter**. 
  
  * If you are running python on Windows, generally speaking you don't need to install this package specifically.
  
  * For those who runing python on Ubuntu:
    ```       
    sudo apt-get update
    sudo apt-get install python3-tk
    ```         

  
* **To change default object type:**
  
  Please edit line 30

  ```
  # 6 object types
  raw_dict = {"frames": {}, "framerate": "1", "inputTags": "person,bicycle,tricycle,car,bus,truck",
            "tag_colors": ["#f409a2", "#ff4900", "#0ed29a", "#0500a6", "#32dc00", "#cac800"]}
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






