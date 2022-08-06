import symforce.symbolic as sf

#to use for small angles

def exp_roll(theta: sf.Symbol):
    r = sf.Matrix33.eye()
    r[1,2] = -theta
    r[2,1] = theta
    
    t = sf.Matrix44.eye()
    t[:3,:3] = r
    return r, t

def exp_pitch(theta: sf.Symbol):
    r = sf.Matrix33.eye()
    r[0,2] = theta
    r[2,0] = -theta

    t = sf.Matrix44.eye()
    t[:3,:3] = r
    return r, t

def exp_yaw(theta: sf.Symbol):
    r = sf.Matrix33.eye()
    r[0,1] = -theta
    r[1,0] = theta

    t = sf.Matrix44.eye()
    t[:3,:3] = r
    return r, t

if __name__ == "__main__":
    theta = sf.Symbol("theta")
    p,t = exp_roll(theta)
    print(t)

