# Sea-Thru
Underwater Object Classification with YOLOv8

## Experiments and Results
### Data Preparation
To prepare the data for the object recognition network, a major obstacle is the need for bounding boxes. Since the turbulent dataset provided by Z. Li et al [2] does not include the corresponding bounding boxes, we had to manually map the bounding boxes to each image. In addition, there is a specific format of the bounding boxes that yolov8 needs, so we had written lots of util files for calculating the position of bounding boxes and copying them to the corresponding folders. It was then we created our GitHub repository for storing these files. 

Another difficulty we faced was the mapping of categories to each image. With the way ImageNet labels the classes, we had to write scripts that map the category code to stringed labels. We also excluded the categories that are uncommon underwater, else we would be passing around 1,000 categories for object recognition.

We then moved images out of their category folders for object recognition training. To avoid the duplication of images in the train images and test images, we split the categories into aquatic categories and non-aquatic categories. The aquatic categories are for testing, which would be part of the results evaluation. The non-aquatic categories are for training in both turbulence removal and object recognition.

### Experiments
We ran yolov8 4 times for different datasets. The first one is the ImageNet ground truth images, without any distortion for reference. The second one is the distorted images from Z. Li et al [2], where the network is trained from distorted images. For the third one, we removed turbulence in the distorted images by training with the DCGAN of Z. Li et al [2], then passed the results in yolov8 for training and recognizing objects in the images with their turbulent effects removed. For the fourth run, we first removed turbulence in the distorted images in the same dataset by training with the SA-GAN by T. Li et al [21]. We then trained the results in yolov8, as in the third run.

![image](https://github.com/typ00ytsa347/Sea-Thru/assets/79774614/4e1bb1fe-2454-4920-8de7-b9530b5de34b)

### Discussion
Looking at the PR curves in Fig. 15., the ground truth images have the best result for object recognition. This is expected because ground truth images do not have any distortion, and therefore do not have as much noise as would affect the result of object recognition. The second-best run, to our surprise, is the run trained from distorted images without any turbulence removal. The reason for this could be because the model is trained to recognize images with distortion, rather than being trained by ground truth images but tested on distorted images. The third-best run, the run of turbulence removal with SA-GAN, has very similar results to the run trained with distorted images. They perform quite a lot better than the run with DCGAN turbulence removal.

Without more information, we cannot say which algorithm performs better than the other, however, in the scenario of object recognition which is a possible task underwater aquatic robots will need to do, both algorithms don’t seem to perform better than passing raw distorted images. It could also be that the algorithms for turbulence removal resize the images to a smaller dimension. Note that there are still a lot of limitations as mentioned before. Currently, we do not have a highquality large underwater database for distorted images caused by underwater turbulence, and the requirement of having to transform each database to a specific format for each algorithm holds back a lot of potential.
