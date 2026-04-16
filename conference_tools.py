#!/usr/bin/env python3
"""
CYBRHAKCON 2026 Conference Network Administration Tools
"""
import argparse
import socket

CONFERENCE_SYSTEMS = [
    "192.168.10.1",
    "192.168.10.5",
    "192.168.10.6",
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
