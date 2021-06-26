# BinaryMaskClassifier
Kernel SVM based 3D BinaryMask classifier
![image](https://user-images.githubusercontent.com/86521736/123514286-dc629080-d6af-11eb-8592-2f4f5e92b0d8.png)
The above figure shows the static view of the mask generator and classifier.

![image](https://user-images.githubusercontent.com/86521736/123514169-2008ca80-d6af-11eb-9530-9c12851ade47.png)
this figure shows the data flow between the different modules in BinaryMaskClassifier 

Please find description of the individual modules in the respective files.

Summary: 
Binary Masks are masks representing 3D objects. Usually they can be used to represent result of segmentation (separate the object and background) operation. These masks could have segmentation results of different tissues like the liver, heart, brain or vessels that carry fluids. Liver and Brain would be large objects while lung nodules could be small objects that are spread throughout the mask. The vessels would be objects that are thin and delineated.

The BinaryMaskClassifier creates example masks based on parametes set in the MaskParameters.csv file using the MaskFactory class. The MaskFactory class additionally adds data sampeles with augmentation that will increase the number of samples m for classification operation. 
The KernelSVM module inputs the feature vectors and classifies the data into 3 different classes.
