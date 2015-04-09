import subprocess

SHA_CHARACTERS = set('1234567890abcdef')

class InvalidSHA(Exception):
    pass

def commit(repo, sha, msg):
    sha = filter(SHA_CHARACTERS.__contains__, sha.lower())
    if len(sha) != 40:
        raise InvalidSHA
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
        return True
    return False

