#!/usr/bin/env python
# encoding: utf-8

import sys
import json
import codecs
from lib.msgParser import Message
from cortexutils.analyzer import Analyzer


class MsgParserAnalyzer(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)

        self.filename = self.getParam('attachment.name', 'noname.ext')
        self.filepath = self.getParam('file', None, 'File is missing')

    def summary(self, raw):
        result = {
            "attachments": 0
        }
        if("attachments" in raw):
            result["attachments"] = len(raw["attachments"])

        return result

    def run(self):
        if self.data_type == 'file':
            try:
                self.report(Message(self.filepath).getReport())
            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()


if __name__ == '__main__':
    MsgParserAnalyzer().run()
