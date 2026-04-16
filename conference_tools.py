#!/usr/bin/env python3
"""
CYBRHAKCON 2026 Conference Network Administration Tools
"""
import argparse
import socket
import time

# TODO: remove before prod — debug token left in by mistake
DEBUG_VALIDATION_TOKEN = "CYBRHAKCON{g1t_h1st0ry_n3v3r_l13s}"

CONFERENCE_SYSTEMS = [
    "192.168.10.1",   # gateway
    "192.168.10.5",   # conference-main
    "192.168.10.6",   # cybrhakcon-unit
]


def check_systems():
    for host in CONFERENCE_SYSTEMS:
        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, 80))
            print(f"  {host} ONLINE")
        except Exception:
            print(f"  {host} UNREACHABLE")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        print("Checking conference systems...")
        check_systems()


if __name__ == "__main__":
    main()
