# Oracle WebLogic Server 11g (10.3.6) Docker Images by Gilberto Holms

This repository stores Dockerfiles and required files to build Oracle WLS docker image, 2 Dockerfile is provided i.e.

1. `weblogic/`: WLS simple standalone server
2. `weblogic-base-domain/`: WLS with a sample domain named 'base_domain' with admin server listen on port 7001 and password is `welcome01`

## Prerequisite:

1. Download the Generic version of "Installers with Oracle WebLogic Server and Oracle Coherence" (`wls1036_generic.jar` - size: 997 MB) from:

   http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-for-dev-1703574.html

2. Download "Java SE Development Kit 7u80" (`jdk-7u79-linux-x64.rpm` - size: 131.69 MB) from:

   http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html

## Building Docker image

Move those files to `weblogic/10.3.6/` and/or `weblogic-base-domain/10.3.6/`

```
$ cd weblogic/10.3.6
$ sudo docker build -t $YOURNAME/weblogic:10.3.6 .

AND

$ cd weblogic-base-domain/10.3.6
$ sudo docker build -t $YOURNAME/weblogic-base-domain:10.3.6 .

the weblogic-base-domain:10.3.6 image dependes on $YOURNAME/weblogic:10.3.6 previous build imagge.

```

For more information read the `Dockerfile` in those directory.

For support and information, please consult the documentation for each image or see [`GibaHolms at WordPress`](https://gibaholms.wordpress.com/).

# WLST Automations

Create container from image with shared volume:
```
docker run -it -p 7001:7001 -v ./wslt-scripts:/wslt-scripts --name=weblogic-base-domain pedrobastosz/weblogic-base-domain:10.3.6
```

To exec bash inside container and iterate with shell:

```
docker exec -i -t weblogic-base-domain /bin/bash
```

Exec
```
./jdbc_config_start.sh


