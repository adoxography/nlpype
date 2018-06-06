import os
from glob import glob

from jpype import startJVM, getDefaultJVMPath, isJVMStarted


""" The separator to use in the classpath """
# TODO: Make this Windows compatible
SEP = ':'


def boot(corenlp_path = '/opt/stanford-corenlp/latest'):
    """
    Starts up the Java Virtual Machine
    """
    if not isJVMStarted():
        startJVM(
            getDefaultJVMPath(), '-ea', '-Xmx4G',
            '-Djava.class.path=' + make_classpath(corenlp_path)
        )


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

