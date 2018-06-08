import os
from glob import glob
from pathlib import Path

from jpype import startJVM, getDefaultJVMPath, isJVMStarted, java

""" The separator to use in the classpath """
# TODO: Make this Windows compatible
SEP = ':'

""" The path to the directory containing this file """
CUR_DIR = Path(__file__).resolve().parent

""" The path to Java's redirected stdout """
STDOUT_PATH = CUR_DIR / 'stdout'

""" The path to Java's redirected stderr """
STDERR_PATH = CUR_DIR / 'stderr'

""" Will hold a buffer to Java's stdout when boot() has been called """
stdout = None

""" Will hold a buffer to Java's stderr when boot() has been called """
stderr = None


def boot(corenlp_path = '/opt/stanford-corenlp/latest'):
    """
    Starts up the Java Virtual Machine
    """
    if not isJVMStarted():
        startJVM(
            getDefaultJVMPath(), '-ea', '-Xmx4G',
            '-Djava.class.path=' + make_classpath(Path(corenlp_path))
        )
        capture_streams()
        open_buffers()


def capture_streams():
    """
    Redirects Java's stdout and stderr to streams
    """
    # Create the streams
    stdout = output_file(STDOUT_PATH)
    stderr = output_file(STDERR_PATH)

    # Redirect Java's streams
    java.lang.System.setOut(stdout)
    java.lang.System.setErr(stderr)


def open_buffers():
    """
    Opens Python buffers into Java's stdout and stderr
    """
    global stdout, stderr

    # Make sure the buffers exist
    STDOUT_PATH.touch()
    STDERR_PATH.touch()

    # Open the buffers
    stdout = STDOUT_PATH.open()
    stderr = STDERR_PATH.open()


def output_file(path):
    """
    Creates a Java PrintStream for to a path

    :param path: The path to create the stream to
    :type path: Path
    :return: A Java PrintStream object
    """
    PrintStream = java.io.PrintStream
    BufferedOutputStream = java.io.BufferedOutputStream
    FileOutputStream = java.io.FileOutputStream

    return PrintStream(BufferedOutputStream(FileOutputStream(str(path))), True)


def make_classpath(path):
    """
    Collects all of the JARs in a path and prepares them for loading into the
    JVM

    :param path: The path to a folder containing JAR files
    :type path: Path
    :return: A string that can be used as a classpath
    """
    return SEP.join([str(p.resolve()) for p in path.glob('*.jar')])

