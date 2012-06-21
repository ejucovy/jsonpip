Pass in a requirements.txt file, get back structured JSON summary.  Work in progress.

Works on URLs too!

$ python parse_reqs.py http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt | python -m json.tool

{
    "Beaker": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 5)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [
            [
                "==", 
                "1.5.4"
            ]
        ], 
        "source_dir": null, 
        "url": null
    }, 
    "Deliverance": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 7)", 
        "editable": true, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": {
            "egg_fragment": "Deliverance-dev", 
            "path": "git+git@github.com:deliverance/Deliverance.git"
        }
    }, 
    "Paste": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 1)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [
            [
                "==", 
                "1.7.2"
            ]
        ], 
        "source_dir": null, 
        "url": null
    }, 
    "PasteDeploy": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 3)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [
            [
                "==", 
                "1.3.4"
            ]
        ], 
        "source_dir": null, 
        "url": null
    }, 
    "PasteScript": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 2)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [
            [
                "==", 
                "1.7.3"
            ]
        ], 
        "source_dir": null, 
        "url": null
    }, 
    "WSGIFilter": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 8)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": null
    }, 
    "WSGIProxy": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 9)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": null
    }, 
    "WebOb": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 4)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [
            [
                "==", 
                "1.0.8"
            ]
        ], 
        "source_dir": null, 
        "url": null
    }, 
    "eyvind": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 11)", 
        "editable": true, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": {
            "egg_fragment": "eyvind-dev", 
            "path": "git+git@github.com:socialplanning/eyvind.git"
        }
    }, 
    "libopencore": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 6)", 
        "editable": true, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": {
            "egg_fragment": "libopencore-dev", 
            "path": "git+git@github.com:socialplanning/libopencore.git"
        }
    }, 
    "setuptools": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 10)", 
        "editable": false, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": null
    }, 
    "transcluder": {
        "comes_from": "-r http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt (line 12)", 
        "editable": true, 
        "extras": [], 
        "install_spec": [], 
        "source_dir": null, 
        "url": {
            "egg_fragment": "transcluder-dev", 
            "path": "git+git@github.com:socialplanning/transcluder.git"
        }
    }
}
