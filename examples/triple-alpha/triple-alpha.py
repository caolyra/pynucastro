# triple-alpha rate module generator
import reaclib

files = ["c12-gaa-he4-fy05",
         "he4-aag-c12-fy05"]

rc = reaclib.RateCollection(files)

rc.make_network(outfile="triple-alpha_rhs.py")




