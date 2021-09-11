import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import math 
from mpmath import *
from scipy import interpolate
from scipy.interpolate import interp1d
import scipy.io
import csv 

def import_file(file_path): #import csv or txt file as numpy matrix
    # Retrieves name of the file used
    filename = file_path.split("/")[-1].split(".")[0]
    format_name = file_path.split(".")[-1] # retrieves format of file imported
    # If header exists, values become NaN
    file = np.genfromtxt(file_path, dtype=float, delimiter=',', names=None)
        #print(file)
        # If first row contains Nan, removes row
    if np.isnan(file[0]).all():
        data = np.delete(file,0,0)
    else:
        data = file

    return data, filename, format_name


def wavenumber3(w,h):
    # Function to calculate wavenumber k for given wave frequency w and water
    # depth h, by Newton's method.
    # Set h < 0 for deep water limit.
    g = 9.80665
    k_deep = np.square(w) / g

    if h < 0:
        k = k_deep
    else:
        k = np.zeros((len(w)), dtype= float)
        alpha = k_deep * h
        for i in range(0, len(w)):
            #print(i + 1)
            z1 = alpha[i] # first guess
            z0 = 0
            while abs(z1 - z0) > 1e-9:
                z0 = z1
                z1 = z0 - (z0 * tanh(z0) - alpha[i]) / (tanh(z0) + z0 * (sech(z0)) ** 2)
            
            k[i] = z1 / h
            #print(k)

    return k

def plot_graph(x,y,xlab,ylab, title, savefig):
        # function to plot different graphs, xlab, ylab, title and savefig should be string
        plt.plot(x,y)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
        plt.savefig(savefig)
        plt.clf()



