
class Presentation(object):

    def __init__(self, path):
        with open(path) as f:
            self.pres_dict = self.parser(f.readlines())

    def parser(self, lines):
        from collections import OrderedDict
        els = OrderedDict()
        cntr = 0
        el = str()
        for l in lines:
            if l.startswith('##'):
                cntr+=1
                els.update({cntr:el})
                el = str()
                continue
            el += l
        return els
        
    def next(self):
        for i,el in self.pres_dict.iteritems():
            yield i,el

def next_slide(pres):
    import os
    os.system('clear')
    i, cur_slide = next(pres)
    print "Slide Nr " + str(i) 
    print cur_slide 
    return cur_slide

