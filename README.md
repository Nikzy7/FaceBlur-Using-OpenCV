# FaceBlur Using OpenCV [![Made with Python](https://img.shields.io/badge/python-3.5.2-grey?style=for-the-badge&labelColor=yellow&logo=python)](https://www.python.org/)<br>
This Mini Project uses OpenCV face detector and Blur capabilities to create a facial blur application. Feel free to use, share or modify this project. I'll be really happy to see what you can build upon these mini-projects.

## Installing the dependencies of this project
Please keep in mind that this project was made on a Windows 10 PC having Python 3.8.5, therefore, the requirements.txt file will have frozen requirements for Python 3.8.5. However, the only major requirement of this project is a proper installation of OpenCV. If you are running a similar or newer version of python, hit the following command in your command prompt.

    pip install -r requirements.txt
    
If you are running some other version of Python go ahead and write the following command in your command prompt.

    pip install opencv-python opencv-contrib-python

That should clear the dependency part.

## Step By Step explanation of working of this project:
* The program starts by checking the command line argument provided by the user to determine which type of blur is to be applied. If no arguments or wrong arguments are provide, a try block will print the error message and close the program.
* After the determination of the type of blur, a while loop (infinity loop) is instantiated that captures a frame from the webcam.
* The frame is scaled down to its 80% and the presence of faces is detected using the HaarCascade Face detection of OpenCV.
* Upon getting the coordinates of all the faces present in the frame, the selected type of blur is applied on those areas of the image and then displayed on the screen.
* Upon pressing "q", the loop terminates.

## Running this project
Follow the instructions below:
   * Clone the repository:
            
          git clone https://github.com/Nikzy7/FaceBlur-Using-OpenCV
   * Get into the cloned repo:
   
          cd FaceBlur-Using-OpenCV-master
   * For gaussian blur (Windows 10):
   
          python face-blur.py gaussian
   * For pixelated blur (Windows 10):
   
          python face-blur.py pixelate
          
## Results
### For Gaussian Blur
<p align="center">
<img src="gaussian_result.gif" width="450" height="350">
</p>

### For Pixelated Blur
<p align="center">
<img src="pixelate_result.gif" width="450" height="350">
</p>
