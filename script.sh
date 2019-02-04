#!/bin/bash

# make a new ROS workspace to test the parameters
cd /tmp
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
#roslaunch demo_keyframe_bundle_adjustment_meta kitti_standalone.launch
cd ..
echo "Running LIMO with rosbag..."
timeout 293 parallel < commands.txt --no-notice 

# delete workspace after this iteration is done
cd /tmp
rm -r -f catkin_workspace

# find fitness value by using evo package and comparing with ground truth
mkdir results
evo_ape kitti groundtruth_04.txt poses_dump.txt -va --plot_mode xz --save_results results/fitness.zip
cd results
unzip fitness.zip -d fitness
cd fitness
val=( $(jq '.rmse' stats.json))
echo $val >> /tmp/rmse_output.txt
cd ..
cd ..
rm -r -f results

# add other parameters to GA




