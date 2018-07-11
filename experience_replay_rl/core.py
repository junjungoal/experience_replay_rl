#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import random

class ReplayBuffer(object):
    def __init__(self, buffer_size=1e5):
        self._memory = RandomAccessQueue()

    def append(self, state, action, reward, next_state=None, next_action=None):
        experience = dict(state=state, action=action, reward=reward,
                          next_state=next_state, next_action=next_action)
        self._memory.append(experience)

    def sample(self, n):
        return self._memory.sample(n)

class RandomAccessQueue(object):

    def __init__(self):
        self._queue = []

    def append(self, x):
        self._queue.append(x)
        if self.buffer_size is not None and len(self) > self.buffer_size:
            self.pop()

    def __len__(self):
        return len(self._queue)

    def __getitem__(self, i):
        return self._queue[i]

    def pop(self):
        if not self._queue:
            raise IndexError("pop from empty RandomAccessQueue")
        self._queue.pop(0)

    def sample(self, n):
        return random.sample(self._queue, n)
