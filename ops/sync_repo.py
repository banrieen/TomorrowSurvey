""" 
# Sync repo between different remote repository community
# Matianer: Thomas
# Update: 2021-05-24
# License: MIT
 """

import os 
import subprocess
from urllib import parse
PIPE = subprocess.PIPE

def call_shell(cmds, cwd='.', timeout=720, **kargs):
    process = subprocess.run(cmds, cwd=cwd, timeout=timeout, stdout=PIPE, stderr=None)
    process.check_returncode()
    
def sync_repo(src, dst, branch="master", remoteAccount={}, remote="ops"):
    localDir = parse.urlparse(src).path.split("/")[-1].split(".")[0]
    if os.path.isdir(os.path.abspath(localDir)):
        clone_src = call_shell(['rm', '-rf', localDir])
    clone_src = call_shell(['git', 'clone', src])
    dstparse = parse.urlparse(dst)
    dst =  "".join([dstparse.scheme, "://", remoteAccount["name"], ":", remoteAccount["passwd"], "@", dstparse.netloc, dstparse.path])
    add_remote = call_shell(['git', 'remote', 'add',  remote, dst], cwd=os.path.abspath(localDir))
    push_remote = call_shell(['git', 'push', remote], cwd=os.path.abspath(localDir))


if __name__ == "__main__":

    branch = 'master'
    account = {"name":"Apulis", "passwd":"apulisSZ2021",}
    sync = [{"name":"apulis_platform",
             "src":"https://gitee.com/apulisplatform/apulis_platform.git",
             "dst":"https://git.openi.org.cn/Apulis/Apulis-AI-Platform.git",
             "branch":"master",
           },
           ]
    for iSy in sync:

        sync_repo(iSy["src"], iSy["dst"], iSy["branch"], account )
