# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

WAIT_FOR_APP_LAUNCH = 'ms:waitForAppLaunch'


class WaitForAppLaunchOption(SupportsCapabilities):
    @property
    def wait_for_app_launch(self) -> Optional[timedelta]:
        """
        Timeout used to retry Appium Windows Driver session startup.
        """
        value = self.get_capability(WAIT_FOR_APP_LAUNCH)
        return None if value is None else timedelta(seconds=value)

    @wait_for_app_launch.setter
    def wait_for_app_launch(self, value: Union[timedelta, int]) -> None:
        """
        Similar to createSessionTimeout, but is
        applied on the server side. Enables Appium Windows Driver to wait for
        a defined amount of time after an app launch is initiated prior to
        attaching to the application session. The limit for this is 50 seconds.
        """
        self.set_capability(WAIT_FOR_APP_LAUNCH, value.seconds if isinstance(value, timedelta) else value)
