function dydt = FRas(Psi,y,cAMP) % right hand side of DE function
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

cAMP = 1000;  %:0.1:10^3;
 % list with parameter values
dydt = [k_R1 * (cAMP + r1) * (R1_tot - y(1,:)) - k_R1 .* y(1,:) ;
k_R2 * (cAMP + r2) * (R2_tot - y(2,:)) - k_R2 .* y(2,:) ;
y(1,:) + y(2,:) ;
kGEF .* y(3,:) - k_GEF .* y(4,:);
kGAP .* y(3,:) - k_GAP .* y(5,:);
kRas .* y(4,:) * (Ras_tot - y(6,:)) - k_Ras .* y(5,:) .* y(6,:);
koff * (RBD_tot - y(7,:)) - kon .* y(6,:) .* y(7,:)];
