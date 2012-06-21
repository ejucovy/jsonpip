from pip.req import InstallRequirement
from pip.req import parse_requirements
from pip.download import _get_used_vcs_backend
from pip.index import Link

def to_json(req):
    url = None; link = None
    if req.url:
        link = Link(req.url)
        url = {
            'egg_fragment': link.egg_fragment,
            'path': link.path,
            }

    return req.name, {
        'comes_from': req.comes_from,
        'source_dir': req.source_dir,
        'editable': req.editable,
        'url': url,
        'install_spec': req.req.specs,
        'extras': req.extras,
        }

class NullOptions(object):
    def __getattr__(self, attr):
        return None

if __name__ == '__main__':
    from pprint import pprint
    import sys
    if len(sys.argv) > 1:
        reqfile = sys.argv[1]
    else:
        raise RuntimeError("usage: parse_requirements /path/to/requirements.txt")
    reqs = list(parse_requirements(reqfile, options=NullOptions()))
    reqs = [i for i in reqs if i.name]
    pprint( dict([
                to_json(i) for i in reqs
                ]) )
    
