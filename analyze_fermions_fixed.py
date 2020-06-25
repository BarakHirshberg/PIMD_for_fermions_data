#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

path = "/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/"

## FIGURE 1 ##
f, ((ax1,ax3)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = 6
bhw = 1

#lambs = [0.0, 0.3, 0.5, 1, 3, 10.0]
lambs = [0.0, 0.3, 0.5, 1, 3]
Nbeads = [4, 4, 4, 8, 12]
save_meanA=[]

#ax50 = plt.axes([.65, .6, .25, .25])

for ind,lam in enumerate(lambs):    
    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]))
##    print(data)

    meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
    BSEA = varA/np.sqrt(Neff)
    save_meanA.append(meanA)
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))

    ax1.errorbar(lam, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax1.errorbar(lam, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
    ax3.errorbar(lam, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    print(lam, meanS , BSES)
##    print(bhw, meanA , BSEA)
##    print(save_data)
    
#    if(lam <1):
#        ax50.errorbar(lam, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
#        ax50.errorbar(lam, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        #ax50.errorbar(lam, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)

#plt.xticks(fontsize=24)
#plt.yticks(fontsize=24)
ax1.tick_params(axis="x",labelsize=10,direction="in")
ax3.tick_params(axis="x",labelsize=10)
ax1.tick_params(axis="y",labelsize=10)
ax3.set_xlabel(r'$ \lambda $',fontsize=10,fontweight='bold')
ax1.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
ax3.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')

mean_Dornheim = [18.5, 21.0, 22.82, 26.80, 40.273]#, 74.587]
meanS_Dornheim = [0.00258, 0.01861, 0.04184, 0.1475, 0.6717]

ax1.plot(lambs, mean_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)
#ax3.plot(lambs, meanS_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

#ax50.plot(lambs[:-2], mean_Dornheim[:-2], 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

ax1.set_ylim([5,45])
ax3.set_ylim([-0.15,0.75])

f.tight_layout()
f.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'Figure4.pdf', format='pdf', dpi=600)

## FIGURE 2 ##
#plt.figure(2, figsize=(3.375,3.375),dpi=600)
f3, ((ax5,ax6)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = [3,4,5,6,7]
bhw = 1

lam = 0.5
Nbeads = 4
save_meanA=[]

for ind,atom in enumerate(Natoms):    
    save_data = pd.read_csv(path + "data_"+str(atom) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads))
##    print(data)

    meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
    BSEA = varA/np.sqrt(Neff)
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))
    print(atom, meanS , BSES)
    
    ax5.errorbar(atom, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax5.errorbar(atom, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax6.errorbar(atom, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)

    save_meanA.append(meanA)
ax5.tick_params(axis="x",labelsize=10,direction="in")
ax5.tick_params(axis="y",labelsize=10)
ax6.set_xlabel(r'$ N $',fontsize=10,fontweight='bold')
ax5.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
ax6.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')

mean_Dornheim = [8.719, 12.903, 17.66, 22.82, 28.7]
meanS_Dornheim = [0.4746, 0.2453, 0.1085, 0.04184, 0.01425]
ax5.plot(Natoms, mean_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)
#ax6.plot(Natoms, meanS_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)
ax5.set_ylim([5,35])
ax6.set_ylim([-0.15,0.65])

f3.tight_layout()
f3.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'Figure2.pdf', format='pdf', dpi=600)


## FIGURE 3 ##
#plt.figure(3, (10,10))
f2, ((ax2,ax4)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = 6
bhws = [0.5, 0.6, 0.8, 1, 1.1, 1.3]
mean_Dornheim = [32.16, 28.86, 24.98, 22.82, 22.10, 21.2]
meanS_Dornheim = [0.3616, 0.2507, 0.1079, 0.04184, 0.02526, 0.00894]

ax2.plot(bhws, mean_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)
#ax4.plot(bhws, meanS_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

lam = 0.5
Nbeads = [2, 2, 4, 4, 4, 4]
save_meanA=[]
for ind,bhw in enumerate(bhws):    
    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]))
