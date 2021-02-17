#!/usr/bin/python

import sys

class_options = None
package_options = None

package = None
for option in sys.argv[1:]:
  # debugging
  #print "option = %s" % option

  if option in ["-c", "--class"]:
    package = False
  elif option in ["-p", "--package"]:
    package = True
  elif package == None:
    print "Must specify -g or -p prior to options"
    sys.exit(1)
  else:
    if package:
      package_options = option
    else:
      class_options = option

# debugging
#print "class options: %s" % class_options
#print "package_options: %s" % package_options

# read file
lines = file("paper.tex").readlines()

# class options
lines[0] = "\documentclass[%s]{book}\n" % class_options
# package options
lines[1] = "\usepackage[%s]{uva-seas-thesis}\n" % package_options

# write file
file("paper.tex", "w").write("".join(lines))

sys.exit(0)
