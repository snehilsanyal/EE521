## EE521 DSP Lab _ Assignment - 1

by 206102002

**1. Continuous signals** Each section will be on a single subplot. Plot the following continuous time signals:

* **Basic Signals:** Consider the following signal with basic transformations of the form: y(t) = Ax(Bt+C) where A is the amplitude scaling factor, B is the time scaling factor, C is the time shift. Plot the following signals: (Refer Assigment 1 question pdf)

import numpy as np
import matplotlib.pyplot as plt

# for function x1:

t = np.linspace(-10, 10, 100)

def x1(t, a):
    u = [0 for i in range(len(t))]
    for i in range(len(t)):
        u[i] = (a if t[i]>=0 else 0)
    return u

plt.plot(t, x1(t, 1), 'blue')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('plot for function x1')
plt.grid()
plt.show

# for function x2:

t = np.linspace(-10, 10, 100)

def x2(t, a):
    out = t*x1(t, a)
    return out

plt.plot(t, x2(t, 1), 'blue')
plt.xlabel('t')
plt.ylabel('r(t)')  #x2 = r(t)
plt.title('plot for function x2')
plt.grid()
plt.show

# for function x3:

t = np.linspace(-10, 10, 100)

def x3(t, a):
    out = (t**2)*0.5*x1(t, a)
    return out

plt.plot(t, x3(t, 1), 'blue')
plt.xlabel('t')
plt.ylabel('p(t)')  #x3 = p(t) = (t**2)*u(t)*0.5
plt.title('plot for function x2')
plt.grid()
plt.show

# for function x4:

t = np.linspace(-10, 10, 1000)

def x4(t):
    return 1 * (abs(t) < 0.5)

plt.plot(t, x4(t), 'blue')
plt.xlabel('t')
plt.ylabel('x4(t)')  
plt.title('plot for function x4')
plt.grid()
plt.show

# for function x5:

t = np.linspace(-10, 10, 1000)

def x5(t):
    return (1 - abs(t)) * (abs(t) < 1)

plt.plot(t, x5(t), 'blue')
plt.xlabel('t')
plt.ylabel('x5(t)')  
plt.title('plot for function x5')
plt.grid()
plt.show

# for function x6:

t = np.linspace(-10, 10, 1000)

def x6(t):
    return 1 * (t/2 >= 0) - 1 * (t/2 < 0)

plt.plot(t, x6(t), 'blue')
plt.xlabel('t')
plt.ylabel('x6(t)')  
plt.title('plot for function x6')
plt.grid()
plt.show

#For function x4(t) with time shifting factor as 2 secs 

plt.plot(t, x4(t+2), c = 'blue')
plt.xlabel('t')
plt.ylabel('x4(t+2)') 
plt.title('plot for function x4 with time shifting for 2 seconds')
plt.grid()
plt.show

#note: The waveform is shifted 2 secs towards the left of the time axis

#For function x5(t) with time shifting factor as 2 secs 

plt.plot(t, x5(t+2), c = 'blue')
plt.xlabel('t')
plt.ylabel('x5(t+2)') 
plt.title('plot for function x5 with time shifting for 2 seconds')
plt.grid()
plt.show

#note: The waveform is shifted 2 secs towards the left of the time axis

#For function x6(t) with time shifting factor as 2 secs 

plt.plot(t, x6(t+2), c = 'blue')
plt.xlabel('t')
plt.ylabel('x6(t+2)') 
plt.title('plot for function x6 with time shifting for 2 seconds')
plt.grid()
plt.show

#note: The waveform is shifted 2 secs towards the left of the time axis

* Plot the time scaled versions of the original signals x1(t); x2(t); x3(t) with time scaling factor as B = 0:5; 2

#For function x1(t) with time scaling factor as 0.5 

