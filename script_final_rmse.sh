#!/bin/bash

# make a new ROS workspace to test the parameters
cd /tmp
mkdir catkin
cd catkin
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
rosclean purge -h
source devel_limo_release/setup.bash
cd ..

# LIMO with rosbag to generate estimate poses
echo "Running LIMO with rosbag..."
# 4705 - sequence 00
# 1142 - sequence 01
# 293 - sequence 04
timeout -k 4705 1 parallel < commands_final_rmse.txt --no-notice 

# delete workspace after this iteration is done
cd /tmp
rm -r -f catkin

mv poses_dump.txt poses_dump_00.txt






