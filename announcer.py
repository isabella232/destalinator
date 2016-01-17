#! /usr/bin/env python

import os
import sys

import executor


class Announcer(executor.Executor):

    def announce(self):
        self.ds.announce_new_channels()

if __name__ == "__main__":
    announcer = Announcer()
    announcer.announce()