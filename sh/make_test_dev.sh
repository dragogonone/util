#!/bin/bash

FILENAME=$1
TEST_LINE=$2
DEV_LINE=$3

TB_LINE=`expr ${TEST_LINE} + ${DEV_LINE}`
head -n ${TEST_LINE} ${FILENAME} > ${FILENAME}.test
echo test ${TEST_LINE}

head -n ${TB_LINE} ${FILENAME} | tail -n ${DEV_LINE} > ${FILENAME}.dev
echo batch ${DEV_LINE}

ALL_LINE=$(wc -l ${FILENAME} | awk '{print $1}')
TRAIN_LINE=`expr ${ALL_LINE} - ${TB_LINE}`
tail -n ${TRAIN_LINE} ${FILENAME} > ${FILENAME}.train
echo train ${TRAIN_LINE}

echo finished
