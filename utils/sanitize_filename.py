import re

def sanitize_filename(filename):
    """
    Sanitizes the filename by removing or replacing characters that are not allowed in filenames.
    """
    # Replace invalid filename characters with an underscore
    return re.sub(r'[\\/*?:"<>|]', "_", filename)