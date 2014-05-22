# -*- coding: utf-8 -*-
# Copyright (c) 2014 Docker.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import os
import shutil

from docker_registry.tools import driver


def prompt(desc, default=None):
    return default


class TestDriver():

    def setUp(self):
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')

    @mock.patch('docker_registry.tools.driver.prompt', prompt)
    def test_new(self):
        driver.main(['new', '-d', './tmp'])
        assert os.path.exists('./tmp/docker-registry-driver-my-driver')
