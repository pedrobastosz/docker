WLST_SCRIPT="$1"
CONTROL_PROPFILE="$2"

umask 027

# set up common environment
WLS_NOT_BRIEF_ENV=true

 
. /u01/app/middleware11g/10.3.6/wlserver_10.3/server/bin/setWLSEnv.sh

export JAVA_HOME=/u01/app/jdk/jdk1.7.0_55

CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${FMWLAUNCH_CLASSPATH}${CLASSPATHSEP}${DERBY_CLASSPATH}

${CLASSPATHSEP}${DERBY_TOOLS}${CLASSPATHSEP}${POINTBASE_CLASSPATH}${CLASSPATHSEP}${POINTBASE_TOOLS}"

if [ "${WLST_HOME}" != "" ] ; then
    WLST_PROPERTIES="-Dweblogic.wlstHome='${WLST_HOME}' ${WLST_PROPERTIES}"
    export WLST_PROPERTIES
fi

echo
echo CLASSPATH=${CLASSPATH}
echo JAVA_HOME
JVM_ARGS="-Dprod.props.file='${WL_HOME}'/.product.properties ${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS}"

eval '"${JAVA_HOME}/bin/java"' ${JVM_ARGS} weblogic.WLST $WLST_SCRIPT $CONTROL_PROPFILE