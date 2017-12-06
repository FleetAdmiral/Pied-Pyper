import pip
def pyp_install(name):
    pip.main(['install', name])

def impyp(name):
    try:
        import name
        pass
    except ModuleNotFoundError as e:
        pyp_install(name)
