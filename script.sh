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
roslaunch demo_keyframe_bundle_adjustment_meta kitti_standalone.launch



# delete workspace after this iteration is done
#sudo rm -r catkin_workspace

# roscore initialization DONE
# ros bag download and where to put it DONE
# make sure to do chmod 777 script.sh DONE
# instructions to install GA DONE
# params.yaml path may need to be modified in keyframs_ba_monolid.launch file - set to dynamic path DONE
# remove params file after one evaluation
# verify if launch file is reading parameters from params.yaml file - IMPORTANT
# add steps to install evo package to find fitness value DONE
# place ground truth file at proper destination /tmp/ DONE
# delete results folder after finding fitness value\ DONE
# install jq DONE



