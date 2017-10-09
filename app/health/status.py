"""
Status of the API.
"""

from flask import request
from flask_restful import Resource
    
class Working(Resource):
    """
    Working reveals whether or not connection to API is working.
    """
    
    def get(self):
        """
        /working/
        
        Args:
            xx
            
        Returns:
            xx
        """
        
        # set up object to export
        data = { "working": "YES" }
        
        return data