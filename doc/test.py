# import dw_incognito_service
import sys
import os
dir = os.path.dirname(__name__)

# we append our path to blender modules path
# we use if not statement to do this one time only
if not dir in sys.path:
   sys.path.append(dir )

import dw_incognito_service