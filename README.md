# engr_cgi
A simple template for using the bottle micro framework from personal OSU Engineering webspace.

## To install, 
* Clone this repository into your public_html directory. It will create a directory named engr_cgi. rename that directory cgi-bin
* Make sure the permissions for the files in the directory (and the directories themselves) are set to 755 (in octal, specifically you need `rwxr xr x`).
* The main server application is in the script called `app`. You may rename this whatever you like. Test that the application is working correctly by visiting `http://web.engr.oregonstate.edu/cgi-bin/cgiwrap/~<yourusername>`
* The script `py_info` is included to 