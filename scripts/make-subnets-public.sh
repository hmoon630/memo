#!/bin/bash

subnetIds=$(aws ec2 describe-subnets --region us-west-1 --query "Subnets[].SubnetId" --output text)

for i in $subnetIds
do
    echo $i
    aws ec2 modify-subnet-attribute --map-public-ip-on-launch --subnet-id $i --region us-west-1
done
