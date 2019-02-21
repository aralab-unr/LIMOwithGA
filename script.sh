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
source devel_limo_release/setup.bash
cd ..

# LIMO with rosbag to generate estimate poses
echo "Running LIMO with first rosbag..."
# 1142 - sequence 01
# 293 - sequence 04
timeout -k 293 1 parallel < commands2.txt --no-notice 

# delete workspace after this iteration is done
cd /tmp
rm -r -f catkin

# check if poses dump have equal poses as in ground truth
python3 /tmp/pose_check2.py

# find fitness value by using evo package and comparing with ground truth
mkdir results
evo_ape kitti groundtruth_04.txt poses_dump.txt -va --plot_mode xz --save_results results/fitness.zip
cd results
unzip fitness.zip -d fitness
cd fitness
val=( $(jq '.rmse' stats.json))
echo $val >> /tmp/rmse_output2.txt
cd ..
cd ..
rm -r -f results

# Running LIMO with second rosbag

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
source devel_limo_release/setup.bash
cd ..

# LIMO with rosbag to generate estimate poses
echo "Running LIMO with second rosbag..."
# 1142 - sequence 01
# 293 - sequence 04
timeout -k 1142 1 parallel < commands.txt --no-notice 

# delete workspace after this iteration is done
cd /tmp
rm -r -f catkin

# check if poses dump have equal poses as in ground truth
python3 /tmp/pose_check.py

# find fitness value by using evo package and comparing with ground truth
mkdir results
evo_ape kitti groundtruth_01.txt poses_dump.txt -va --plot_mode xz --save_results results/fitness.zip
cd results
unzip fitness.zip -d fitness
cd fitness
val=( $(jq '.rmse' stats.json))
echo $val >> /tmp/rmse_output1.txt
cd ..
cd ..
rm -r -f results