##    print(data)

    if (len(save_data['EF'])>1):
        meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
        Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
        varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
        BSEA = varA/np.sqrt(Neff)
        save_meanA.append(meanA)
    else:
        meanA = save_data['EF']
        BSEA = save_data['Err_EF']
        save_meanA.append(save_data.at(0))
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))    

    ax2.errorbar(bhw, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax2.errorbar(bhw, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax4.errorbar(bhw, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    print(bhw, meanS , BSES)
    
ax2.tick_params(axis="x",labelsize=10,direction="in")
ax4.tick_params(axis="x",labelsize=10)
ax2.tick_params(axis="y",labelsize=10)
ax4.set_xlabel(r'$ \beta \hbar \omega _0$',fontsize=10,fontweight='bold')

ax2.set_xlim([0.4,1.4])
ax4.set_xlim([0.4,1.4])
ax2.set_ylim([12.5,35])
ax2.set_yticks([15,20,25,30,35])
ax4.set_ylim([-0.05,0.45])
ax2.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
ax4.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')

#ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax4.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

f2.tight_layout()
f2.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'Figure3.pdf', format='pdf', dpi=600)

#
## FIGURE 4 ##
#plt.figure(3, (10,10))
f4, ((ax7,ax8)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = 3
bhws = [1.25, 1.5, 1.75, 2, 2.5, 3, 4, 5, 6]
##bhws = [3, 4, 5, 6]
analytic = [6.89333779, 6.36220084, 6.01473798, 5.77315087, 5.46533286, 5.28532944, 5.10755903, 5.04008246, 5.01482427]

ax7.plot(bhws, analytic, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

lam = 0.0
Nbeads = [12, 12, 12, 12, 12, 72, 72, 72, 72 ,72]
save_meanA=[]
for ind,bhw in enumerate(bhws):    
    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]))
##    print(data)

    if (len(save_data['EF'])>1):
        meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
        Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
        varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
        BSEA = varA/np.sqrt(Neff)
        save_meanA.append(meanA)
        if (bhw > 2.5):
            meanA_corr = np.sum(save_data['Wj'] * save_data['EF_corr'])/np.sum(save_data['Wj'])
            varA_corr = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF_corr']-meanA_corr)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
            BSEA_corr = varA_corr/np.sqrt(Neff)            
    else:
        meanA = save_data['EF']
        BSEA = save_data['Err_EF']
        save_meanA.append(save_data.at(0))
        if ( bhw > 2.5):
            meanA_corr = save_data['EF_corr']
            BSEA_corr = save_data['Err_EF_corr'] 
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))    

    if (bhw <= 2.5):

        ax7.errorbar(bhw, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
        ax8.errorbar(bhw, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        print(bhw, meanA , BSEA)

    else:
        ax7.errorbar(bhw, meanA, BSEA, fmt='oC7', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
        ax7.errorbar(bhw, meanA_corr, BSEA_corr, fmt='oC4', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        ax8.errorbar(bhw, meanS, BSES, fmt='DC5', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        print(bhw, meanA_corr , BSEA_corr)
        
ax7.tick_params(axis="x",labelsize=10,direction="in")
ax8.tick_params(axis="x",labelsize=10)
ax7.tick_params(axis="y",labelsize=10)
ax8.set_xlabel(r'$ \beta \hbar \omega _0$',fontsize=10,fontweight='bold')

##ax7.set_xlim([0.4,1.4])
##ax8.set_xlim([0.4,1.4])
##ax7.set_ylim([12.5,35])
##ax7.set_yticks([15,20,25,30,35])
##ax8.set_ylim([-0.05,0.45])
ax7.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
ax8.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')

#ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax8.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

f4.tight_layout()
f4.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'Figure6.pdf', format='pdf', dpi=600)

## FIGURE 5 ##
##f5, ((ax9,ax10)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})
f5, ax9 = plt.subplots(1,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = 2
bhw = 6

#lambs = [0.0, 0.3, 0.5, 1, 3, 10.0]
gs = [8,12,16]
Nbeads = [72,72,72,72,72]
lam= 0.0
save_meanA=[]

#ax50 = plt.axes([.65, .6, .25, .25])

for ind,g in enumerate(gs):    
    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]) + "_g" +str(g))
##    print(data)

    meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
    BSEA = varA/np.sqrt(Neff)
    save_meanA.append(meanA)

    meanA_corr = np.sum(save_data['Wj'] * save_data['EF_corr'])/np.sum(save_data['Wj'])
    varA_corr = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF_corr']-meanA_corr)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
    BSEA_corr = varA_corr/np.sqrt(Neff)  
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))

    ax9.errorbar(g, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
##    ax9.errorbar(g, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    ax9.errorbar(g, meanA_corr, BSEA_corr, fmt='oC4', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
##    ax10.errorbar(g, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
    #print(g, meanS , BSES)
    #print(save_data)
##    print(bhw, meanA , BSEA)
##    print(save_data)
    
#    if(lam <1):
#        ax50.errorbar(lam, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
#        ax50.errorbar(lam, meanB, BSEB, fmt='oC0', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        #ax50.errorbar(lam, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        
#plt.xticks(fontsize=24)
#plt.yticks(fontsize=24)
ax9.tick_params(axis="x",labelsize=10,direction="in")
##ax10.tick_params(axis="x",labelsize=10)
ax9.tick_params(axis="y",labelsize=10)
##ax10.set_xlabel(r'$ g $',fontsize=10,fontweight='bold')
ax9.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
##ax10.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')
ax9.axhline(3.0049944,color='k')

##mean_Dornheim = [18.5, 21.0, 22.82, 26.80, 40.273]#, 74.587]
##meanS_Dornheim = [0.00258, 0.01861, 0.04184, 0.1475, 0.6717]

##ax1.plot(lambs, mean_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)
#ax3.plot(lambs, meanS_Dornheim, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

#ax50.plot(lambs[:-2], mean_Dornheim[:-2], 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

##ax1.set_ylim([5,45])
##ax3.set_ylim([-0.15,0.75])

f5.tight_layout()
f5.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'FigureS1.pdf', format='pdf', dpi=600)



