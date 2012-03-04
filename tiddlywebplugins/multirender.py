"""
Render TiddlyWiki syntax wikitext to HTML
choosing which rendering system to use based on
environ['tiddlyweb.render'].
"""


from tiddlyweb.web.util import encode_name


DEFAULT_RENDERER = 'raw'


def render(tiddler, environ):
    """
    Render TiddlyWiki wikitext in the provided
    tiddler to HTML.
    """
    config = environ.get('tiddlyweb.config', {})
    default_renderer = config.get('multirender.default', DEFAULT_RENDERER)
    renderer_name = environ.get('tiddlyweb.render', default_renderer)
    try:
        imported_module = __import__('tiddlyweb.wikitext.%s' % renderer_name,
                {}, {}, ['render'])
    except ImportError, err:
        err1 = err
        try:
            imported_module = __import__(renderer_name, {}, {}, ['render'])
        except ImportError, err:
            raise ImportError("multirender couldn't load module for %s: %s, %s" %
                    (renderer_name, err, err1))
    return imported_module.render(tiddler, environ)
