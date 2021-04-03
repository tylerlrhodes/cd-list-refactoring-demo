# Music CD List

This application was developed along with a series of blog posts at [my blog](https://tylerrhodes.net), to 
demonstrate refactoring Python code to be more Pythonic.

You can run this either locally, by launching the Flask application and creating a Python Virtual
Environment while also running the SPA located in the music-list-web-app folder, or, by building
and running the Docker image in Dockerfile.build.

To run this locally you must set an environment variable REACT_APP_CDLISTURL to be the host and port where
the Flask application is listening.  For instance, http://localhost:5000 or something along those lines.
