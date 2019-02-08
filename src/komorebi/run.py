#!/usr/bin/env python3

import argparse
import os

import bjoern

from komorebi.app import app


def main():
    parser = argparse.ArgumentParser(description="A runner for bjoern.")
    parser.add_argument(
        "--unix",
        help="Path to Unix domain socket",
        default="/var/run/komorebi.sock",
    )
    args = parser.parse_args()

    # This is a hack until I can find a better way to do the cleanup.
    if os.path.exists(args.unix):
        os.unlink(args.unix)

    bjoern.run(app.wsgi_app, "unix:" + args.unix)


if __name__ == "__main__":
    main()