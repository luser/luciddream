#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

from marionette.marionette_test import MarionetteTestCase, MarionetteJSTestCase

class LucidDreamTestCase(MarionetteTestCase):
    def __init__(self, marionette_weakref, browser=None, **kwargs):
        self.browser = browser
        MarionetteTestCase.__init__(self, marionette_weakref, **kwargs)