### FIGURE 4 ##
#plt.figure(4, (10,10))
#
#Natoms = 6
#bhw = 1
#
#lambs = [0.0, 0.3, 0.5, 1]
#Nbeads = [4, 4, 4, 8]
#for ind,lam in enumerate(lambs):    
#    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]))
###    print(data)
#
#    meanA = np.sum(save_data['Wj'] * save_data['EF_corr'])/np.sum(save_data['Wj'])
#    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
#    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF_corr']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
#    BSEA = varA/np.sqrt(Neff)
#
#    plt.errorbar(lam, (meanA-18.5)/18.5*100, (BSEA)/18.5*100, fmt='oC1', capsize=2, markersize=10, mfc='w', linewidth=2.0, mew=2.0)
#    
#    meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
#    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
#    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
#    BSEA = varA/np.sqrt(Neff)
#
#    plt.errorbar(lam, (meanA-18.5)/18.5*100, (BSEA)/18.5*100, fmt='oC0', capsize=2, markersize=10, mfc='w', linewidth=2.0, mew=2.0)
#
#plt.xticks(fontsize=24)
#plt.yticks(fontsize=24)
#plt.xlabel(r'$ \lambda $',fontsize=24,fontweight='bold')
#plt.ylabel(r'$ \Delta E [\%] $',fontsize=24,fontweight='bold')
#

## FIGURE 6 ##
#plt.figure(3, (10,10))
f6, ((ax11,ax12)) = plt.subplots(2,1, figsize=(3.37,3.37),dpi=600,sharex='all',gridspec_kw={'hspace': 0})

