#!/bin/bash

echo "args = ${0} ${1} ${2}"

if [ $# -ge 4 ]; then
    ENABLE_DEBUG=${1^^}
fi

if [ $# -ge 3 ]; then
    ENABLE_PATH_LOG=${1^^}
    DIR_LIST_FILE=${2}
elif [ $# -ge 2 ]; then
    ENABLE_PATH_LOG=${1^^}
fi

TARGET_PATH=".."
TARGET_PROJECT="Project_C"
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

OS_NAME=`uname`

if [ "$OS_NAME" = "Darwin" ]; then
    EXECUTE_FILE="main_for_mac"
    MAKE_COMMAND="make"

elif [ "$OS_NAME" = "Linux" ]; then
    EXECUTE_FILE="main_for_linux"
    MAKE_COMMAND="make"

else
    EXECUTE_FILE="main_for_linux"
    MAKE_COMMAND="make"

fi

if [ "$ENABLE_DEBUG" = "TRUE" ]; then
    MAKE_COMMAND="$MAKE_COMMAND debug"

fi

for target in "${LIST[@]}" ; do
    target=${target/../$PARRENT_PATH}
    echo "${target}"
    cd "${target}"

    ## Rebuild ##
    $MAKE_COMMAND

    ## Execute ##
    ./$EXECUTE_FILE ../testdata.txt

    if [ "${LOGFILE}" != "" ]; then
        echo `pwd` >> ${LOGFILE}
    fi

  # read
done

cd $START_PATH
