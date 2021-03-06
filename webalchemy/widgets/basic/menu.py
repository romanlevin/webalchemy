from webalchemy import remotedocument

class menu:
    def __init__(self,rdoc,on_add=None):
        self.rdoc= rdoc
        self.element= rdoc.element('nav')

        vn= 'nav.'+self.element.varname
        self.stylesheet= self.rdoc.stylesheet()
        self.rule_nav= self.stylesheet.rule(vn)
        self.rule_navli= self.stylesheet.rule(vn+' li')
        self.rule_navlihover= self.stylesheet.rule(vn+' li:hover')
        self.on_add= on_add

    def add_item(self,*varargs):
        for text in varargs:
            i= self.rdoc.element('li',text)
            if self.on_add:
                self.on_add(i,text)
            self.element.append(i)

