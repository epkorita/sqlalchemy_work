import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitaion data as json"""
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    one_year_ago = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()

    all_precip = []
    for precip in one_year_ago:
        precip_dict = {}
        precip_dict["name"] = precip.name
        precip_dict["age"] = precip.age

        all_precip.append(precip_dict)

    return jsonify(Measurement)



@app.route("/api/v1.0/stations")
def stations():

   all_stations = session.query(Station.id, Station.station, Station.name).all()

   return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():

   

   return jsonify()





if __name__ == "__main__":
    app.run(debug=True)