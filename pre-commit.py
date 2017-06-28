#!/usr/bin/env python

import subprocess
import sys


def main():
    print('-----> running pre-commit unit tests')
    proc = subprocess.Popen(['python', 'tests.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, err = proc.communicate()
    err = str(err, 'utf-8')
    print(err)

    if 'FAILED' in err:  # we have to abort this commit
        print('-----> code did not pass the unit tests, aborting commit')
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
