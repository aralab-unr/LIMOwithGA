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
#gnome-terminal --tab --command="roslaunch demo_keyframe_bundle_adjustment_meta kitti_standalone.launch;" --tab --command="rosbag play 04.bag --pause --clock;"
roslaunch demo_keyframe_bundle_adjustment_meta kitti_standalone.launch



# delete workspace after this iteration is done
#sudo rm -r catkin_workspace

# roscore initialization
# ros bag download and where to put it
# make sure to do chmod 777 script.sh
# instructions to install GA
# params.yaml path may need to be modified in keyframs_ba_monolid.launch file - set to dynamic path
# remove params file after one evaluation



