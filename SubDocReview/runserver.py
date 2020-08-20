import os
from project import app

if __name__ == '__main__':
    port = 5555
    url = '127.0.0.1'
    app.run(host=url, port=port)

    # from project.app import *