x = input("Has standard data already been calculated? \n Type yes(y) or no(n):  ")
rho = 1025
g = 9.80665
if x.lower() == "no" or x.lower() == "n":
    print("User selected no")
    # opens window to select matlab data. 
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file, filename,format_name = import_file(file_path)
    print("filename: ", filename)
    xdata = file[:,0] #numpy array
    ydata = file[:,1]
    h1 = plot_graph(xdata,ydata,'xvalues','yvalues', 'plot', 'Graphs/{0}_raw_data.png'.format(filename))


    # asks user for metric inputs
    B = float(input("Enter the characteristic dimensions in metres:  "))
    SA = float(input("Enter the Submerged Surface Area in square metres:  "))
    d = float(input("Enter water depth in metres. If water is deep then enter any negative number:  "))
    x_axis = int(input("select the given units of x axis. Please type the corresponding number for units. \n 1. T (s) \n 2. frequency (1/s) \n 3. rotational frequency (rad/s) \n 4. k*x'\n 5. T/T0' \n 6. lambda \n Input parameters:  "))
    
    # Case 1
    if x_axis == 1:
        print("Option 1")
        T = xdata
        print(T)

    # Case 2
    elif x_axis == 2:
        print("Option 2")
        f = xdata
        T = 1 / f
        print("T", T)

    # Case 3    
    elif x_axis == 3:
        print("Option 3")
        w = xdata
        T = (2 * math.pi) / w 
        print(T)

    # Case 4
    elif x_axis == 4:
        print("Option 4")
        x8 = float(input("enter the value of x (e.g. water nepth, width, radius) that has been mutiplied by wavenumber, k:  "))
        k_x = xdata
        k = k_x / x8
        print(k)
        
        if d < 0:
            w = np.sqrt(g * k)
        else:
            w = np.sqrt( g * k * np.tanh( k * d))

        #print(w)
        T = 2 * math.pi / w 
        print(T)

    # Case 5
    elif x_axis == 5:
        print("Option 5")
        lambda_zero = float(input("enter the value of L, i.e. the resonant wavelength (lambda zero):  "))
        T_normal = xdata
        k_zero = 2 * math.pi / lambda_zero
        w_zero = np.sqrt(g * k_zero * np.tanh( k_zero * d))
        T_zero = 2 * math.pi / w_zero
        T = T_normal * T_zero
        print(T)

    # Case 6
    elif x_axis == 6:
        print("Option 6")
        L = float(input("enter the value of L, i.e. value wavelength has been divided by: "))
        lambda_6 = xdata * L
        k = 2 * math.pi / lambda_6
        if d < 0:
            w = np.sqrt(g * k)
        else:
            w = np.sqrt(g * k * np.tanh(k * d))

        T = 2 * math.pi / w 


    else:
        pass                        


    
    w = (2*np.pi) / T
    #print('w', w)
    k = wavenumber3(w, d)
    #print("k: ", k)

    # Y AXIS
    y_axis = int(input("Select the given units of y axis \n 1. da (m) \n 2. da ratio () \n 3. Power per square metre (kW/m^2) \n 4. Power (kW) \n 5. da*k \n 6. da/Lambda) \n Input parameters:  "))
    if y_axis == 1:
        da = ydata 
        print(da)

    elif y_axis == 2:
        ratio = input("is da ratio presented as a decimal or percentage?: ")
        if ratio == "percentage":
            c9 = 0.01
        else:
            c9 = 1

        da_ratio = ydata * c9
        da = da_ratio * B
        print(da)

    elif y_axis == 3:

        measure = input("Is Power in kw or w?: ")
        if measure == "w":
            c5 = 1
        else:
            c5 = 1000

        P = ydata

        
        if d < 0:
            De = 1
        else:
            De = (np.tanh(k*d) + k*d) / np.square((np.cosh(k*d)))  # depth function
        
        A = 1

        # wave energy transport [W/m]
        J = (rho * np.square(g) * De * np.square(A)) / (4 * w)

        #capture width 
        da = (P*c5) / J

    elif y_axis == 4:
        c5 = 1000
        measure = input("Is Power in kw or w?:")
        if measure == "w":
            c5 = 1

        else:
            c5 = 1000

        P = ydata
        A = float(input("Enter incident wave amplitude in metres: "))       
        if d < 0:
            De = 1
        else:
            De = (np.tanh(k*d) + k*d) / np.square(np.cosh(k*d))

        J = (rho * np.square(g) * De * np.square(A)) / (4 * w)

        da = (P * c5) / J

        print(da)
    
    elif y_axis == 5:
        KL = ydata
        da = KL / k  
        print(da)

    elif y_axis == 6:
        lambda_6 = (2*np.pi)/k
        da_ratio_lambda = ydata
        da = da_ratio_lambda*lambda_6
        print(da)

    else:
        pass


    if x_axis == 2 or x_axis == 3 or x_axis == 4:
        T = np.flipud(T)
        da = np.flipud(da)
        print(da)



    w = (2* math.pi)/T

    k = wavenumber3(w, d)

    lambda_6 = (2 * math.pi) / k

    h2 = plot_graph(lambda_6,da,'lambda','da', 'Capture Width vs Wavelength', 'Graphs/{0}.png'.format(filename))

    # Saving variables into csv file
    #print('da', da, len(da))
    #print('SA', SA)
    #print('B', B)
    #print('T', T)
    #print('d', d)

    lambda_list = lambda_6.tolist()
    lambda_list.insert(0, 'lambda')
    T_list = T.tolist()
    T_list.insert(0,'T')
    da_list = da.tolist()
    da_list.insert(0,'da')
    SA_list = ['SA', SA]
    B_list = ['B', B]
    d_list = ['d', d]

    var_list = [] # list saved as csv file to store the variables
    var_list.append(lambda_list)
    var_list.append(T_list)
    var_list.append(da_list)
    var_list.append(SA_list)
    var_list.append(B_list)
    var_list.append(d_list)

    with open("Variables/{0}.csv".format(filename), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(var_list)

    

else:
    # if user selects yes
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    filename = file_path.split("/")[-1].split(".")[0]
    format_name = file_path.split(".")[-1] # retrieves format of file imported
    
    if format_name == 'mat':
        mat = scipy.io.loadmat(file_path)
        lambda_6 = mat['lambda'].flatten()
        T = mat['T'].flatten()
        da = mat['da'].flatten()
        SA = mat['SA'].item()
        B = mat['B'].item()
        d = mat['d'].item()

    else:
        # code if imported file is csv or txt
        pass

    h2 = plot_graph(lambda_6,da,'lambda','da', 'Capture Width vs Wavelength', 'Graphs/{0}.png'.format(filename))


D = np.sqrt(SA) # square root of surface area 

# Using square root of surface area
T_hat = T * np.sqrt(g/D)
da_hat = da / D
lambda_hat = lambda_6 / D
sigma = np.sqrt(lambda_6 / D)

# Using characteristic dimensions
T_hat2 = T * np.sqrt(g/B)
da_hat2 = da / B
lambda_hat2 = lambda_6 / B
sigma2 = np.sqrt(lambda_6 / B)

# Various metrics, without integration limits
product = lambda_hat * da_hat
NM_lambda_hat = abs(np.trapz(x = lambda_hat, y = product))

product = T_hat * da_hat
NM_T_hat = abs(np.trapz(x = T_hat, y = product))

product = sigma * da_hat
NM_sigma = abs(np.trapz(x = sigma, y = product))

product = lambda_hat2 * da_hat2
NM_lam_hat2 = abs(np.trapz(x = lambda_hat2, y = product))

product = T_hat2 * da_hat2
NM_T_hat2 = abs(np.trapz(x = T_hat2, y = product))

product = sigma2 * da_hat2
NM_sigma2 = abs(np.trapz(x = sigma2, y = product))

# Wave period limits

t0 = float(input("Enter full-scale design period in seconds: ")) # design period (taken as centroid of area under curve) 
tl = float(input("Enter full-scale lower cut-off period in seconds: ")) # lower integration limit
tu = float(input("Enter full-scale upper cut-off period in seconds: "))  # upper integration limit
# preferred values { 9, 4, 14 }

# Using characteristic dimension

product = T_hat2 * da_hat2
first_area = abs(np.trapz(x = T_hat2, y = product))

Area = abs(np.trapz(x = T_hat2, y = da_hat2))
t0_hat = first_area / Area

t0_hat_old = 0
countitr2 = 0
print("new", t0_hat)
print("old", t0_hat_old)
print("t0", t0)
print("T_hat2", T_hat2)
print("da_hat2", da_hat2)


while abs(t0_hat - t0_hat_old) > 1e-3:
    t0_hat_old = t0_hat
    d_scaled2 = g / (np.square(t0_hat/t0)) # scaled to match design period

    tl_hat = tl * np.sqrt(g/d_scaled2)
    tu_hat = tu * np.sqrt(g/d_scaled2)

    # Apply limits, interpolate, and extrapolate (if necessary)
    T_hat_new  = np.arange(tl_hat,tu_hat,0.01)
    f = interpolate.interp1d(x = T_hat2, y = da_hat2, kind = 'linear',bounds_error = False,  fill_value = 'extrapolate') # interpolate function
    da_hat_new = f(T_hat_new)

    #print("tl_hat",tl_hat)
    #print("tu_hat", tu_hat)

    # Calculating metric score
    product = T_hat_new * da_hat_new
    first_area = abs(np.trapz(x = T_hat_new, y = product))

    Area = abs(np.trapz(x = T_hat_new, y = da_hat_new))
    t0_hat = first_area / Area

    countitr2 += 1
    #print(countitr2)
    #print(abs(t0_hat - t0_hat_old))

NM_T_hat_withlimit2 = first_area
#print("NM2", NM_T_hat_withlimit2)

# Using square root of surface area

product2 = T_hat * da_hat
first_area = abs(np.trapz(x = T_hat, y = product2))

Area = abs(np.trapz(x = T_hat, y = da_hat))
t0_hat = first_area / Area

t0_hat_old = 0
countitr = 0

while abs(t0_hat - t0_hat_old) > 1e-3:
    t0_hat_old = t0_hat
    d_scaled = g / (np.square(t0_hat/t0))

    tl_hat = tl * np.sqrt(g/d_scaled)
    tu_hat = tu * np.sqrt(g/d_scaled)

    # Apply limits, interpolate, and extrapolate (if necessary)
    T_hat_new  = np.arange(tl_hat,tu_hat,0.01)
    f = interpolate.interp1d(T_hat, da_hat, kind = 'linear', bounds_error = False,  fill_value = 'extrapolate') # interpolate function
    da_hat_new = f(T_hat_new)

    # Calculating metric score
    product = T_hat_new * da_hat_new
    first_area = abs(np.trapz(x = T_hat_new, y = product))

    Area = abs(np.trapz(x = T_hat_new, y = da_hat_new))
    t0_hat = first_area / Area

    countitr += 1

NM_T_hat_withlimit = first_area
#print("NM",NM_T_hat_withlimit)

# Saving Normalised Variables
d_scaled_list = ['da_scaled', d_scaled]
d_scaled2_list = ['da_scaled2', d_scaled2]

da_hat_list = da_hat.tolist()
da_hat_list.insert(0, 'da_hat')

da_hat_new_list = da_hat_new.tolist()
da_hat_new_list.insert(0, 'da_hat_new')

lambda_hat_list = lambda_hat.tolist()
lambda_hat_list.insert(0, 'lambda_hat')

NM_lam_hat2_list = ['NM_lam_hat2', NM_lam_hat2]
NM_lambda_hat_list = ['NM_lambda_hat', NM_lambda_hat]
NM_sigma_list = ['NM_sigma', NM_sigma]
NM_sigma2_list = ['NM_sigma2', NM_sigma2]
NM_T_hat_list = ['NM_T_hat', NM_T_hat]
NM_T_hat2_list = ['NM_T_hat2', NM_T_hat2]
NM_T_hat_withlimit_list = ['NM_T_hat_withlimit', NM_T_hat_withlimit]
NM_T_hat_withlimit2_list = ['NM_T_hat_withlimit2', NM_T_hat_withlimit2]

T_hat_list = T_hat.tolist()
T_hat_list.insert(0, 'T_hat')

T_hat_new_list = T_hat_new.tolist()
T_hat_new_list.insert(0, 'T_hat_new')

normalised_var = []
normalised_var.append(d_scaled_list)
normalised_var.append(d_scaled2_list)
normalised_var.append(da_hat_list)
normalised_var.append(da_hat_new_list)
normalised_var.append(lambda_hat_list)
normalised_var.append(NM_lam_hat2_list)
normalised_var.append(NM_lambda_hat_list)
normalised_var.append(NM_sigma_list)
normalised_var.append(NM_sigma2_list)
normalised_var.append(NM_T_hat_list)
normalised_var.append(NM_T_hat2_list)
normalised_var.append(NM_T_hat_withlimit_list)
normalised_var.append(NM_T_hat_withlimit2_list)
normalised_var.append(T_hat_list)
normalised_var.append(T_hat_new_list)

with open("Variables/{0}_normalised_with_Tlimits.csv".format(filename), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(normalised_var)



# Plot 3

plt.subplot(2,1,1)
plt.plot(T_hat_new, da_hat_new, color = "green")
plt.suptitle('T hat Vs da hat with set limits and extrapolation')
plt.plot(T_hat, da_hat, color = "blue")
plt.xlabel('T hat')
plt.ylabel('da\u0302')
plt.xlim([0, tu_hat + 3])
plt.ylim([0, max(da_hat) * 1.1])
plt.axvline(tu_hat, color = "red")
plt.axvline(tl_hat, color = "red")

plt.subplot(2,1,2)
plt.plot(lambda_hat, da_hat)
plt.ylim([0,max(da_hat) * 1.1])
plt.xlabel('\u03BB hat')
plt.ylabel('da\u0302')
plt.tight_layout(pad = 1)
plt.savefig("Graphs/{0}_normalised_with_Tlimits.png".format(filename))