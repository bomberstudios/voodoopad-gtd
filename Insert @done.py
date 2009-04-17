# -*- coding: utf-8 -*-

'''
:Title
Insert @done

:Planguage
Python

:Requires
VoodooPad 3.5+

:Description
Inserts "@done:" in front of the given text.

EOD
'''
VPScriptSuperMenuTitle = "GTD"
VPScriptMenuTitle = "Insert @done"
VPShortcutMask = "control"
VPShortcutKey = "d"

import AppKit

def main(windowController, *args, **kwargs):
    textView = windowController.textView()
    document = windowController.document()

    if textView != None:
        textView.insertText_("@done:")
