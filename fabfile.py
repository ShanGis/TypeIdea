import os

from fabric.api import run, env, roles, prefix, put ,cd
from fabric.contrib.files import exists


ENV_PATH = '/home/wcj/DjangoBlog/ven'
ACTIVE_FILE_PATH = (os.path.join(ENV_PATH, 'bin/activate')).replace('\\', '/')
PYPI = 'http://127.0.0.1:8080/simple/'


env.key_filename = ['D:/DjangoProject/fabT']
env.roledefs = {
    'develop': [
    'wcj@127.0.0.1'], 
    }


@roles('develop')
def deploy(version):
    ensure_venv()
    install(version)
    upload_supervisord_conf()
    run_supervisord()

            # run('nohup gunicorn typeidea.wsgi:application -w 4 -b 0.0.0.0:8000 &')


def pip(package, version=None):
    command = 'pip install -i {pypi} --trusted-host=127.0.0.1 '.format(
                pypi=PYPI)
    if version:
        command = command + '{package}=={version}'.format(package=package, version=version)
    else:
        command = command + package
    run(command)


def install(version):
    with prefix('source %s' % ACTIVE_FILE_PATH):
        run('nohup pypi-server -p 8080 -P ~/DjangoBlog/.htacess packages &')
        pip('typeidea', version)


def ensure_venv():
    if not exists(ACTIVE_FILE_PATH):
        run('virtualenv {}'.format(ENV_PATH))


def ensure_supervisord():
    with prefix('source %s' % ACTIVE_FILE_PATH):
        result = run('which supervisord', warn_only=True)
        # import pdb; pdb.set_trace()
        if not result:
            pip('supervisor')


def upload_supervisord_conf():
    put('conf/supervisord.conf', '{}/supervisord.conf'.format(ENV_PATH))


def restart_supervisord():
    with prefix('source %s' % ACTIVE_FILE_PATH):
        with cd(ENV_PATH):
            run('supervisorctl -c supervisord.conf restart all')


def shutdown_supervisord():
    with prefix('source %s' % ACTIVE_FILE_PATH):
        with cd(ENV_PATH):
            run('supervisorctl -c supervisord.conf shutdown', warn_only=True)


def run_supervisord():
    ensure_supervisord()
    result = run('ps aux|grep supervisord| grep -v grep', warn_only=True)
    # import pdb; pdb.set_trace()
    if result:
        shutdown_supervisord()

    with prefix('source %s' % ACTIVE_FILE_PATH):
        with cd(ENV_PATH):
            run('supervisord -c supervisord.conf')

