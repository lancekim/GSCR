%TRS INPUT
%This is the input interface for TRS
%The structure of the function is
%[t dTE ttb RRmax X]=TRS(Q,RQ,DT,L,rw,b,K,ne,J,theta,rhocs,rhocw,ds,Dt,tend,PT,nPT)

%The outputs are:
%- t are the timesteps [d]
%- dTE is the temperature variation in the extraction well [K]
%- ttb is the thermal breakthrough time [d]
%- RRmax is the maximum recirculated flow rate fraction [-]
%- X is the thermal breakthrough parameter X=2Q/(pi*k*b*J*L) [-]

%The input parameters are:
%- Q is the flow rate [m3/s]
%- RQ is the reinjected flow rate fraction (values: 0÷1)
%- DT is the temperature difference [K] between the extraction 
%and the injection well (i.e. positive for cooling plants)
%- L is the well distance [m]
%- rw is the well radius [m]
%- b is the aquifer thickness [m]
%- K is the hydraulic conductivity [m/s]
%- ne is the effective porosity [-]
%- J is the hydraulic gradient in the aquifer [-]
%- theta is the hydraulic flow angle (radians measured counterclockwise
%from the conjunction line between extraction and injection well)
%- rhocs is the thermal capacity of the solid matrix of the soil [MJ/(m3K)]
%- rhocw is the thermal capacity of groundwater (usually 4.2 MJ/(m3K))
%- ds is the spatial step adopted for the calculation of the pathlines [m]
%- Dt is the time step adopted for the calculation of the water temperature[d]
%- tend is the final time for the calculation of the water temperature [d]
%- PT is the option for the particle pathlines to be plotted (PT=1) or not
%(PT=0)
%- nPT is the step for the particles pathlines to be skipped when plotting
%(e.g. nPT=3 means that one pathline on three will be plotted)

%Further information can be found on
%Casasso A., Sethi R., 2014, Modelling thermal recycling occurring in Groundwater
%Heat Pumps (GWHPs), Renewable Energy, in press

%For any trouble or bug report, please write to
%alessandro.casasso[at]polito.it
%
%DISCLAIMER
%The code is free of charge, even for commercial use.
%The authors decline any responsibility for its use.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Assign the input parameters and select the output here:
Q=0.103009;         % [m3/s] well flow rate
RQ=1;           % [-] reinjected flow rate fraction (values: 0÷1) 
DT=70;           % [K] temperature difference between the extraction and injection well
L=1000;           % [m] well distance
rw=0.25;        % [m] well radius
b=50;           % [m] aquifer thickness
K=2E-5;         % [m/s] hydraulic conductivity
ne=0.14;         % [-] effective porosity
J=0.01;        % [-] aquifer hydraulic gradient
theta=0;        % [rad] hydraulic flow angle (radians measured counterclockwise from the conjunction line between extraction and injection well)
rhocs=2.289;      % [MJ/(m3K)] thermal capacity of the solid matrix of the soil
rhocw=4.2;      % [MJ/(m3K)] thermal capacity of groundwater
ds=0.25;        % [m] spatial step for the calculation of the pathlines
Dt=0.5;         % [d] timestep adopted for the calculation of the water temperature
tend=365*10; % [d] final time
PT=1;           % select 1 to plot the pathlines or 0 to avoid the plotting of pathlines
nPT=10;          % number of pathlines to be skipped in the plot 

[t dTE ttb RRmax X]=TRS(Q,RQ,DT,L,rw,b,K,ne,J,theta,rhocs,rhocw,ds,Dt,tend,PT,nPT);




