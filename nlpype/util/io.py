# From https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python/22434262#22434262
import os
import sys
from contextlib import contextmanager


def fileno(file_or_fd):
    fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    if not isinstance(fd, int):
        raise ValueError('Expected a file (`.fileno()`) or a file descriptor')
    return fd


class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush()
        self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


@contextmanager
def stdout_redirected(to=os.devnull, stdout=None):
    if stdout is None:
        stdout = sys.stdout

    stdout_fd = fileno(stdout)

    with os.fdopen(os.dup(stdout_fd), 'wb') as copied:
        stdout.flush()
        try:
            os.dup2(fileno(to), stdout_fd)
        except ValueError:
            with open(to, 'wb') as to_file:
                os.dup2(to_file.fileno(), stdout_fd)
        try:
            yield stdout
        finally:
            stdout.flush()
            os.dup2(copied.fileno(), stdout_fd)


@contextmanager
def stderr_redirected(to=os.devnull, stderr=None):
    if stderr is None:
        stderr = sys.stderr

    stderr_fd = fileno(stderr)

    with os.fdopen(os.dup(stderr_fd), 'wb') as copied:
        stderr.flush()
        try:
            os.dup2(fileno(to), stderr_fd)
        except ValueError:
            with open(to, 'wb') as to_file:
                os.dup2(to_file.fileno(), stderr_fd)
        try:
            yield stderr
        finally:
            stderr.flush()
            os.dup2(copied.fileno(), stderr_fd)


def merged_stderr_stdout():
    return stdout_redirected(to=sys.stdout, stdout=sys.stderr)

