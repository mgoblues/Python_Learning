from ..general import expressions
from ..countries.us import locations as us
from ..countries.uk import locations as uk

# DO NOT EDIT BELOW THIS LINE
phrase = expressions.polite("love {} in US, love {} in UK".format(
    us.best,
    uk.best,
))
