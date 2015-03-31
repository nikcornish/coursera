abc = 'With               three words'
mysplit = abc.split()
print mysplit


# specifying the delimiter tells python
# to use the semi-colon as the splitter
animals = 'cat;dog;mouse'
thing = animals.split(';')
print thing
print len(thing)