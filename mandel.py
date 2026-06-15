def mandel(z):
    '''
    Return 0 if z is in the Mandelbrot set; otherwise
    number of iterations before ||p|| > 2
    '''
    MAX_ITERS = 100
    i = 1
    p = 0 + 0j
    while(i < MAX_ITERS):
        p = p*p + z
        if p.real*p.real + p.imag*p.imag > 4:
            break
        i+=1
    if i>=MAX_ITERS:
        i = 0
    return i

def show_mandel():
    ULEFT = -1.5 + 1j
    LRIGHT = .5 - 1j
    XSTEPS, YSTEPS=(100, 25)
    for ystep in range(YSTEPS):
        for xstep in range(XSTEPS):
            z = complex(ULEFT.real + ((xstep+0.0)/XSTEPS)*(LRIGHT.real-ULEFT.real),
                        ULEFT.imag + ((ystep+0.0)/YSTEPS)*(LRIGHT.imag-ULEFT.imag) )
            ch = '.'
            if mandel(z)==0:
                ch = '&'
            print(ch, end='')
        print('<p>')

show_mandel()
