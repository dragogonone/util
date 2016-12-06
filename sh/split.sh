#!/bin/bash

if [ $# -ne 2 ]; then
echo "Usage: this FILENAME LINE"
exit 1
fi

FILENAME=$1
LINE_1=$2

head -n ${LINE_1} ${FILENAME} > ${FILENAME}.1

LINE_FILE=$(wc -l ${FILENAME} | awk '{print $1}')
echo ${LINE_FILE}
LINE_2=`expr ${LINE_FILE} - ${LINE_1}`
tail -n ${LINE_2} ${FILENAME} > ${FILENAME}.2
