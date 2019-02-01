#!/bin/bash

# make a new ROS workspace to test the parameters
mkdir catkin_workspace
cd catkin_workspace
mkdir src
catkin_make
mkdir logs
catkin init
cd src
git clone https://github.com/adarshsehgal/LIMOwithGA
mv LIMOwithGA limo
cd limo
bash install_repos.sh
cd ..
cd ..
catkin_make
source devel_limo_release/setup.bash
roslaunch demo_keyframe_bundle_adjustment_meta kitti_standalone.launch



# delete workspace after this iteration is done
#sudo rm -r catkin_workspace

# roscore initialization
# 



