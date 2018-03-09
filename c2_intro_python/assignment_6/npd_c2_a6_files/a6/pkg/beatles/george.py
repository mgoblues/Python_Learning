from ..general.expressions import impolite
from ..countries.us import locations as us_locations
from ..countries.uk import locations as uk_locations

# DO NOT EDIT BELOW THIS LINE
phrase = impolite("I like {} in the US, and {} in the UK".format(
    us_locations.best,
    uk_locations.best,
))
