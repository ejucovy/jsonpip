Pass in a requirements.txt file, get back structured JSON summary.  Work in progress.

Works on URLs too!

$ python jsonpip.py parse http://dist.socialplanning.org/build/requirements/opencore-maximal/trunk/frontend-req.txt | python -m json.tool

{
    "Beaker": {
        "editable": false, 
        "name": "Beaker", 
        "url": null, 
        "version": "1.5.4"
    }, 
    "Deliverance": {
        "editable": true, 
        "name": "Deliverance", 
        "url": "git+git@github.com:deliverance/Deliverance.git", 
        "version": "dev"
    }, 
    "Paste": {
        "editable": false, 
        "name": "Paste", 
        "url": null, 
        "version": "1.7.2"
    }, 
    "PasteDeploy": {
        "editable": false, 
        "name": "PasteDeploy", 
        "url": null, 
        "version": "1.3.4"
    }, 
    "PasteScript": {
        "editable": false, 
        "name": "PasteScript", 
        "url": null, 
        "version": "1.7.3"
    }, 
    "WSGIFilter": {
        "editable": false, 
        "name": "WSGIFilter", 
        "url": null, 
        "version": null
    }, 
    "WSGIProxy": {
        "editable": false, 
        "name": "WSGIProxy", 
        "url": null, 
        "version": null
    }, 
    "WebOb": {
        "editable": false, 
        "name": "WebOb", 
        "url": null, 
        "version": "1.0.8"
    }, 
    "eyvind": {
        "editable": true, 
        "name": "eyvind", 
        "url": "git+git@github.com:socialplanning/eyvind.git", 
        "version": "dev"
    }, 
    "libopencore": {
        "editable": true, 
        "name": "libopencore", 
        "url": "git+git@github.com:socialplanning/libopencore.git", 
        "version": "dev"
    }, 
    "setuptools": {
        "editable": false, 
        "name": "setuptools", 
        "url": null, 
        "version": null
    }, 
    "transcluder": {
        "editable": true, 
        "name": "transcluder", 
        "url": "git+git@github.com:socialplanning/transcluder.git", 
        "version": "dev"
    }
}

