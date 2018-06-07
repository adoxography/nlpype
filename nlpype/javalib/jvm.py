import os
from glob import glob

from jpype import startJVM, getDefaultJVMPath, isJVMStarted, java


""" The separator to use in the classpath """
# TODO: Make this Windows compatible
SEP = ':'

stdout = None
stderr = None


def boot(corenlp_path = '/opt/stanford-corenlp/latest'):
    """
    Starts up the Java Virtual Machine
    """
    if not isJVMStarted():
        startJVM(
            getDefaultJVMPath(), '-ea', '-Xmx4G',
            '-Djava.class.path=' + make_classpath(corenlp_path)
        )
        capture_streams()


def capture_streams():
    """
    Redirects Java's stdout and stderr to streams
    """
    global stdout, stderr
    ByteArrayOutputStream = java.io.ByteArrayOutputStream
    PrintStream = java.io.PrintStream

    stdout = ByteArrayOutputStream() 
    stderr = ByteArrayOutputStream() 
    java.lang.System.setOut(PrintStream(stdout))
    java.lang.System.setErr(PrintStream(stderr))


def make_classpath(path):
    """
    Collects all of the JARs in a path and prepares them for loading into the
    JVM

    :param path: The path to a folder containing JAR files
    :type path: str
    :return: A string that can be used as a classpath
    """
    jars = glob(os.path.join(path, '*.jar'))
    return SEP.join(jars)