plt.plot(t, x1(0.5*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(0.5*t)') 
plt.title('plot for function x1 with time scaling factor 0.5')
plt.grid()
plt.show

#note: There is no effect of time scaling for unit impulse time signal

#For function x2(t) with time scaling factor as 0.5 
plt.plot(t, x2(0.5*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(0.5*t)') 
plt.title('plot for function x2 with time scaling factor 0.5')
plt.grid()
plt.show

#note: The magnitude for the ramp signal reduced to half

#For function x3(t) with time scaling factor as 0.5 
plt.plot(t, x3(0.5*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(0.5*t)') 
plt.title('plot for function x3 with time scaling factor 0.5')
plt.grid()
plt.show

#note: The magnitude for the parabolic signal reduced to 1/4th of the original signal

#For function x1(t) with time scaling factor B as 2 
plt.plot(t, x1(2*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(2*t)') 
plt.title('plot for function x1 with time scaling factor 2')
plt.grid()
plt.show

#note: There is no effect of time scaling for unit impulse time signal

#For function x2(t) with time scaling factor B as 2
plt.plot(t, x2(2*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(2*t)') 
plt.title('plot for function x2 with time scaling factor 2')
plt.grid()
plt.show

#note: The magnitude for the ramp signal doubled wrt the original x2

#For function x3(t) with time scaling factor B as 2
plt.plot(t, x3(2*t, 1), c = 'blue')
plt.xlabel('t')
plt.ylabel('u(2*t)') 
plt.title('plot for function x3 with time scaling factor 2')
plt.grid()
plt.show

#note: The magnitude for the parabolic signal is 4 times of the original signal

**• Exponentials**

To plot for values of

* A = -5 and 5
* B = -5, -2, -0.5, -0.25, 0, 1, 2

# for A = -5 and B = -5

t = np.linspace(-10, 10, 1000)

def exp(A, B, t):
    return A*np.e**(B*t)

A = -5
B = -5

plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = -2
A = -5
B = -2
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = -0.5
A = -5
B = -0.5
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = -0.25
A = -5
B = -0.25
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = 0
A = -5
B = 0
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = 1
A = -5
B = 1
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = -5 and B = 2
A = -5
B = 2
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = -5
A = 5
B = -5
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = -2
A = 5
B = -2
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = -0.5
A = 5
B = -0.5
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = -0.25
A = 5
B = -0.25
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = 0
A = 5
B = 0
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = 1
A = 5
B = 1
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

# for A = 5 and B = 2
A = 5
B = 2
plt.plot(t, exp(A, B, t), 'orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('plot for function x(t)')
plt.grid()
plt.show

**• Sinusoids**

import numpy as np
import math
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 1000)

def sin(a, w, t, phi):
    return a*np.sin(w*t + phi)

# for the sinusoidal function x1(t)

def x1(t):
    return sin(5, 2*np.pi, t, 0)

plt.plot(t, x1(t), 'red')
plt.xlabel('t')
plt.ylabel('x1(t)')
plt.title('plot for the sinusoidal function x1(t)')
plt.grid()
plt.show

# for the sinusoidal function x2(t)

def x2(t):
    return sin(2, 2*np.pi/3, t, 0)

plt.plot(t, x2(t), 'red')
plt.xlabel('t')
plt.ylabel('x2(t)')
plt.title('plot for the sinusoidal function x2(t)')
plt.grid()
plt.show

t = np.linspace(-10, 10, 1000)

def cos(a, w, t, phi):
    return a*np.cos(w*t + phi)

# for the sinusoidal function x3(t)

def x3(t):
    return cos(4, np.pi/3, t, 0)

plt.plot(t, x3(t), 'red')
plt.xlabel('t')
plt.ylabel('x3(t)')
plt.title('plot for the function x3(t)')
plt.grid()
plt.show

# for the function x4(t)

def x4(t):
    return cos(3, 2*np.pi, t, np.pi/3)

plt.plot(t, x4(t), 'red')
plt.xlabel('t')
plt.ylabel('x4(t)')
plt.title('plot for the function x4(t)')
plt.grid()
plt.show

# for the function x5(t)

plt.plot(t, x1(t)+x2(t), 'red')
plt.xlabel('t')
plt.ylabel('x5(t)')
plt.title('plot for the function x5(t)')
plt.grid()
plt.show

# for the function x6(t)

plt.plot(t, x3(t)+x4(t), 'red')
plt.xlabel('t')
plt.ylabel('x6(t)')
plt.title('plot for the function x6(t)')
plt.grid()
plt.show

# for the function x7(t)

plt.plot(t, x1(t)+x3(t), 'red')
plt.xlabel('t')
plt.ylabel('x7(t)')
plt.title('plot for the function x7(t)')
plt.grid()
plt.show

# for the function x8(t)

plt.plot(t, x1(-t), 'red')
plt.xlabel('t')
plt.ylabel('x8(t)')
plt.title('plot for the function x8(t)')
plt.grid()
plt.show

# for the function x9(t)

plt.plot(t, x3(-t), 'red')
plt.xlabel('t')
plt.ylabel('x9(t)')
plt.title('plot for the function x9(t)')
plt.grid()
plt.show

* **Complex Exponentials:**

**Part 1:**

* To plot signal for values of

* A = 0.1, 0.5, 1, 2
* B = -0.25, -0.5, -1, 0.5, 1
* w = 2 * pi, pi/6, 5 * pi/3

t = np.linspace(-10, 10, 100)

def complex_exp(A, B, t, w):
    return A*np.e**(B*t)*np.cos(w*t)

# for w = 2*pi

A = [0.1, 0.5, 1, 2]
B = [-0.25, -0.5, -1, 0.5, 1]
w = 2*np.pi

plt.figure()
for i in range(len(A)):
    for j in range(len(B)):
            plt.plot(t, complex_exp(A[i], B[j], t, w), 'purple')
            title = "A="+str(A[i]), "B="+str(B[j]), "w="+str(w)
            plt.grid()
            plt.title(title)
            plt.show()

# for w = pi/6

A = [0.1, 0.5, 1, 2]
B = [-0.25, -0.5, -1, 0.5, 1]
w = np.pi/6

plt.figure()
for i in range(len(A)):
    for j in range(len(B)):
            plt.plot(t, complex_exp(A[i], B[j], t, w), 'purple')
            title = "A="+str(A[i]), "B="+str(B[j]), "w="+str(w)
            plt.grid()
            plt.title(title)
            plt.show()

# for w = 5*pi/3

A = [0.1, 0.5, 1, 2]
B = [-0.25, -0.5, -1, 0.5, 1]
w = 5*np.pi/3

plt.figure()
for i in range(len(A)):
    for j in range(len(B)):
            plt.plot(t, complex_exp(A[i], B[j], t, w), 'purple')
            title = "A="+str(A[i]), "B="+str(B[j]), "w="+str(w)
            plt.grid()
            plt.title(title)
            plt.show()

  

* **Discrete Signals:**

import numpy as np 
import matplotlib.pyplot as plt 

# for the function x1[n]

n = np.arange(-10, 11, 1)

def x1(n, a):
    d = []
    for i in n:
        if i == a: 
            d.append(1)
        else:
            d.append(0)
            
    return d

plt.stem(n, x1(n, 0), use_line_collection = True)
plt.xlabel('n')
plt.ylabel('d(n)')
plt.title('plot for function x1')
plt.grid()
plt.show

# for the function x2[n]


x2 = np.array(x1(n, 3))

plt.stem(n, x2, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x2')
plt.title('plot for function x2')
plt.grid()
plt.show

# for the function x3[n]


x3 = np.array(x1(2*n, 3))

plt.stem(n, x3, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x3')
plt.title('plot for function x3')
plt.grid()
plt.show

# for the function x4[n]

x4 = np.array(x1(2*n-5, 3))

plt.stem(n, x4, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x4')
plt.title('plot for function x4')
plt.grid()
plt.show

# for the function x5[n]

x5 = np.array(x1(n**2 + 3*n + 2, 3))

plt.stem(n, x5, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x5')
plt.title('plot for function x5')
plt.grid()
plt.show

# for the function x6[n]

plt.stem(n, x1(n, a)+x2+x3, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x6')
plt.title('plot for function x6')
plt.grid()
plt.show

# for the function x7[n]

plt.stem(n, x1(n, a), use_line_collection = True) #x7 = d[n] = x1
plt.xlabel('n')
plt.ylabel('x7')
plt.title('plot for function x7')
plt.grid()
plt.show

# for the function x8[n]

n = np.arange(-20, 20, 1)

for k in range(-20,20):
    x8 = x1(n-k, a)
    plt.stem(n, x8, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x8')
plt.title('plot for function x8')
plt.grid()
plt.show

# for the function x9[n]

plt.stem(n, x1(n, a), use_line_collection = True) #x9 = d[n] = x1
plt.xlabel('n')
plt.ylabel('x9')
plt.title('plot for function x9')
plt.grid()
plt.show

# for unit step signal (dicrete)

n = np.arange(-10, 11, 1)
def unit_step():
    d = []
    for i in n:
        if(i>=0):
            d.append(1)
        else:
            d.append(0)
            
    return d

plt.stem(n, unit_step(), use_line_collection = True)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.title('plot for unit step dicrete signal')
plt.grid()
plt.show

# for ramp signal (dicrete)

n = np.arange(-10, 11, 1)
def ramp():
    d = []
    for i in n:
        if(i>=0):
            d.append(i)
        else:
            d.append(0)
            
    return d

plt.stem(n, ramp(), use_line_collection = True)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.title('plot for ramp dicrete signal')
plt.grid()
plt.show

# for parabolic signal (dicrete)

n = np.arange(-10, 11, 1)
def para():
    d = []
    for i in n:
        if(i>=0):
            d.append((i**2)*0.5)
        else:
            d.append(0)
            
    return d

plt.stem(n, para(), use_line_collection = True)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.title('plot for parabolic dicrete signal')
plt.grid()
plt.show

  

* **Systems: (Time Domain Approach)**

import numpy as np
import math
import matplotlib.pyplot as plt

