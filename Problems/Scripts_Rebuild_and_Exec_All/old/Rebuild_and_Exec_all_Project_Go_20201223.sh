#!/bin/bash

echo "args = ${0} ${1} ${2}"

if [ $# -ge 3 ]; then
    ENABLE_PATH_LOG=${1^^}
    DIR_LIST_FILE=${2}
elif [ $# -ge 2 ]; then
    ENABLE_PATH_LOG=${1^^}
fi

TARGET_PATH=".."
TARGET_PROJECT="Project_Go"
START_PATH=`pwd`
BASENAME=`basename \`pwd\``
PARRENT_PATH=${START_PATH/$BASENAME//}
PARRENT_PATH=${PARRENT_PATH/\/\//}

echo "TARGET_PATH = $TARGET_PATH"
echo "PARRENT_PATH = $PARRENT_PATH"
echo "BASENAME = $BASENAME"

IFS=$'\n'
if [ "$DIR_LIST_FILE" != "" -a -f "$DIR_LIST_FILE" ]; then
    LIST=(`cat $DIR_LIST_FILE`)
else
    LIST=(`find $TARGET_PATH -type d | grep $TARGET_PROJECT$ | sort`)
fi

if [ "$ENABLE_PATH_LOG" = "TRUE" ]; then
    TIMESTAMP=`date +%Y%m%d_%H%M%S`
    LOGFILE=${START_PATH}/log/${TARGET_PROJECT}_${TIMESTAMP}.log
    touch ${LOGFILE}
fi

echo "ENABLE_PATH_LOG = $ENABLE_PATH_LOG"
echo "DIR_LIST_FILE = $DIR_LIST_FILE"
echo "LOGFILE = $LOGFILE"

for target in "${LIST[@]}" ; do
    target=${target/../$PARRENT_PATH}
    echo "${target}"
    cd "${target}"

    ## Rebuild and Execute ##
    go run main.go ../testdata.txt

    if [ "${LOGFILE}" != "" ]; then
        echo `pwd` >> ${LOGFILE}
    fi

  # read
done

cd $START_PATH

