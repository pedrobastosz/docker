from java.util import Properties
from java.io import FileInputStream
from java.io import File
from java.io import FileOutputStream
from java import io
from java.lang import Exception
from java.lang import Throwable
import os.path
import sys

envproperty=""
if (len(sys.argv) > 1):
  envproperty=sys.argv[1]
else:
    print "Environment Property file not specified"
    sys.exit(2)

propInputStream=FileInputStream(envproperty)
configProps=Properties()
configProps.load(propInputStream)

def createJDBCDS(ds_name,ds_jndi,ds_url,ds_user,ds_pwd,target_name):
        try:      
                cd('/')
                print "Deleting datasource: " + ds_jndi
                delete(ds_jndi,'JDBCSystemResource')
                print ds_jndi + " deleted!"
        except:
                print ds_jndi + " does not exist!"

        jdbcds = create(ds_name,"JDBCSystemResource")
        jdbcResource = jdbcds.getJDBCResource()
        jdbcResource.setName(ds_name)
        jdbcds.addTarget(getMBean("/Servers/"+target_name))
        #jdbcds.addTarget(getMBean("/Clusters/"+target_name))
        dsParams = jdbcResource.getJDBCDataSourceParams()
        dsParams.addJNDIName(ds_jndi)
        dsParams.setGlobalTransactionsProtocol('None')
        driverParams = jdbcResource.getJDBCDriverParams()
        driverParams.setUrl(ds_url)
        driverParams.setDriverName('oracle.jdbc.OracleDriver')
        driverParams.setPassword(ds_pwd)
        driverProperties = driverParams.getProperties()
        connectionPoolParams = jdbcResource.getJDBCConnectionPoolParams()
        connectionPoolParams.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')
        connectionPoolParams.setMaxCapacity(30)
        connectionPoolParams.setStatementCacheSize(150)
        connectionPoolParams.setInitialCapacity(30)
        connectionPoolParams.setHighestNumWaiters(2)
        connectionPoolParams.setShrinkFrequencySeconds(0)
        connectionPoolParams.setConnectionReserveTimeoutSeconds(15)
        connectionPoolParams.setStatementTimeout(180)
        connectionPoolParams.setRemoveInfectedConnections(bool(false))
        connectionPoolParams.setConnectionCreationRetryFrequencySeconds(15)
        connectionPoolParams.setSecondsToTrustAnIdlePoolConnection(15)
        driverProperties = driverParams.getProperties()
        prop = driverProperties.createProperty('user')
        prop.setValue(ds_user)


adminUser=configProps.get("adminUser")
adminPassword=configProps.get("adminPassword")
adminURL=configProps.get("adminURL")

try:
        connect(adminUser,adminPassword,adminURL)

        edit()
        startEdit()


        ##############################################################################################
        # JDBC CONFIGURATION
        ##############################################################################################
        total_ds=configProps.get("total_ds")

        print 'Total dataSources: ' + total_ds

        
        l = 1
        while ( l <= int(total_ds)):
                print 'Configurando ds ' + str(l)
                jd_name=configProps.get("ds_name"+ str(l))
                jd_jndi=configProps.get("ds_jndi"+ str(l))
                jd_url=configProps.get("ds_url"+ str(l))
                jd_usr=configProps.get("ds_user"+ str(l))
                jd_pwd=configProps.get("ds_pwd"+ str(l))
                trg = configProps.get("target_name")
                createJDBCDS(jd_name,jd_jndi,jd_url,jd_usr,jd_pwd,trg)
                l = l+1
        ##############################################################################################
        print 'Passou while'
        save()
        print 'Passou save'
        activate(block="true")     
        print 'DataSource ' + l + ' configurado.'
except Exception:
        print 'Erro ao configurar dataSources: '

disconnect()
##############################################################################################