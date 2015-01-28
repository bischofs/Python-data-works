import pandas as pd
import logging
from Logger import *

class DataIO:

    def __init__(self):
        log_init()
        self.logger = logging.getLogger("Evaluation_Log")
        self.logger.info("Beginning Data Import")
      
# @name load_data
# @desc Import csv file and create pandas DataFrame
# @memberOf IO.DataIO
       
    def load_data(self,filename):
        
        try:
            self.data = pd.read_csv(filename)
            self.meta_data = _load_meta_data(data, filename)
            
            self.data = self.data.convert_objects(convert_numeric=True)
            self.logger.info("Data Import successful - %s" % filename)
        except Exception as e:
            self.logger.error(e)

# @name check_analyzer_maximums 
# @desc Load json ranges and check imported data for out of range
# The Ranges are loaded from configuration file for 
# @memberOf IO.DataIO


    def _check_analyzer_maximums(self):
        
        try:
            self.ranges = pd.read_json("ranges.json")
            self.logger.info("Checking Data Ranges")
        except Exception as e:
            self.logger.error(e)
                
        boolean_data = self.data.E_CO2D2 <  self.ranges.EngineOut_Max.CO2
        if boolean_data.all()

        
    
    def _check_units():

        








   def _load_meta_data(data, filename):
       
       meta_data = data[:2]
       
       if 'proj' in meta_data.columns:
           return meta_data
       else:
           self.logger.warning("Meta-Data missing in import file %s" % filename)
           

