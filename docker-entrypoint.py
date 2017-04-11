#!/usr/bin/env python3

# Single entry point / dispatcher for simplified running of
#
## pman
## pfioh
## purl
#

import  argparse
import  os

str_desc = """

 NAME

    docker-entrypoint.py

 SYNOPSIS

    docker-entrypoint.py    [optional cmd args for pfioh]

 DESCRIPTION

  'docker-entrypoint.py' is the main entry point for running the pfioh container.

"""


def pfioh_do(args, unknown):

    str_otherArgs   = ' '.join(unknown)

    str_CMD = "/usr/local/bin/pfioh %s" % (str_otherArgs)
    return str_CMD

def purl_do(args, unknown):

    str_http        = http_construct(args, unknown)
    str_otherArgs   = ' '.join(unknown)

    str_raw = ''
    if args.b_raw: str_raw = "--raw"

    str_CMD = "/usr/local/bin/purl --verb %s %s %s --jsonwrapper '%s' --msg '%s' %s" % (args.verb, str_raw, str_http, args.jsonwrapper, args.msg, str_otherArgs)
    return str_CMD

def bash_do(args, unknown):

    str_http        = http_construct(args, unknown)
    str_otherArgs   = ' '.join(unknown)

    str_CMD = "/bin/bash"
    return str_CMD


parser  = argparse.ArgumentParser(description = str_desc)


parser.add_argument(
    '--msg',
    action  = 'store',
    dest    = 'msg',
    default = '',
    help    = 'JSON msg payload'
)


args, unknown   = parser.parse_known_args()

if __name__ == '__main__':
    try:
        fname   = 'pfioh_do(args, unknown)'
        str_cmd = eval(fname)
        print(str_cmd)
        os.system(str_cmd)
    except:
        print("Misunderstood container app... exiting.")