## Writeup 

---

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Normalize the features extracted from the previous steps
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./examples/car_not_car.png
[image2]: ./examples/HOG_feature.png
[image11]: ./examples/HOG_feature_notcar.png
[image3]: ./examples/sliding_window.png
[image4]: ./examples/sliding_window_search_result.png
[image5]: ./examples/bboxes_and_heat_1.png
[image6]: ./examples/labels_map.png
[image7]: ./examples/output_bboxes.png
[image8]: ./examples/bboxes_and_heat_2.png
[image9]: ./examples/bboxes_and_heat_3.png
[image10]: ./examples/bboxes_and_heat_4.png
[video1]: ./output_videos/project_video_output.mp4

---
### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the sixth and seventh code cells of the IPython notebook.

I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][image1]

I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=8`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:

![alt text][image2]
![alt text][image11]

#### 2. Explain how you settled on your final choice of HOG parameters.

I tried various combinations of parameters. For the HOG parameters, the combination of `YCrCb`, `orientations=9`, `pixels_per_cell=(8,8)`, and `cells_per_block=(2,2)` gives a nice result in the SVM training score. Besides HOG features, I alse concatenate the color histogram feature and original pixel values to the feature set. My experimental result indicates "HLS" gives the best result becuase the vehicle color satuation is separated in the "L" channel. To reduce the size of feature set for speed up traning, I resize each training picture to 16x16 in the SVM training step. You can find this step at the ninth code block in the Ipython Notebook.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM using color features and HOG features. The code is in the ninth code block in the Ipython Notebook. I first extracted color features and hog features from "car" pictures and "notcar" pictures using the parameters obtained from the experiment and function written before. Then, I stacked the features together and used "StandardScaler()" from Sklearn package to normalize the extracted features. I also splited the data into training set and validation set and shuffle them. After this, I used GridSearchCV to find the best parameter combination used for SVM (Kernel:'linear', C:0.1). aFTER, I trained the SVM using training dataset and validate my SVM using the validation dataset. The final score obtained by this linear SVM model is 0.998.

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

I use different sliding window sizes and manually choose them based on the rule that the far windows should be smaller than the closer windows. I use sizes of the cars in the test image as the reference when choosing the window size. 

![alt text][image3]

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Ultimately I searched using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.  Here are some example images:

![alt text][image4]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./output_videos/project_video_output.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  

Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:

##### Here are 4 frames and their corresponding heatmaps:

![alt text][image5]
![alt text][image8]
![alt text][image9]
![alt text][image10]

##### Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap from all six frames:
![alt text][image6]

##### Here the resulting bounding boxes are drawn onto the last frame in the series:
![alt text][image7]

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

I used color feature and gradient feature(HOG) to train a SVM model to detect vehicles. I generated sliding windows of different size to capture vehicle pixels in each video image. I used heat map, a threshold, and a consecutive serie of images to eliminate false positive. I used sklean.label to separate vehicles and remove duplicates. 
One thing I can improve here is the label function. When two vehicle overide each other, the current algorithm won't be able to distinguish them. I think I might include a vehicle locking mechanism and train the svm to know this situation. 
Another thing there is the sliding window part, I think I can scale the window using a coefficient which is proportional to the distance from possible vehicle positions to the image bottom line.
I am improving my advanced lane detection pipeline. If I can get the revised version work, I will add the lane line and predicted curvature to this project.

### Acknowledgement 
* Udacity Self-Driving Car Nano Degree
* GTI vehicle image database
* KITTI vision benchmark suite
* Udacity dataset
