#!/usr/bin/python3
"""Creating a rebel class"""


class MyInt(int):
    """Rebel Class"""
    
    def __eq__(self, rebel):
        """__eq__ method to compare two 
        objects by their values"""

        return int(self) != rebel
    
    def __ne__(self, rebel):
        """Negating return value"""
        
        return int(self) == rebel
