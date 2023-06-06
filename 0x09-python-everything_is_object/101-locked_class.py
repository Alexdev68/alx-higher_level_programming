#!/usr/bin/python3
class LockedClass:

    __slots__ = ['first_name']

    def something(self, first_name):
        self.first_name
