# saveimg

Command line utility to create image datasets from webcam feed or from Video files.

## Installation

- Install from pip using ```pip install mkdataset```

- Clone the repo and install using ```python setup.py install```

---

## Usage:

```
$$ saveimg
Usage: saveimg [OPTIONS] NAME
Try "saveimg --help" for help.

Error: Missing argument "NAME".
```
---
```
$$ saveimg --help
Usage: saveimg [OPTIONS] NAME

  Capture frame from video feed at set intervals and save them as an
  organized dataset with  images in training, test and validation folders

  Currently supports only for one class name

Options:
  -d, --directory PATH            Directory where images has to be saved,
                                  expects path not string
  -v, --video FILENAME            Video file to parse, default is webCam feed
  -s, --fps INTEGER               Capture rate in seconds per Frame
  -p, --distribution <FLOAT FLOAT FLOAT>...
                                  Distribution of train, test and valid images
                                  to be saved
  -c, --cont BOOLEAN              If train, test and validation images should
                                  have continuity in naming
  -r, --reverse BOOLEAN           If train, test and validation should be
                                  inside class folder unlike class folder
                                  inside these
  --help                          Show this message and exit.

$$
```
---
```
$$ saveimg test_class
---------------------------------------------------------------------------------
        Directory is D:\venvs\saveimg

        Saving image every 1 seconds

        Saving train, test and validation in ratio of (0.6, 0.2, 0.2)

        Reading video feed from Webcam
---------------------------------------------------------------------------------
Please enter to proceed :  [True]: n

```
---

```
$$ saveimg test_class
---------------------------------------------------------------------------------
        Directory is D:\venvs\saveimg

        Saving image every 1 seconds

        Saving train, test and validation in ratio of (0.6, 0.2, 0.2)

        Reading video feed from Webcam
---------------------------------------------------------------------------------
Please enter to proceed :  [True]: y
Saved D:\venvs\saveimg\train\test_class\test_class_1.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_2.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_3.jpg
---------
Saved D:\venvs\saveimg\validation\test_class\test_class_1.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_4.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_5.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_6.jpg
---------
Saved D:\venvs\saveimg\validation\test_class\test_class_2.jpg
---------
Saved D:\venvs\saveimg\train\test_class\test_class_7.jpg

Aborted!
[ WARN:0] global C:\projects\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (674) SourceReaderCB::~SourceReaderCB terminating async callback

$$

```

---

```
$$ saveimg -d D:\venvs -p 0.7 0.15 0.15 label1
---------------------------------------------------------------------------------
        Directory is D:\venvs

        Saving image every 1 seconds

        Saving train, test and validation in ratio of (0.7, 0.15, 0.15)

        Reading video feed from Webcam
---------------------------------------------------------------------------------
Please enter to proceed :  [True]: n
```

---

Notice that image numbers are continuous
```
$$ saveimg -d D:\venvs -p 0.4 0.3 0.3 -c y label
---------------------------------------------------------------------------------
        Directory is D:\venvs

        Saving image every 1 seconds

        Saving train, test and validation in ratio of (0.4, 0.3, 0.3)

        Reading video feed from Webcam
---------------------------------------------------------------------------------
Please enter to proceed :  [True]:
Saved D:\venvs\train\label\label_0.jpg
---------
Saved D:\venvs\train\label\label_1.jpg
---------
Saved D:\venvs\train\label\label_2.jpg
---------
Saved D:\venvs\train\label\label_3.jpg
---------
Saved D:\venvs\test\label\label_4.jpg
---------
Saved D:\venvs\train\label\label_5.jpg
---------
Saved D:\venvs\validation\label\label_6.jpg
---------
Saved D:\venvs\train\label\label_7.jpg
---------
Saved D:\venvs\test\label\label_8.jpg
---------
Saved D:\venvs\train\label\label_9.jpg
---------
Saved D:\venvs\train\label\label_10.jpg
---------
Saved D:\venvs\validation\label\label_11.jpg
---------
Saved D:\venvs\test\label\label_12.jpg
---------
Saved D:\venvs\validation\label\label_13.jpg

Aborted!
[ WARN:0] global C:\projects\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (674) SourceReaderCB::~SourceReaderCB terminating async callback

$$
```
---
Train, test and validation inside image_label folder
```
$$ saveimg -d D:\venvs -p 0.4 0.3 0.3 -r y image_label
---------------------------------------------------------------------------------
        Directory is D:\venvs

        Saving image every 1 seconds

        Saving train, test and validation in ratio of (0.4, 0.3, 0.3)

        Reading video feed from Webcam
---------------------------------------------------------------------------------
Please enter to proceed :  [True]:
Saved D:\venvs\image_label\validation\image_label_1.jpg
---------
Saved D:\venvs\image_label\train\image_label_1.jpg
---------
Saved D:\venvs\image_label\validation\image_label_2.jpg
---------
Saved D:\venvs\image_label\validation\image_label_3.jpg
---------
Saved D:\venvs\image_label\test\image_label_1.jpg
---------
Saved D:\venvs\image_label\test\image_label_2.jpg
---------
Saved D:\venvs\image_label\validation\image_label_4.jpg

Aborted!
[ WARN:0] global C:\projects\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (674) SourceReaderCB::~SourceReaderCB terminating async callback

$$
```
