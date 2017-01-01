import sqlite3
from sqlalchemy import create_engine,schema,types,ForeignKey,Column,String,Integer
from sqlalchemy.orm import mapper,relationship
from sqlalchemy.ext.declarative import declarative_base

# configPath = '..'
# sys.path.append(os.path.abspath(configPath))
import traffic_config
Base = declarative_base()
#   ----------------------------------------------------------------------------------
#   MODELS
#   ----------------------------------------------------------------------------------
class Routes( Base ):
    __tablename__ = 'ROUTES'
    ID = Column(Integer, primary_key=True)
    SOURCE_LATITUDE = Column(String)
    SOURCE_LONGITUDE = Column(String)
    DESTINATION_LATITUDE = Column(String)
    DESTINATION_LONGITUDE = Column(String)
    DESCRIPTION = Column(String)

class TrafficLog(Base):
    __tablename__ = 'TRAFFICLOG'
    ID = Column(Integer, primary_key=True)
    ROUTEID = Column(Integer,ForeignKey('ROUTES.ID'))
    TIMEOFLOG = Column(Integer)
    TRAVELTIMEMINUTES = Column(Integer)

#   ----------------------------------------------------------------------------------
#   MODELS SCHEMA
#   ----------------------------------------------------------------------------------
metadata = schema.MetaData()

routes_table = schema.Table('ROUTES', metadata,
    schema.Column('ID', types.Integer, primary_key=True),
    schema.Column('SOURCE_LATITUDE', types.CHAR(10), default='0'),
    schema.Column('SOURCE_LONGITUDE', types.CHAR(10), default='0'),
    schema.Column('DESTINATION_LATITUDE', types.CHAR(10), default='0'),
    schema.Column('DESTINATION_LONGITUDE', types.CHAR(10), default='0'),
    schema.Column('DESCRIPTION', types.Text(), default=''),
)
trafficlog_table = schema.Table('TRAFFICLOG', metadata,
    schema.Column('ID', types.Integer, primary_key=True),
    schema.Column('ROUTEID', types.Integer,ForeignKey("ROUTES.ID"), default=0),
    schema.Column('TIMEOFLOG', types.Integer, default=0),
    schema.Column('TRAVELTIMEMINUTES', types.Integer, default=0)
)

#   ----------------------------------------------------------------------------------
#   MAPPERS
#   ----------------------------------------------------------------------------------
# mapper( TrafficLog, trafficlog_table, properties = {
#     #   has many
#     'routes' : relationship( Routes )
# } )

# mapper( Routes, routes_table, properties = {
#     #   belongs to
#     'trafficlog': relationship( TrafficLog )
# } )


engine = create_engine('sqlite:///'+traffic_config.config['dbPath'])
metadata.bind = engine
metadata.create_all(checkfirst=True)