from flask import Flask
import subprocess
app = Flask(__name__)
app.debug = True

SHA_CHARACTERS = set('1234567890abcdef')

@app.route('/commit/<repo>/<sha>/<msg>')
def hello_world(repo, sha, msg):
    sha = filter(SHA_CHARACTERS.__contains__, sha.lower())
    if len(sha) != 40:
        return "INVALID_SHA", 500
    command = [
        'lolcommits',
        '--manual',
        '--capture',
        '--repo', repo,
        '--sha', sha,
        '--msg', msg,
    ]
    ret = subprocess.call(command)
    if ret == 0:
        return "lolcommit succesful!", 200
    else:
        return "lolcommit error code: {}".format(ret), 500

if __name__ == '__main__':
    app.run(port=17363)
