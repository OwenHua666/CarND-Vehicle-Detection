# Vehicle Detection

In this project, my goal is to write a software pipeline to detect vehicles in a video (start with the test_video.mp4 and later implement on full project_video.mp4). I created a detailed writeup for this project, which is also in the Github repo.

The Project
---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Normalize the features obtained from the previous feature-extraction processes
* Implement a sliding-window technique and use my trained classifier to search for vehicles in images.
* Run my pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

Here are links to the labeled data for [vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/vehicles.zip) and [non-vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/non-vehicles.zip) examples to train your classifier.  These example images come from a combination of the [GTI vehicle image database](http://www.gti.ssr.upm.es/data/Vehicle_database.html), the [KITTI vision benchmark suite](http://www.cvlibs.net/datasets/kitti/), and examples extracted from the project video itself.   You are welcome and encouraged to take advantage of the recently released [Udacity labeled dataset](https://github.com/udacity/self-driving-car/tree/master/annotations) to augment your training data.  

You can find some example images in the processing pipeline in the example folders. The output videos and images are in the corresponding output folder.

### Prerequisites

What things you need to install the software and how to install them

```
Udacity Carnd-term1 conda package
```
### Running

You can check my output video or use the jupyter notebook to processing your own videos. 

### Author

**Yiwen(Owen).Hua** - *Initial work* - [OwenHua666](https://github.com/OwenHua666)

## Acknowledgments

* Udacity Self-Driving Car Nanodegree
* Opencv
* Matplotlib
* Pickle
* ...

