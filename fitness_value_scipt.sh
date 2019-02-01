#!/bin/bash

cd /tmp
mkdir results
evo_ape kitti groundtruth_04.txt poses_dump.txt -va --plot_mode xz --save_results results/fitness.zip
cd results
unzip fitness.zip -d fitness
cd fitness
val=( $(jq '.rmse' stats.json))
echo $val
cd ..
cd ..
rm -r results



