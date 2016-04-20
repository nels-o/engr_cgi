import os, sys

# this should generally be your cgi-bin
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# this is the location for all static files served from your project.
# You don't actually have to do it this way, but it makes it easier to 
# reference local files.
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Contains .egg libraries you'd like to bring along
CARTON_ROOT = os.path.join(PROJECT_ROOT, 'carton')
# Load all eggs in the carton
# Note that importing any egg dependency prior to this loop
# will blow up -- the interpreter won't know what you're 
# talking about.
eggs = os.listdir(CARTON_ROOT)
for egg in eggs:
    if egg.endswith('.egg'):
        sys.path.append(os.path.join(CARTON_ROOT, egg))

# Add the control directory to the path. 
# This is for models, utility classes, etc. 
CONTROL_ROOT = os.path.join(PROJECT_ROOT, 'control')
sys.path.append(CONTROL_ROOT)

# This is a less than robust solution.
_uname = PROJECT_ROOT.split('/')[-3]

def static(file):
    if file[0] is '/':
        file = file[1:]
    # Might want to serve these directly from your public html folder via 
    # apache. This will infer your username, but the name of the application is still hardcoded (app).
    return 'http://web.engr.oregonstate.edu/cgi-bin/cgiwrap/%s/app/static/%s' %(_uname,file)