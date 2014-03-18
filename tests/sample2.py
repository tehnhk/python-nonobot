# -*- coding: utf-8 -*-
# Author: Chmouel Boudjnah <chmouel@chmouel.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def _arguments(o):
    o.add_option('--blah')


class Plugin(object):
    def __init__(self, config):
        pass

    def foo2(self, msg, **kwargs):
        return "Hello World"

    def foo2_multiple(self, msg, **kwargs):
        return ["Hello", "World"]

    def foo2_doc(self, msg, **kwargs):
        "THIS IS SOME DOC"
        pass

    def stream(self, msg, **kwargs):
        """DOC STREAM."""
        if msg['body'] != 'callstream2':
            return
        return "Hello Stream"