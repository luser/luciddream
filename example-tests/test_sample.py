# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from luciddream import LucidDreamTestCase

class TestSample(LucidDreamTestCase):
    def test_sample(self):
        #TODO: make this better
        self.assertIsNotNone(self.marionette.session)
        self.assertIsNotNone(self.browser.session)
