#!/bin/sh

if [ $# -lt 1 ]; then
	echo "invalid parms,must need 1 of config file"
	exit;
fi

CONFIG_FILE=$1
#校验配置文件
if [ ! -f $CONFIG_FILE ]; then
	echo "config file is not exist"
	exit
fi
. ${CONFIG_FILE}

#校验参数
params_invide=0
if [ -z "${DATA_PATH}" ]; then
	params_invide=1
fi
if [ -z "${FILE_PREFIX}" ]; then
	params_invide=1
fi
if [ -z "${LOG_USER}" ]; then
	params_invide=1
fi
if [ -z "${HDFS_CONFIG_DIR}" ]; then
	params_invide=1
fi
if [ -z "${BAK_PATH}" ]; then
	params_invide=1
fi
if [ -z "${BAK_DAY}" ]; then
	params_invide=1
fi
if [ -z "${HADOOP_HOME}" ]; then
	params_invide=1
fi
if [ -z "${HDFS_ROOT_PATH}" ]; then
	params_invide=1
fi
if [ -z "${NOTIFY_PHONES}" ]; then
	params_invide=1
fi

if [ $params_invide -eq 1 ]; then
	echo "fail config file"
	exit
fi

if [ ! -d ${BAK_PATH} ]; then
	chown -R ${LOG_USER}:${LOG_USER} ${BAK_PATH}
fi

BAK_PATH_WORK=${BAK_PATH}/WORK
if [ ! -d ${BAK_PATH_WORK} ]; then
	mkdir -p ${BAK_PATH_WORK}
	chown -R ${LOG_USER}:${LOG_USER} ${BAK_PATH_WORK}
fi

BAK_PATH_BAK=${BAK_PATH}/BAK
if [ ! -d ${BAK_PATH_BAK} ]; then
	mkdir -p ${BAK_PATH_BAK}
	chown -R ${LOG_USER}:${LOG_USER} ${BAK_PATH_BAK}
fi

BAK_PATH_WORK_LOG=${BAK_PATH_WORK}/LOG
if [ ! -d ${BAK_PATH_WORK_LOG} ]; then
	mkdir -p ${BAK_PATH_WORK_LOG}
	chown -R ${LOG_USER}:${LOG_USER} ${BAK_PATH_WORK_LOG}
fi

RUN_HOME=$(cd "$(dirname "$0")";echo "${PWD%}")
DELEDATE="`date -d $BAK_DAY' day ago' +%Y%m%d`"

echo "DELEDATE":${DELEDATE}

#IP=`/usr/sbin/ifconfig |grep "192.168.1" |awk '{print $2}'`
IP=`hostname -i`


/usr/local/bin/python /home/qingniu/hainiu_crawler/download_page/util/html_merge_util.py

INPUT_FILES=`ls ${DATA_PATH}/*.done`

for FILE in $INPUT_FILES
do
	TIMESTAMP="`date -d 5' mins ago' +%Y%m%d%H%M%S`"
	DES_LOG_FILE=${FILE_PREFIX}_${IP}_${TIMESTAMP}.log
	echo "${DES_LOG_FILE}"
	
	mv ${FILE} ${BAK_PATH_WORK}/${DES_LOG_FILE}
	#cp ${FILE} ${BAK_PATH_WORK}/${DES_LOG_FILE}

	/usr/bin/gzip ${BAK_PATH_WORK}/${DES_LOG_FILE}
	chown ${LOG_USER}:${LOG_USER} ${BAK_PATH_WORK}/${DES_LOG_FILE}.gz

	cp -r ${BAK_PATH_WORK}/${DES_LOG_FILE}.gz ${BAK_PATH_BAK}/${DES_LOG_FILE}.gz
	chown ${LOG_USER}:${LOG_USER} ${BAK_PATH_BAK}/${DES_LOG_FILE}.gz
done

su - ${LOG_USER}<<EOF
nohup ${RUN_HOME}/put_hdfs.sh ${CONFIG_FILE} >> ${BAK_PATH_WORK_LOG}/put_hdfs.log 2>&1 &
exit
EOF

rm -f ${BAK_PATH_BAK}/*${DELEDATE}*
