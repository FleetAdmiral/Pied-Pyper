import pip
def pyp_install(name):
    pip.main(['install', name])

def impyp(name, mods=[], alias=""):
    if(mods!=[]):
        try:
            for k in mods:
                exec("from " + name + " import "+ k)
        except ModuleNotFoundError as e:
            pyp_install(name)
            for k in mods:
                exec("from " + name + " import "+ k)
    else:
        try:
            if(alias!=""):
                exec("import " + name + " as " + alias)
            else:
                exec("import " + name)
            pass
        except ModuleNotFoundError as e:
            pyp_install(name)
            if(alias!=""):
                exec("import " + name + " as " + alias)
            else:
                exec("import " + name)
