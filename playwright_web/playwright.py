# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import gzip
import os
import shutil
import stat
import sys
import subprocess

from playwright_web.connection import Connection
from playwright_web.object_factory import create_remote_object
from playwright_web.browser_type import BrowserType
from typing import Dict

class Playwright:
  def __init__(self) -> None:
    self.loop = asyncio.get_event_loop()
    self.loop.run_until_complete(self._sync_init())

  async def _sync_init(self):
    package_path = os.path.dirname(os.path.abspath(__file__))
    platform = sys.platform
    if platform == 'darwin':
      driver_name = 'driver-macos'
    elif platform == 'linux':
      driver_name = 'driver-linux'
    elif platform == 'win32':
      driver_name = 'driver-win.exe'
    driver_executable = os.path.join(package_path, driver_name)
    archive_name = os.path.join(package_path, 'drivers', driver_name + '.gz')

    if not os.path.exists(driver_executable) or os.path.getmtime(driver_executable) < os.path.getmtime(archive_name):
      with gzip.open(archive_name, 'rb') as f_in, open(driver_executable, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    st = os.stat(driver_executable)
    if st.st_mode & stat.S_IEXEC == 0:
      os.chmod(driver_executable, st.st_mode | stat.S_IEXEC)

    subprocess.run([driver_executable, 'install'])

    self._proc = await asyncio.create_subprocess_exec(driver_executable,
      stdin=asyncio.subprocess.PIPE,
      stdout=asyncio.subprocess.PIPE,
      stderr=asyncio.subprocess.PIPE,
      limit=32768)
    self._connection = Connection(self._proc.stdout, self._proc.stdin, create_remote_object, self.loop)
    chromium, firefox, webkit = await asyncio.gather(
      self._connection.wait_for_object_with_known_name('chromium'),
      self._connection.wait_for_object_with_known_name('firefox'),
      self._connection.wait_for_object_with_known_name('webkit'))
    self.chromium: BrowserType = chromium
    self.firefox: BrowserType = firefox
    self.webkit: BrowserType = webkit
    self.browser_types: Dict[str, BrowserType] = dict(chromium=self.chromium, firefox=self.firefox, webkit=self.webkit)

playwright = Playwright()
