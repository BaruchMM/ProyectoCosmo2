from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas


## Background variation
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)

# variation in omega_b
file = np.loadtxt("datos/backc_ontrol.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/variandoOmegaB/default00_background.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/variandoOmegaB/default01_background.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/variandoOmegaB/default02_background.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/variandoOmegaB/default03_background.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/variandoOmegaB/default04_background.dat")
axs[0, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
axs[0, 0].set_title("variation in $\Omega_b$")


# variation in $\Omega(CDM)$
file = np.loadtxt("datos/backc_ontrol.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/VariandoOmegaCDM/default00_background.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/VariandoOmegaCDM/default01_background.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/VariandoOmegaCDM/default02_background.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/VariandoOmegaCDM/default03_background.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/VariandoOmegaCDM/default04_background.dat")
axs[0, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
axs[0, 1].set_title("variation in $\Omega(CDM)$")
# Variando_h
file = np.loadtxt("datos/backc_ontrol.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/Variando_h/default00_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/Variando_h/default01_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/Variando_h/default02_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/Variando_h/default03_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/Variando_h/default04_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
file = np.loadtxt("datos/Variando_h/default05_background.dat")
axs[0, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.15')
axs[0, 2].set_title("Variando h")

# Variando_lnA_s
file = np.loadtxt("datos/backc_ontrol.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/Variando_lnA_s/default00_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/Variando_lnA_s/default01_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/Variando_lnA_s/default02_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/Variando_lnA_s/default03_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/Variando_lnA_s/default04_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
file = np.loadtxt("datos/Variando_lnA_s/default05_background.dat")
axs[1, 0].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.15')
axs[1, 0].set_title("Variando $ln(A_s)$")

# regular star marker
file = np.loadtxt("datos/backc_ontrol.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[1])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/Variando_Tau_reio/default00_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/Variando_Tau_reio/default01_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/Variando_Tau_reio/default02_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/Variando_Tau_reio/default03_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/Variando_Tau_reio/default04_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
file = np.loadtxt("datos/Variando_Tau_reio/default05_background.dat")
axs[1, 1].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.15')
axs[1, 1].set_title("Variando $\tau$ reio")

# regular asterisk marker
file = np.loadtxt("datos/backc_ontrol.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, color='blue', lw=2,label='Control')
file = np.loadtxt("datos/Variando_n_s/default00_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.05')
file = np.loadtxt("datos/Variando_n_s/default01_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.10')
file = np.loadtxt("datos/Variando_n_s/default02_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='-0.15')
file = np.loadtxt("datos/Variando_n_s/default03_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.05')
file = np.loadtxt("datos/Variando_n_s/default04_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.10')
file = np.loadtxt("datos/Variando_n_s/default05_background.dat")
axs[1, 2].plot(file.T[0],5*np.log10(file.T[6])+25, lw=2,label='+0.15')
axs[1, 2].set_title("variation in $n_s$")
plt.ylim(35,50)
plt.xlim(0,2)
plt.tight_layout()
plt.show()

## Background variation in omega_b
def BackgroundVar():
    file = np.loadtxt("datos/backc_ontrol.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, color='blue', lw=2,label='Control')
    file = np.loadtxt("datos/variandoZ/default00_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='-0.05')
    file = np.loadtxt("datos/variandoZ/default01_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='-0.10')
    file = np.loadtxt("datos/variandoZ/default02_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='-0.15')
    file = np.loadtxt("datos/variandoZ/default03_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='+0.05')
    file = np.loadtxt("datos/variandoZ/default04_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='+0.10')
    file = np.loadtxt("datos/variandoZ/default05_background.dat")
    plt.plot(file.T[0],5*np.log10(file.T[1])+25, lw=2,label='+0.15')
    plt.xlabel('z')
    plt.ylabel('$\omega_b$')
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    pylab.show()

## Background variation in omega_b
def PowerSpectrumCMB():
    file = np.loadtxt("datos/cl_control.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, color='blue', lw=2,label='Control')
    file = np.loadtxt("datos/variandoZ/default00_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='-0.05')
    file = np.loadtxt("datos/variandoZ/default01_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='-0.10')
    file = np.loadtxt("datos/variandoZ/default02_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='-0.15')
    file = np.loadtxt("datos/variandoZ/default03_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='+0.05')
    file = np.loadtxt("datos/variandoZ/default04_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='+0.10')
    file = np.loadtxt("datos/variandoZ/default05_cl.dat")
    plt.plot(file.T[0],file.T[1]*0.75*10**12, lw=2,label='+0.15')
    fileNasa = pandas.read_csv("datos/variandoZ/nasaCL.csv")
    plt.plot(fileNasa['l_center'],fileNasa['Power']*0.1,'+', lw=2,label='experimental Data')
    plt.xlabel('z')
    plt.ylabel('$\omega_b$')
    plt.legend()
    pylab.show()