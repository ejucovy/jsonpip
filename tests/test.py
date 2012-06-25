

def test_basics():
    from jsonpip import parse

    foo = parse("tests/frontend-req.txt")
    assert foo == {
        'Beaker': {'url': None, 'version': '1.5.4', 'editable': False, 'name': 'Beaker'}, 
        'transcluder': {'url': 'git+git@github.com:socialplanning/transcluder.git',
                        'version': 'dev', 'editable': True, 'name': 'transcluder'},
        'libopencore': {'url': 'git+git@github.com:socialplanning/libopencore.git',
                        'version': 'dev', 'editable': True, 'name': 'libopencore'}, 
        'Paste': {'url': None, 'version': '1.7.2', 'editable': False, 'name': 'Paste'}, 
        'PasteDeploy': {'url': None, 'version': '1.3.4', 'editable': False, 
                        'name': 'PasteDeploy'}, 
        'eyvind': {'url': 'git+git@github.com:socialplanning/eyvind.git',
                   'version': 'dev', 'editable': True, 'name': 'eyvind'}, 
        'WSGIProxy': {'url': None, 'version': None, 'editable': False, 'name': 'WSGIProxy'},
        'Deliverance': {'url': 'git+git@github.com:deliverance/Deliverance.git', 
                        'version': 'dev', 'editable': True, 'name': 'Deliverance'}, 
        'setuptools': {'url': None, 'version': None, 'editable': False, 'name': 'setuptools'}, 
        'WebOb': {'url': None, 'version': '1.0.8', 'editable': False, 'name': 'WebOb'},
        'WSGIFilter': {'url': None, 'version': None, 'editable': False, 'name': 'WSGIFilter'},
        'PasteScript': {'url': None, 'version': '1.7.3', 'editable': False,
                        'name': 'PasteScript'}}

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '.')
    test_basics()
