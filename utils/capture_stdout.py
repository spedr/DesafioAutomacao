import sys
from io import StringIO

class CaptureStdout:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.captured = self._stringio.getvalue()
        sys.stdout = self._original_stdout
