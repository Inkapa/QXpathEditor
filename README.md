About
-----

QXpathEditor is a **simple** XPath editor written in Python and
PyQt.

You can use QXPathEditor as a standalone application but also as a widget
in your own PyQt/PySide application.


The tool has been inspired by:

- QRegexEditor: https://github.com/ColinDuquesnoy/QRegexEditor

![Preview image](https://i.imgur.com/SNq3Swr.png)
![Preview image](https://i.imgur.com/zRAV8Kq.png)

Installation
------------

First install the package from pypi:

    pip install qxpatheditor --upgrade

Then you can run the application::

    QXPathEditor

Dependencies
------------

- python (2.7 or >= 3.2)
- PyQt5 or PySide or PyQt4
- lxml (>=4.7.1)

Using the widget in a custom PyQt application
---------------------------------------------

Use the widget as any other qt widget.

You may specify the XPath expression and the string pattern programmatically.
You might also want to connect to the ``quick_ref_requested`` signal so that your
application can show/hide a quick reference widget in the most appropriate place.


```python
"""
This example show you how to use the widget in a custom application.
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# if you use PyQt4 or PySide, you must set the QT_API environment variable
# to select the proper bindings, see
# https://github.com/pyQode/pyQode/wiki/Getting-started#qt-bindings-selection
from qxpatheditor.api import XPathEditorWidget, QuickRefWidget


app = QApplication(sys.argv)
window = QMainWindow()
editor = XPathEditorWidget()
quick_ref = QuickRefWidget()
quick_ref.hide()
window.setCentralWidget(editor)
# show/hide quick reference widget
editor.quick_ref_requested.connect(quick_ref.setVisible)
window.show()
app.exec_()
```
