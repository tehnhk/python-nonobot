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

import random
import nonobot.plugins

class Plugin(nonobot.plugins.Base):

    def what(self, msg, **kwargs):
        """Подскажет, что тебе делать, юзернейм"""        
        phraseEnd = ('очевидно же!',
                     'бака!',
                     '%username%.',
                     'но не думай, что это я ради тебя тут выбираю, б-б-бака!'
                    )
        random.seed()
        splittedMsg = msg['body'].strip("?").split(" или ")
        result = random.randint(0,len(splittedMsg)-1)
        endresult = random.randint(0,len(phraseEnd)-1)
        midanswer=splittedMsg[result]
        midanswer=midanswer[0].upper() + midanswer[1:]
        answer = ", ".join([midanswer,
                            phraseEnd[endresult]])        
        return answer
