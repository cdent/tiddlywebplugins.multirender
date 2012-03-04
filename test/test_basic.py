
import py.test

from tiddlywebplugins.multirender import render

from tiddlyweb.model.tiddler import Tiddler

def setup_module(module):
    module.tiddler = Tiddler('hi', 'bagone')
    tiddler.text = '!Hello'

def test_render_raw():
    content = render(tiddler, {})

    assert content == '<pre>\n!Hello</pre>\n'

def test_render_missing():
    py.test.raises(ImportError,
        'render(tiddler, {"tiddlyweb.render": "monkeyrender"})')

def test_render_wikklytext():
    content = render(tiddler, {'tiddlyweb.render':
        'tiddlywebplugins.wikklytextrender'})

    assert content == '<h1 class="wikkly-h1">Hello</h1>'

def test_config_default():
    environ = {'tiddlyweb.config': {
        'multirender.default': 'tiddlywebplugins.wikklytextrender'}}
    content = render(tiddler, environ)
    assert content == '<h1 class="wikkly-h1">Hello</h1>'

