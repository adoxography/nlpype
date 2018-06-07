import sys
import threading
import time
import itertools
from contextlib import contextmanager


class Signal:
    def __init__(self):
        self._trigger = False

    def fire(self):
        self._trigger = True

    def __bool__(self):
        return self._trigger


def animate(message, signal):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if signal:
            break
        sys.stderr.write('\r' + message + ' ' + c)
        sys.stderr.flush()
        time.sleep(0.1)
    sys.stderr.write('\rDone!' + ' ' * len(message) + '\n')
    sys.stderr.flush()


@contextmanager
def loading(message):
    signal = Signal()
    thread = threading.Thread(target=animate, args=[message, signal])
    thread.start()
    yield
    signal.fire()

