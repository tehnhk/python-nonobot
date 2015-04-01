# -*- coding: utf-8 -*-
# Author: Alexander Thordendal <thordendal@thordendal.ru>
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
    
    def dice(self, msg, **kwargs):
        """Сгенерить случайное число."""
        split = msg['body'].split()
        if split and len(split) == 1 and split[-1].isdigit():
            random.seed()
            num = random.randint(1,int(split[-1]))
            result = "Результат броска: " + str(num)
            return result
        elif split and len(split) == 2 and split[0].isdigit() and split[1].isdigit():
            random.seed()
            num = random.randint(int(split[0]), int(split[1]))
            result = "Результат броска: " + str(num)
            return result
        else:
            random.seed()
            num = random.randint(1,6)
            result = "Результат броска: " + str(num)
            return result
