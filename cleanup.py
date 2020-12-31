import shutil

"""
This script will set up the media files for testing.

    1. Removes media folder
    2. Copies contents of media_backup to media
    
"""


def cleanup_directory():
    #   1.
    shutil.rmtree('./media')

    #   2.
    shutil.copytree('./media_backup', './media')
