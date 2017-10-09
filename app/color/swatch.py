"""
Swatch from color database.
"""

from flask import request
from flask_restful import Resource

import configuration

import psycopg2
import psycopg2.extras
    
class Swatch(Resource):
    """
    Swatch constitutes a designated naming/meaning attached to a particular color value.
    
    i.e. "rgb(255,255,200)" is Color
        
        but
        
        "Ash" is Swatch where the color value defined for that swatch is rgb(255,255,255) which is Color
    """
    
    # initialize
    def __init__(self, connection=configuration.PG_CONNECTION):
        
        # postgres connection
        self.postgres_connection = psycopg2.connect(connection)

        # postgres database cursor
        self.postgres_cursor = self.postgres_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    def get(self):
        """
        /swatches/<string:id>/
        
        Args:
            id (string): record id of the swatch
            
        Returns:
            A swatch object.
        """
                
        statement = "select * from blah;"

        # pull from postgres
        self.postgres_cursor.execute(statement)
        
        data = []
        
        # format results
        for record in self.postgres_cursor:
            
            # add to data
            data.append(record)
        
        # commit changes
        self.postgres_connection.commit()
        
        # close connection
        self.postgres_connection.close()
        
        return data