# limo

Lidar-Monocular Visual Odometry.
This library is designed to be an open platform for visual odometry algortihm development.
LIMO focuses explicitely on the simple integration of the following key methodologies:

* Keyframe selection
* Landmark selection
* Prior estimation
* Depth integration from different sensors.
* Scale integration by groundplane constraint.

The core library keyframe_bundle_adjustment is a backend that should faciliate to swap these modules and easily develop those algorithms.

* It is supposed to be an add-on module to do temporal inference of the optimization graph in order to smooth the result
* In order to do that online a windowed approach is used
* Keyframes are instances in time which are used for the bundle adjustment, one keyframe may have several cameras (and therefore images) associated with it
* The selection of Keyframes tries to reduce the amount of redundant information while extending the time span covered by the optimization window to reduce drift
* Methodologies for Keyframe selection:
  * Difference in time
  * Difference in motion

* This library is used for combining Lidar with monocular vision.
* Limo2 on KITTI is LIDAR with monocular Visual Odometry, supported with groundplane constraint.

## Details

limo reference: 
```shell
 https://github.com/johannes-graeter/limo
 ```

## Installation

### Requirements

In any case:

* ceres: 
  - follow the instructions on [http://ceres-solver.org/installation.html](http://ceres-solver.org/installation.html)
  - you will need ```sudo make install``` to install the headers.
  - tested with libsuitesparse-dev from standard repos.
* png++: 
```shell
 sudo apt-get install libpng++-dev
 ```
* install ros: 
  - follow the instructions on [https://wiki.ros.org/kinetic/Installation](https://wiki.ros.org/kinetic/Installation).
  - you will need to install ros-full (for pcl).
  - don't forget to source your ~/.bashrc afterwards.
* install catkin_tools: 
```shell 
sudo apt-get install python-catkin-tools
 ```
* install opencv_apps: 
```shell
sudo apt-get install ros-kinetic-opencv-apps
```
* install git: 
```shell
sudo apt-get install git
```
* install jq: 
```shell
sudo apt-get install jq
```
* install Genetic Algorithm (GA):
Follow the below github repository to install GA library 
```shell
https://github.com/chovanecm/python-genetic-algorithm
```
* groundtruth file: 
download groundtruth pose file from this github and place it in /tmp directory of your system
```shell
https://github.com/adarshsehgal/LIMOwithGA/blob/master/groundtruth_04.txt
```
* commands file: 
download commands and commands2 files from this github and place it in /tmp directory of your system
```shell
https://github.com/adarshsehgal/LIMOwithGA/blob/master/commands.txt
https://github.com/adarshsehgal/LIMOwithGA/blob/master/commands2.txt
```
* pose_check file: 
download pose_check and pose_check2 files from this github and place it in /tmp directory of your system
```shell
https://github.com/adarshsehgal/LIMOwithGA/blob/master/pose_check.py
https://github.com/adarshsehgal/LIMOwithGA/blob/master/pose_check2.py
```
* KITTI bag file: 
download KITTI bag file from below link and place it in /tmp directory of your system
```shell
https://www.mrt.kit.edu/graeterweb/04.bag
```
* install evo package: 
```shell
pip install evo --upgrade --no-binary evo
```
* install parallel package: 
```shell
sudo apt install parallel
```
* make sure scripts are accessible: 
```shell
sudo chmod 777 script.sh
sudo chmod 777 fitness_value_scipt.sh
```

### Run
* Follow these steps:
    1. Open `roscore`
    2. Download only below files to your computer to run the code, rest is taken care:
	```shell
       ga.py
       script.sh
       commands.txt
       commands2.txt
       pose_check.py
       pose_check2.py
       groundtruth_04.txt
       04.bag
       ```
    3. Run this command to start GA:
       ```shell
       python3 ga.py
       ```
* watch GA trying out different parameter values and limo traces the trajectory in rviz :)

## Known issues
* Unittest of LandmarkSelector.voxel fails with libpcl version 1.7.2 or smaller (just 4 landmarks are selected). 
Since this works with pcl 1.8.1 which is standard for ros melodic, this is ignored. This should lower the performance of the software only by a very small amount.
