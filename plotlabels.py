class Labels(object):
    def __init__(self):
        self.time = r'Time $t$ [s]'
        self.timeInHours = r'Time $t$ [h]'
        self.degreeOfSwelling = r'Degree of swelling $q$ [-]'
        self.saltMassFraction = r'Salt mass fraction $c^{F_s}\,[\mathrm{m}\%]$'
        self.psiw = r'Cumulative activity coefficient $\psi^w$ [-]'
        self.gammaw0 = r'$\Gamma^w_0$ [kg/(m$^3$\,s)]'
        self.tauw = r'Characteristic transfer time $\tau^w$ [s]'
        self.numberOfExperiment = r'Number of experiment [-]'
        self.equilibriumDegreeOfSwelling = r'Equilibrium Degree of Swelling $q^\infty$ [-]'
        self.dmuMixRT = r'$\Delta\mu^w_{mix} / (RT)$ [-]'
        self.gelSaturation = r'Norm. gel saturation $s^G_{out} / \bar{s}^G_{in,max}$ [-]'
        self.gelSaturationAtPoint = r'norm. gel saturation $s^G / \bar{s}^G_{in,max}$ [-]'
        self.poreVolumesInjected = r'Pore Volumes Injected $\mathit{PVI}$ [-]'
        self.darcyVelocity = r'Darcy velocity $|\mathbf{q}|$ [m/s]'
        self.revAttachmentRate = r'Norm. attachment rate $k_{a,rev} / |\mathbf{q}|$ [-]'
        self.revAttachmentVolumeFraction = r'Rev. attachment $n^{A}_{rev,eq}$ [-]'
        self.flowRate = r'Flow rate $Q$ [ml/min]'
        self.porousMediaShearRate = r'Porous media shear rate $\dot{\gamma}_{pm}$ [1/s]'
        self.viscosityIncreaseFactor = r'Viscosity Increase Factor $\mathit{VIF}$ [-]'
        self.shearRate = r'Shear rate $\dot{\gamma}$ [1/s]'
        self.effectiveViscositySuspension = r'Effective viscosity $\mu^{LR}$ [Pa\,s]'
        self.attachedPolymerVolumeFraction = r'Attached Polymer $n^{A}_{k} / n^{A}_{k,crit}$ [-]'
        self.attachmentFunction = r'Attachment Function $\psi_{a,k}$ [-]'
        self.effectivePorosity = r'Effective porosity $n^L$ [-]'
        self.normalizedPermeability = r'Normalized permeability $k^S/k^S_0$ [-]'
        self.shearStress = r'Shear stress $\tau_{eff}$ [Pa]'
        self.molarConcentration = r'Molar concentration $c_m$ [mol/l]'