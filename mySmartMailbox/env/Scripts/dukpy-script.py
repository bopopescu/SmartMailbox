#!C:\Users\chris\Documents\Git\SmartMailbox\mySmartMailbox\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'dukpy==0.2.0','console_scripts','dukpy'
__requires__ = 'dukpy==0.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dukpy==0.2.0', 'console_scripts', 'dukpy')()
    )
