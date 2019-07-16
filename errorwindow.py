# Code derived from Bryan Olson's source posted in this related Usenet discussion:
#   https://groups.google.com/d/msg/comp.lang.python/HWPhLhXKUos/TpFeWxEE9nsJ
#   https://groups.google.com/d/msg/comp.lang.python/HWPhLhXKUos/eEHYAl4dH9YJ
#
#  See the comments and doc string below.
#
#   Here's a module to show stderr output from console-less Python
#   apps, and stay out of the way otherwise. I plan to make a ASPN
#   recipe of it, but I thought I'd run it by this group first.
#
#   To use it, import the module. That's it. Upon import it will
#   assign sys.stderr.
#
#   In the normal case, your code is perfect so nothing ever gets
#   written to stderr, and the module won't do much of anything.
#   Upon the first write to stderr, if any, the module will launch a
#   new process, and that process will show the stderr output in a
#   window. The window will live until dismissed; I hate, hate, hate
#   those vanishing-consoles-with-critical-information.
#
#   The code shows some arguably-cool tricks. To fit everthing in
#   one file, the module runs the Python interpreter on itself; it
#   uses the "if __name__ == '__main__'" idiom to behave radically
#   differently upon import versus direct execution. It uses TkInter
#   for the window, but that's in a new process; it does not import
#   TkInter into your application.
#
#   To try it out, save it to a file -- I call it "errorwindow.py" -
#   - and import it into some subsequently-incorrect code. For
#   example:
#
#        import errorwindow
#
#        a = 3 + 1 + nonesuchdefined
#
#   should cause a window to appear, showing the traceback of a
#   Python NameError.
#
#   --
#   --Bryan
#   ----------------------------------------------------------------
#
#   martineau - Modified to use subprocess.Popen instead of the os.popen
#               which has been deprecated since Py 2.6. Changed so it
#               redirects both stdout and stderr. Added numerous
#               comments, and also inserted double quotes around paths
#               in case they have embedded space characters in them, as
#               they did on my Windows system.
#
#               Recently updated it to work in both Python 2 and Python 3.

"""
    Import this module into graphical Python apps to provide a
    sys.stderr. No functions to call, just import it. It uses
    only facilities in the Python standard distribution.

    If nothing is ever written to stderr, then the module just
    sits there and stays out of your face. Upon write to stderr,
    it launches a new process, piping it error stream. The new
    process throws up a window showing the error messages.
"""
import subprocess
import sys
try:
    import thread
except ModuleNotFoundError:  # Python 3
    import _thread as thread
import os

EXC_INFO_FILENAME = 'exc_info.txt'

