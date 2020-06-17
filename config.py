class Config:
    pass            #configuraciones globales del servidor

class DevelopmentConfig(Config):        #hereda de config
    #congiraciones necesarias para que el servidor funcione en un entorno de desarrollo
    DEBUG = True


#directorio de configuraciones
config = {
    'development': DevelopmentConfig,
    'default'    : DevelopmentConfig,  
}

