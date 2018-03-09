from ..general.expressions import polite
from ..countries.us import locations as us
from ..countries.uk import locations as locations_uk

# DO NOT EDIT BELOW THIS LINE
phrase = polite("I truly hate {} in US, and really hate {} in UK".format(
    us.worst,
    locations_uk.worst,
))