if __name__ == '__main__':  # When spawned as separate process.
    # create window in which to display output
    # then copy stdin to the window until EOF
    # will happen when output is sent to each OutputPipe created
    try:
        from Tkinter import BOTH, END, Frame, Text, TOP, YES
        import tkFont
        import Queue
    except ModuleNotFoundError:  # Python 3
        from tkinter import BOTH, END, Frame, Text, TOP, YES
        import tkinter.font as tkFont
        import queue as Queue

    Q_EMPTY = Queue.Empty  # An exception class.
    queue = Queue.Queue(1000)  # FIFO

    def read_stdin(app, bufsize=4096):
        fd = sys.stdin.fileno()  # File descriptor for os.read() calls.
        read = os.read
        put = queue.put
        while True:
            put(read(fd, bufsize))

    class Application(Frame):
        def __init__(self, master=None, font_size=8, text_color='#0000AA', rows=25, cols=100):
            Frame.__init__(self, master)
            # Create title based on the arguments passed to the spawned script:
            #   argv[0]: name of this script (ignored)
            #   argv[1]: name of script that imported this module
            #   argv[2]: name of redirected stream (optional)
            if len(sys.argv) < 2:
                title = "Output stream from unknown source"
            elif len(sys.argv) < 3:
                title = "Output stream from %s" % (sys.argv[1],)
            else:  # Assume it's a least 3.
                title = "Output stream '%s' from %s" % (sys.argv[2], sys.argv[1])
            self.master.title(title)
            self.pack(fill=BOTH, expand=YES)
            font = tkFont.Font(family='Courier', size=font_size)
            width = font.measure(' ' * (cols+1))
            height = font.metrics('linespace') * (rows+1)
            self.configure(width=width, height=height)
            self.pack_propagate(0)  # Force frame to be configured size.

            self.logwidget = Text(self, font=font)
            self.logwidget.pack(side=TOP, fill=BOTH, expand=YES)
            # Disallow key entry, but allow text copying with <Control-c>
            self.logwidget.bind('<Key>', lambda x: 'break')
            self.logwidget.bind('<Control-c>', lambda x: None)
            self.logwidget.configure(foreground=text_color)
            self.logwidget.insert(END, '==== Output ====\n\n')
            self.logwidget.see(END)
            self.after(200, self.start_thread, ())  # Start polling thread.

        def start_thread(self, _):
            thread.start_new_thread(read_stdin, (self,))
            self.after(200, self.check_q, ())

        def check_q(self, _):
            log = self.logwidget
            log_insert = log.insert
            log_see = log.see
            queue_get_nowait = queue.get_nowait

            go = True
            while go:
                try:
                    data = queue_get_nowait().decode()  # Must decode for Python 3.
                    if not data:
                        data = '[EOF]'
                        go = False
                    log_insert(END, data)
                    log_see(END)
                except Q_EMPTY:
                    self.after(200, self.check_q, ())
                    go = False

    app = Application()
    app.mainloop()

else: # when module is first imported
    import traceback

    class OutputPipe(object):
        def __init__(self, name=''):
            self.lock = thread.allocate_lock()
            self.name = name

        def flush(self):  # NO-OP.
            pass

        def __getattr__(self, attr):
            if attr == 'pipe':  # Attribute doesn't exist, so create it.
                # Launch this module as a separate process to display any output
                # it receives.
                # Note: It's important to put double quotes around everything just in
                # case any have embedded space characters.
                command = '"%s" "%s" "%s" "%s"' % (sys.executable,                # executable
                                                   __file__,                      # argv[0]
                                                   os.path.basename(sys.argv[0]), # argv[1]
                                                   self.name)                     # argv[2]
                #
                # Typical command and arg values on receiving end:
                #   C:\Python3\python[w].exe                                      # executable
                #   C:\vols\Files\PythonLib\Stack Overflow\errorwindow3k.py       # argv[0]
                #   errorwindow3k_test.py                                         # argv[1]
                #   stderr                                                        # argv[2]

                # Execute this script directly as __main__ with a stdin PIPE for sending
                # output to it.
                try:
                    # Had to also make stdout and stderr PIPEs too, to work with pythonw.exe
                    self.pipe = subprocess.Popen(command, bufsize=0,
                                                 stdin=subprocess.PIPE,
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE).stdin
                except Exception:
                    # Output exception info to a file since this module isn't working.
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    msg = ('%r exception in %s\n' %
                            (exc_type.__name__, os.path.basename(__file__)))
                    with open(EXC_INFO_FILENAME, 'wt') as info:
                        info.write('fatal error occurred spawning output process')
                        info.write('exeception info:' + msg)
                        traceback.print_exc(file=info)

                    sys.exit('fatal error occurred')

            return super(OutputPipe, self).__getattribute__(attr)

        def write(self, data):
            with self.lock:
                data = data.encode()  # Must encode for Python 3.
                self.pipe.write(data)  # First reference to pipe attr will cause an
                                       # OutputPipe process for the stream to be created.

    # Clean-up any left-over debugging files.
    try:
        os.remove(DEBUG_FILENAME)  # Delete previous file, if any.
    except Exception:
        pass
    try:
        os.remove(EXC_INFO_FILENAME)  # Delete previous file, if any.
    except Exception:
        pass

    # Redirect standard output streams in the process that imported this module.
    sys.stderr = OutputPipe('stderr')
    sys.stdout = OutputPipe('stdout')
