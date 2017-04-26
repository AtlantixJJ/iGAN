def AnimateEMDFrames64():
    n_layers = 3 # number of layers
    n_f = 128  # number of feature channels
    npx = 64  # height = width
    nc = 3  # number of image channels
    nz = 100  # # of dim for Z
    niter = 75  # # of iter at starting learning rate
    niter_decay = 125  # of iter to linearly decay learning rate to zero
    return npx, n_layers, n_f, nc

def AnimateBigData64():
    return AnimateEMDFrames64()

def AnimateFaces():
    n_layers = 3 # number of layers
    n_f = 256  # number of feature channels
    npx = 64  # height = width
    nc = 3  # number of image channels
    nz = 256  # # of dim for Z
    niter = 35  # # of iter at starting learning rate
    niter_decay = 15  # of iter to linearly decay learning rate to zero
    return npx, n_layers, n_f, nc


def AnimateEMDFrames128():
    n_layers = 4 # number of layers
    n_f = 64  # number of feature channels
    npx = 128  # height = width
    nc = 3  # number of image channels
    nz = 128  # # of dim for Z
    niter = 75  # # of iter at starting learning rate
    niter_decay = 125  # of iter to linearly decay learning rate to zero
    return npx, n_layers, n_f, nc

def outdoor_64():
    n_layers = 3 # number of layers
    n_f = 128  # number of feature channels
    npx = 64  # height = width
    nc = 3  # number of image channels
    return npx, n_layers, n_f, nc

def shoes_64():
    n_layers = 3
    n_f = 128
    npx = 64
    nc = 3
    return npx, n_layers, n_f, nc

def handbag_64():
    n_layers = 3
    n_f = 128
    npx = 64
    nc = 3
    return npx, n_layers, n_f, nc

def church_64():
    n_layers = 3
    n_f = 128
    npx = 64
    nc = 3
    return npx, n_layers, n_f, nc


def hed_shoes_64():
    n_layers = 3
    n_f = 128
    npx = 64
    nc = 1
    return npx, n_layers, n_f, nc


