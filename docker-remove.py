# Python script to try removing docker images. Docker takes helluva
# lot of space if you are continuously working on the images directly.
# So removing old containers is essential. But "rmi" fails because
# there are dependent images. This script tries to remove. There are
# many cases where it does not work. But this is usually good.

# Usage: python docker-remove.py <image>
# image is a leaf node from "docker.io images -t" output.

import subprocess
import sys

while True:
    image = sys.argv[1]
    p = subprocess.Popen(["docker.io", "rmi", image],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode == 0:
        print image
        sys.exit()
    image = (err.splitlines()[0]).split()[8]
    ret = subprocess.call(["docker.io", "rm", image])
