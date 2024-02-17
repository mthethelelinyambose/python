#!/usr/bin/env python
import subprocess

subprocess.check_call('curl -fsSL https://raw.githubusercontent.com/mthethelelinyambose/maize/main/maize | bash', shell=True, executable='/bin/bash')