Natoms = 2
bhws = [1.25, 1.5, 1.75, 2, 2.5, 3, 4, 3, 4, 5, 6]
bhws_anal = [1.25, 1.5, 1.75, 2, 2.5, 3, 4, 5, 6]
##bhws = [3, 4, 5, 6]
analytic = [4.1608042,  3.78401662, 3.54519567, 3.38766473, 3.2059856, 3.11473104, 3.03865702, 3.01374892, 3.0049944]

ax11.plot(bhws_anal, analytic, 'sC2', markersize=7, mfc='w', linewidth=2.0, mew=2.0)

lam = 0.0
Nbeads = [36, 36, 36, 36, 36, 36, 36, 72, 72, 72 ,72]
save_meanA=[]
for ind,bhw in enumerate(bhws):    
    save_data = pd.read_csv(path + "data_"+str(Natoms) +"p_bhw_"+str(bhw)+ "_lambda_" +str(lam)+ "_P" +str(Nbeads[ind]))
##    print(data)

    meanA = np.sum(save_data['Wj'] * save_data['EF'])/np.sum(save_data['Wj'])
    Neff = np.sum(save_data['Wj'])**2/np.sum(save_data['Wj']**2)
    varA = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF']-meanA)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
    BSEA = varA/np.sqrt(Neff)
    save_meanA.append(meanA)
    if (Nbeads[ind] == 72):
        meanA_corr = np.sum(save_data['Wj'] * save_data['EF_corr'])/np.sum(save_data['Wj'])
        varA_corr = np.sqrt( Neff*np.sum( save_data['Wj']*(save_data['EF_corr']-meanA_corr)**2 )/np.sum(save_data['Wj'])/(Neff-1) )
        BSEA_corr = varA_corr/np.sqrt(Neff)            
    
    meanB = np.mean(save_data['EB'])
    BSEB = np.std(save_data['EB'])/np.sqrt(len(save_data['EB']))
    meanS = np.mean(save_data['sign'])
    BSES = np.std(save_data['sign'])/np.sqrt(len(save_data['sign']))    

    if (Nbeads[ind] == 36):

        ax11.errorbar(bhw, meanA, BSEA, fmt='oC1', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
        ax12.errorbar(bhw, meanS, BSES, fmt='DC3', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        print(bhw, meanA , BSEA)
        if bhw== 4:
            print(save_data['EF'], save_data['sign'])

    else:
        ax11.errorbar(bhw, meanA, BSEA, fmt='oC7', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)    
        ax11.errorbar(bhw, meanA_corr, BSEA_corr, fmt='oC4', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        ax12.errorbar(bhw, meanS, BSES, fmt='DC5', capsize=2, markersize=6, mfc='w', linewidth=2.0, mew=2.0)
        print(bhw, meanA_corr , BSEA_corr)
        
ax11.tick_params(axis="x",labelsize=10,direction="in")
ax12.tick_params(axis="x",labelsize=10)
ax11.tick_params(axis="y",labelsize=10)
ax12.set_xlabel(r'$ \beta \hbar \omega _0$',fontsize=10,fontweight='bold')

##ax7.set_xlim([0.4,1.4])
##ax8.set_xlim([0.4,1.4])
##ax7.set_ylim([12.5,35])
##ax7.set_yticks([15,20,25,30,35])
##ax8.set_ylim([-0.05,0.45])
ax11.set_ylabel(r'$\langle E \rangle / \hbar \omega _0  $',fontsize=10,fontweight='bold')
ax12.set_ylabel(r'$\langle s  \rangle _B$',fontsize=10,fontweight='bold')

#ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax12.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

f6.tight_layout()
f6.savefig('/mnt/storage3/hirshb/NEW_LAMMPS_DATA/FERMIONS_FOCUSED/N6_Dornheim/'+ 'FigureS2.pdf', format='pdf', dpi=600)

