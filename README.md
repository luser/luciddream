Luciddream is a test harness for running tests between a Firefox browser and another device, such as a Firefox OS emulator.

Installation and Configuration
==============================

Currently running Luciddream is only supported on Linux, as the Firefox OS emulator is only well-supported there.

Install this module and its Python prerequisites in a virtualenv:
```
  virtualenv ./ve
  . ./ve/bin/activate
  python setup.py develop
```

**Note: currently Luciddream requires an unreleased version of marionette-client to work around a bug in it, see [bug 1101539](https://bugzilla.mozilla.org/show_bug.cgi?id=1101539).**

[Download a Firefox build](http://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/) (if you don't already have one).


[Download a Firefox OS emulator build](http://pvtbuilds.pvt.build.mozilla.org/pub/mozilla.org/b2g/tinderbox-builds/mozilla-central-emulator/) (if you don't already have one, this link requires Mozilla VPN access).


Unzip both your Firefox and your Firefox OS emulator somewhere.

If you're on a 64-bit Ubuntu, you may need to do some fiddling to ensure you have the 32-bit OpenGL libraries available. See the "Solution : have both 32bit and 64bit OpenGL libs installed, with the right symlinks" section [in this blog post](http://rishav006.wordpress.com/2014/05/19/how-to-build-b2g-emulator-in-linux-environment/).


Running Tests
=============

```
runluciddream --b2gpath /path/to/b2g-distro/ --browser-path /path/to/firefox/firefox example-tests/luciddream.ini
```
