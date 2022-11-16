import os

basedir = os.path.abspath(os.path.dirname(__file__))

#Give access to the projcect from an Operating System (os) we find ourselves in
# Allow outsode file/folders to be added to the project from base directory


class Config():
    """
    Set config variable for the Flask App.
    Using environment variables where available.
    Otherwise, create the config variable if not done already.
    
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'u cant catch me im the gingerbread man'