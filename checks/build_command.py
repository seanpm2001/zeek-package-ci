#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult
from checks.bropkg import get_metadata

NAME = "build_command"

def check_build_command(pkg):
    md = get_metadata(pkg)
    if 'build_command' not in md:
        return CheckResult(NAME, True)
    bc = md['build_command']
    msg = "Package contains build command: {!r}".format(bc)
    return CheckResult(NAME, False, warnings=[msg])
