""" coding: utf-8 """

# Import libraries
import os
import shutil
import tempfile
from argparse import ArgumentParser


# Class Builder
class Builder(object):

    # @name: __init__()
    # @description: Class initialization
    # @return: self values
    def __init__(self, outputexe):
        """ Class initialization """
        self.execfile = False
        self.execname = outputexe
        self.execname = os.path.basename(self.execname)
        self.worktemp = os.path.join(tempfile.gettempdir(), 'Obfuscator')
        self.builddir = os.path.dirname(__file__)

    # @name: buildexec()
    # @description: Build the stopwatch
    # @return: boolean
    def buildexec(self):
        """ Build the stopwatch """
        # Define our template
        buildfile = 'template.py'

        # Remove previous template if exists
        if os.path.exists(buildfile):
            os.remove(buildfile)

        # Create a copy of the agent
        shutil.copy('cppcrypt.py', buildfile)

        # Check if temporary path exists
        if os.path.exists(self.worktemp):
            shutil.rmtree(self.worktemp)

        # Copy the agent directory to the temporary directory
        shutil.copytree(self.builddir, self.worktemp)

        # Get the current path
        cwd = os.getcwd()

        # Move to the temporary directory
        os.chdir(self.worktemp)

        # Move the script to the temporary directory
        shutil.move(buildfile, self.execname + '.py')

        # Create the executable using PyInstaller
        exefile = self.execname + '.py'
        upxpath = '/usr/bin/upx'

        os.system('pyinstaller --noconsole --onefile --upx-dir={} {}'.format(upxpath, exefile))
        self.execfile = os.path.join(self.worktemp, 'dist', self.execname)

        # Return to main directory
        os.chdir(cwd)

        # Move the executable
        shutil.move(self.execfile, self.execname)

        # Delete the temporary directory
        shutil.rmtree(self.worktemp)

        # Delete the template
        os.remove(buildfile)

        # Terminate
        print('StopWatch built successfully: %s' % self.execname)


# Main function
def main():
    parser = ArgumentParser(description='Build the C++ Obfuscator executable')
    parser.add_argument('-o', '--output', required=True, help='executable name')
    args = parser.parse_args()
    execgen = Builder(outputexe=args.output)
    execgen.buildexec()


# Callback
if __name__ == '__main__':
    main()
