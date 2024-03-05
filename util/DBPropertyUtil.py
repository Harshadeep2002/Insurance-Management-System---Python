class PropertyUtil:
    connection_properties = None

    @staticmethod
    def getConnectionString():
        if PropertyUtil.connection_properties is None:
            host = 'localhost'
            database = 'insurance_managementdb'
            user = 'root'
            password = 'Mahitharsha@1'
            PropertyUtil.connection_properties = {'host': host, 'database': database, 'user': user, 'password': password}
        return PropertyUtil.connection_properties