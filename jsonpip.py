from pip.req import InstallRequirement
from pip.req import parse_requirements
from pip.download import _get_used_vcs_backend
from pip.index import Link
from pip.vcs import VersionControl

def determine_version(name, url_spec, distutils_spec):
    url_spec_version = None
    if url_spec and 'egg_fragment' in url_spec:
        
        url_spec_version = url_spec['egg_fragment'].split("-")[-1]

    distutils_spec_version = None
    if distutils_spec:
        for spec in distutils_spec:
            if spec and spec[0] == "==":
                distutils_spec_version = spec[1]
    if distutils_spec_version:
        return distutils_spec_version
    if url_spec_version:
        return url_spec_version
    return None

def to_json(req):
    url = None; link = None
    if req.url:
        link = Link(req.url)
        path = link.url
        if link.egg_fragment:
            egg_fragment = "#egg=%s" % link.egg_fragment
            path = path.replace(egg_fragment, '')
        parser = VersionControl(path)
        __, revision = parser.get_url_rev()
        path = path.replace('@%s' % revision, '')
        url = {
            'egg_fragment': link.egg_fragment,
            'path': path,
            'revision': revision,
            }

    version = determine_version(req.name, url, req.req.specs)

    return req.name, {
        'name': req.name,
        'version': version,
        'editable': req.editable,
        'url': url['path'] if url else None,
        'revision': url['revision'] if url else None,
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
