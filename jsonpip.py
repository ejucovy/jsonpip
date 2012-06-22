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

def parse(reqfile):
    reqs = list(parse_requirements(reqfile, options=NullOptions()))
    reqs = [i for i in reqs if i.name]
    return dict([to_json(i) for i in reqs])

def diff(old, new):
    import datadiff
    return datadiff.diff(parse(old), parse(new))

if __name__ == '__main__':
    from pprint import pprint
    import sys
    import json
    if len(sys.argv) == 1:
        raise RuntimeError("usage: jsonpip [parse | diff]")
    if sys.argv[1] == "parse":
        if len(sys.argv) > 2:
            reqfile = sys.argv[2]
        else:
            raise RuntimeError("usage: jsonpip parse /path/to/requirements.txt")
        reqs = parse(reqfile)
        print json.dumps(reqs)
        sys.exit(0)

    if sys.argv[1] == "diff":
        if len(sys.argv) > 3:
            old = sys.argv[2]
            new = sys.argv[3]
        else:
            raise RuntimeError("usage: jsonpip parse /path/to/first/requirements.txt /path/to/second/requirements.txt")
        print diff(old, new)
        sys.exit(0)
