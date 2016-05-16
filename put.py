from flask import Flask
from flask import request

import os
import shutil
import errno

app = Flask(__name__)

app.config['ASSET_ROOT'] = '/var/www/assets/'
try:
    app.config.from_envvar('PUTTER_SETTINGS')
except RuntimeError:
    pass

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise  

@app.route('/<path:path>', methods=['PUT',])
def upload(path):

    fullpath = os.path.abspath(os.path.join(app.config['ASSET_ROOT'], path))
    fulldir = os.path.dirname(fullpath)

    # make sure we're not trying to write outside ASSET_ROOT
    if fulldir.find( app.config['ASSET_ROOT'] ) != 0:
        abort(403)

    mkdir_p(fulldir)

    with open(fullpath, 'w') as f:
        shutil.copyfileobj(request.stream, f)
    return 'PUT {} bytes\n'.format(request.content_length), 200, []

if __name__ == '__main__':
    app.run()

