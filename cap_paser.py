#!/usr/bin/python3

import os
import sys

CAP_LIST = [
    "CAP_CHOWN",
    "CAP_DAC_OVERRIDE",
    "CAP_DAC_READ_SEARCH",
    "CAP_FOWNER",
    "CAP_FSETID",
    "CAP_KILL",
    "CAP_SETGID",
    "CAP_SETUID",
    "CAP_SETPCAP",
    "CAP_LINUX_IMMUTABLE",
    "CAP_NET_BIND_SERVICE",
    "CAP_NET_BROADCAST",
    "CAP_NET_ADMIN",
    "CAP_NET_RAW",
    "CAP_IPC_LOCK",
    "CAP_IPC_OWNER",
    "CAP_SYS_MODULE",
    "CAP_SYS_RAWIO",
    "CAP_SYS_CHROOT",
    "CAP_SYS_PTRACE",
    "CAP_SYS_PACCT",
    "CAP_SYS_ADMIN",
    "CAP_SYS_BOOT",
    "CAP_SYS_NICE",
    "CAP_SYS_RESOURCE",
    "CAP_SYS_TIME",
    "CAP_SYS_TTY_CONFIG",
    "CAP_MKNOD",
    "CAP_LEASE",
    "CAP_AUDIT_WRITE",
    "CAP_AUDIT_CONTROL",
    "CAP_SETFCAP",
    "CAP_MAC_OVERRIDE",
    "CAP_MAC_ADMIN",
    "CAP_SYSLOG",
    "CAP_WAKE_ALARM",
    "CAP_BLOCK_SUSPEND",
    "CAP_AUDIT_READ",
    "CAP_PERFMON",
    "CAP_BPF",
    "CAP_CHECKPOINT_RESTORE",
    "CAP_LAST_CAP",
]


def open_and_read_files(path: str = "./files/test001.txt") -> list:
    with open(path) as f:
        l_strip = [
            s.strip().replace("\t", "").split(":")
            for s in f.readlines()
            if s.startswith("Cap")
        ]
        return l_strip


def perse_cap(c: list) -> list:
    l = []
    for i, b in enumerate(bin(int(c, 16)).replace("0b", "")[::-1]):
        if int(b):
            l.append(CAP_LIST[i])
    return l


def print_cap(cap: list):
    for c in cap:
        print(f"====={c[0]}=====")
        print(perse_cap(c[1]))


def main(path):
    cap = open_and_read_files(path)
    print_cap(cap)


if __name__ == "__main__":
    main(sys.argv[1])
