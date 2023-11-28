#!/usr/bin/python3
class LockedClass:
    '''
    A locked class that only lets the user dynamically
    create the instance
    except if the new instance attribute is called first_name.
    '''
    __slots__ = ['first_name']
