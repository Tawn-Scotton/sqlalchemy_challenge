#import all dependencies
########################

import datetime as dt

import numpy 
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create connection to Hawaii.sqlite file
#########################################

engine = create_engine("sqlite:///Resources.hawaii.sqlite") 

# Reflect an exsisting database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine)

#Save references to the "Measurement" and "Station"tables in the database
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


#initalize Flask
################
app = Flask(__name__)


#Create Flask Routes

#create the root route
@app.route("/")
def welcome():
    #list all the available api routes
    return(
        f"Welcome to the Hawaii Climate Analysis API <br/>"
        f"Avalable Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/ 1.0/station<br/>"
        f"api/v1.0.temps/start<br/>"
        f"api/v1.0.temps/end<br/>"
        f"<p> 'start' and 'end' date should be in the format MMDDYYYY.<p/>"
    )
    
    
 # Create a route that queries precipitation levels and dates and returns a dictionary using date as key and precip as value   
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year ).all()
  
    session.close()
    precip = { date: prcp for date, prcp in precipitation}
    
    return jsonify(precip)

if __name__ == "__main__":
        app.run(debug = True)
        
        
            
            
        
  
    
    
    





