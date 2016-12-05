#!/bin/bash

FILENAME=$1
TEST_LINE=$2
BATCH_LINE=$3

TB_LINE=`expr ${TEST_LINE} + ${BATCH_LINE}`
echo $TB_LINE
head -n ${TEST_LINE} ${FILENAME} > ${FILENAME}.test
head -n ${TB_LINE} ${FILENAME} | tail -n ${BATCH_LINE} > ${FILENAME}.batch
ALL_LINE=$(wc -l ${FILENAME} | awk '{print $1}')
echo $ALL_LINE
TRAIN_LINE=`expr ${ALL_LINE} - ${TB_LINE}`
echo $TRAIN_LINE
tail -n ${TRAIN_LINE} ${FILENAME} > ${FILENAME}.train
echo finisjes
