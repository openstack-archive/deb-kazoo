

from nose.tools import eq_

from kazoo.testing import KazooTestCase
from oslo_utils import uuidutils

class KazooCounterTests(KazooTestCase):

    def _makeOne(self, **kw):
        path = "/" + uuidutils.generate_uuid(dashed=False)
        return self.client.Counter(path, **kw)

    def test_int_counter(self):
        counter = self._makeOne()
        eq_(counter.value, 0)
        counter += 2
        counter + 1
        eq_(counter.value, 3)
        counter -= 3
        counter - 1
        eq_(counter.value, -1)

    def test_float_counter(self):
        counter = self._makeOne(default=0.0)
        eq_(counter.value, 0.0)
        counter += 2.1
        eq_(counter.value, 2.1)
        counter -= 3.1
        eq_(counter.value, -1.0)

    def test_errors(self):
        counter = self._makeOne()
        self.assertRaises(TypeError, counter.__add__, 2.1)
        self.assertRaises(TypeError, counter.__add__, b"a")

    def test_pre_post_values(self):
        counter = self._makeOne()
        eq_(counter.value, 0)
        eq_(counter.pre_value, None)
        eq_(counter.post_value, None)
        counter += 2
        eq_(counter.pre_value, 0)
        eq_(counter.post_value, 2)
        counter -= 3
        eq_(counter.pre_value, 2)
        eq_(counter.post_value, -1)
