#!/bin/bash

dirs=(
  "./0001_0099/"
  "./0100_0199/"
  "./0200_0299/"
  "./0300_0399/"
  "./0400_0499/"
  "./0500_0599/"
  "./0600_0699/"
  "./0700_0799/"
  "./0800_0899/"
  "./0900_0999/"
  "./1000_1099/"
  "./1100_1199/"
  "./1200_1299/"
  "./1300_1399/"
  "./1400_1499/"
  "./1500_1599/"
  "./1600_1699/"
  "./1700_1799/"
  "./1800_1899/"
  "./1900_1999/"
  "./2000_2099/"
  "./2100_2199/"
)

total=0
for dir in ${dirs[@]}; do
  count=`ls -alRd ${dir}* | wc -l`
  printf "${dir}* = $count\n"
  total=$(($total+$count))
done

printf "total = $total\n"
