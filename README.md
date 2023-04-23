# Drowsiness Detection System


# Abstract

<p>
  This project is a real-time drowsiness detection system used to detect fatigue among drivers and alert them. This system uses computer vision for image pre processing, machine learning for object (face and eye) detection using cascade classifiers and a Convolutional Neural Networks model for classification. 
</p>

# Tech Used 
<ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://jupyter.org/">Jupyter Notebook</a></li>  
</ul>

# Dataset used
<p> <a href="https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new">Yawn_Eye_Dataset_New </a> </p>
<p> You can use any other dataset that contains images of closed and open eyes </p>

# Cascade Classifiers
<p> Haar cascade is a ML based object detection algorithm, and was used in this project to detect face and eyes 
Link of the files used
<li><a href="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml">To detect face</a></li>
<li><a href="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_lefteye_2splits.xml">To detect left eye</a></li>
<li><a href="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_righteye_2splits.xml">To detect right eye</a></li>
</p


# Installation and Execution
<ol>
    <li>Clone the repository. </li>
    <li>Go to the directory where repository was saved</a> </li>
    <li>Download the above dataset or any other dataset and paste it in the same directory</li>
    <li>Either rename the dataset as YawnDS or modify the code</li>
    <li>Run the model.py file to train the model. Adjust the parameters as per your convenience</li>
    <li>After the model is trained, open the terminal in that director and type "GUI.py" or "new drowsiness detection.py"</li>
</ol>
