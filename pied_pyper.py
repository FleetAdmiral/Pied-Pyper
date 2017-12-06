import pip
def pyp_install(name):
    pip.main(['install', name])

def impyp(name, mods=[]):
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
            exec("import " + name)
            pass
        except ModuleNotFoundError as e:
            pyp_install(name)
            exec("import " + name)
