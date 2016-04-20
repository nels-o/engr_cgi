# engr_cgi
A simple template for using the bottle micro framework from personal OSU Engineering webspace.

## Installation
* Clone this repository into your `public_html` directory. It will create a directory named `engr_cgi`. Rename that directory `cgi-bin`.
* Make sure the permissions for the files in the directory (and the directories themselves) are set to `755` (in octal, if you prefer: `rwxr xr x`).
* The main server application is in the script called `app`. You may rename this whatever you like. Test that the application is working correctly by visiting `http://web.engr.oregonstate.edu/cgi-bin/cgiwrap/~<yourusername>`
* The script `py_info` is included to debug the python environment. It generally should not be included in your deployment. Remove it, or set the permissions to `700`.