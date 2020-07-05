import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #TODO change this once development complete.
    # app secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Set DB Env variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Destination for uploaded photos and size limit.
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'static/images')
    IMAGE_UPLOADS = os.path.join(basedir, 'static/images')
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    
""" 
    TODO: uncomment to set up e-mail error notifications.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com'] """

    #for logging.
    #LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')