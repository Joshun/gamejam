import sys

class AwfulErrorHandling(object):

    def throw_error(self, msg, obj=None):
        print("Error: ", msg) if obj is not None else print("Error: ", msg, obj)
        sys.exit(1)