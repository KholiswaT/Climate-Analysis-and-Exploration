#Define Dependencies

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")

class Measurement:


    # Create our session from Python to the DB
    session = Session(engine)
"
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    precipitation_date = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
       
        precipitation_date.append(precipitation_dict)

    return jsonify(precipitation_date)

  

@app.route("/api/v1.0/stations")

def station():
    # Create our session 
    session = Session(engine)

   
    # Query all stations
    results = session.query(Measurement.station).distinct().all()

    session.close()

    # Convert list of tuples into normal list
    all_stations= list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")

def temp:

  session = Session(engine)

    temp_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date <= '2017-08-23').\
                      filter(Measurement.date >= '2016-08-23').filter(Measurement.station == 'USC00519281').all()

  session.close()
  
  temp_date = list(np.ravel(temp_results))

  return jsonify(temp_date)

@app.route("/api/v1.0/tobs")

      select_results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                         filter(Measurement.date >= start).all()
      
      start_temp = list(np.ravel(select_results))
        return jsonify(start_temp)


@app.route("/api/v1.0/<start>/<end>")
def dates(start,end)
    select2_results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                         filter(Measurement.date >= start).filter(Measurement.date <= end).all()

                         
    start_end_temp = list(np.ravel(select2_results))
        return jsonify(start_end_temp)

if __name__ == '__main__':
    app.run(debug=True)