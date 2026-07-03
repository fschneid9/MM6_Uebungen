from math import sin, cos, pi


def sin_pi_calculator():
    method=str()
    while method!='Sin' and method != 'Cos':
        method=input('Sin/Cos')
    success=False
    while success==False:
        n=input('n')
        try:
            n=int(n)
            success=True
            print('test')
        except:
            print('Please enter an integer.')
    results=[]
    if method=='Sin':
        for i in range(n+1):
            print('Sinus of '+str(i)+' * pi is '+str(sin(i*pi)))
            results.append(sin(i*pi))
        return(results)
    elif method=='Cos':
        for i in range(n+1):
            print('Cosinus of '+str(i)+' * pi is '+str(cos(i*pi)))
            results.append(cos(i*pi))
        return(results)

sin_pi_calculator()
    