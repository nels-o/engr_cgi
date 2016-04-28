# engr_cgi
A simple template for using the bottle micro framework from personal OSU Engineering webspace.

## Installation
* Clone this repository into your `public_html` directory. It will create a directory named `engr_cgi`. Rename that directory `cgi-bin`.
* Make sure the permissions for the files in the directory (and the directories themselves) are set to `755` (in octal, if you prefer: `rwxr xr x`).
* The main server application is in the script called `app`. You may rename this whatever you like. Beware; if you rename the application, you must also modify the static path specified in `settings.py`. Test that the application is working correctly by visiting `http://web.engr.oregonstate.edu/cgi-bin/cgiwrap/<yourusername>/app`
    
    Note that this url invokes a cgi application. The main engineering webserver's `cgi-bin` has a program `cgiwrap` that knows about user names and public html directories. Conveniently, that means that you can safely omit (or include) the usual `~` that prefixes your username.

* The script `py_info` is included to debug the python environment. It generally should not be included in your deployment. Remove it, or set the permissions to `700`.

## Dependencies

If you are using python, you will probably want access to the broadwer pacakge ecosystem. Because of administrative constraints (and security, and good sense) we can't directly install packages on the server. Instead, host those dependencies as `.egg` files in the `carton` directory. I know `.egg`s aren't the preferred form of distribution these days, but `.egg`s are better than wheels for our purposes because they can be imported at run-time.

When imported, the `settings` module includes all of the `.egg` files on the python path. If your script relies on modules in the `carton` you must `import settings` before importing any of your dependencies. See `app` or `py_info` for examples.


