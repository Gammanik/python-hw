# DO NOT TOUCH THIS FILE!

import unittest
import os

if __name__ == "__main__":
    loader = unittest.TestLoader()
    
    script_path = os.path.realpath(__file__)
    start_dir = os.path.dirname(script_path) + "/tests"

    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
