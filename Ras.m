
% De IVP solver
R1_tot = 0.1;
R2_tot = 0.9;
kR1 = 0.00267;
k_R1 = 0.16;
kR2 = 0.00244;
k_R2 = 1.1;
r1 = 0.012;
r2 = 0.115;
kGEF = 0.04;
k_GEF = 0.4;
kGAP = 0.01;
k_GAP = 0.1;
Ras_tot = 1;
kRas = 390;
k_Ras = 3126;
RBD_tot = 1;
koff = 0.53;
kon = 1;
Tend = 30;
cAMP = 20;  %:0.1:10^3;
y0 = [0.09594; 1.27; 1.155; 4.405; 0.7; 0.2; 1.16];
tspan = [0 Tend]; 
options = odeset('RelTol',10^-6,'AbsTol',10^-7,'Vectorized','on');
[t,y] = ode45(@FRas,tspan,y0,options,cAMP); % using DE integrator ode...
y(:,3);

plot(t,y(:,1),'b')%, v = axis;

plot(t,y(:,2),'b')

plot(t,y(:,3),'b')

plot(t,y(:,4),'b')

plot(t,y(:,5),'b')

plot(t,y(:,6),'b')

% hold on
plot(t,y(:,7),'r')

plot(y(:,4),y(:,6),'b')

