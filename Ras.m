% [t, y] = neurocycle(hf,Tend,y0,S)
% Sample call : [t,y] = neurocycle(0.004554,20);
% Input : hf = hydrogen ion concentration of input
% Tend = end of time interval for integration
% y0 = initial value column vector,
% with entries for h_1, s_11, s_21, s_31, h_2, s_12, s_22, s_32
% S = color choice for graphs, such as �r� for red, �g� for green etc

% standard : if "standard" is set to 1, we use the standard initial
% values from the book (section 4.4);
% if "standard" is set different from 1, we use special
% initial values and annotate the graphs differently.
% Output: Three different plots are obtainable by (un)commenting :
% First plotting block active:
% Graphs of all 8 profiles for 0 <= t <= Tend in an 8 window plot
% Second plotting block active:
% Phase plot of acetylcholine concentrations in (I) versus (II),
% after limit cycle has been reached (for t >= 0.4 * Tend)
% Third plotting block active:
% s_12 profile and phase plot for 0 <= t <= Tend
% Use the MATLAB text editor ("Text" help button) to (un)comment the
% three plotting blocks so that ONLY ONE is active.
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
%  clf, 
% subplot(4,2,1) 
plot(t,y(:,1),'b')%, v = axis;
%  xlabel('t','FontSize',11); ylabel('h_1' ,'FontSize',12,'Rotation',0);
%  title('Hydrogen ion concentration in (I)','FontSize',12);
%  %if standard == 1,
%  text(v(1)+0*(v(2)-v(1)),v(4)+0.26*(v(4)-v(3)),...
%  ['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
%  ' and the standard initial value \Psi(0)'],'FontSize',14);
%  %else,
%  %text(v(1)+0*(v(2)-v(1)),v(4)+0.32*(v(4)-v(3)),...
%  %['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
%  %' and initial value'],'FontSize',14);
%  %text(v(1)+0.1*(v(2)-v(1)),v(4)+0.21*(v(4)-v(3)),...
%  %['\Psi(0) = ',num2str(y0','%7.5g')],'FontSize',14); end
%  subplot(4,2,3)
plot(t,y(:,2),'b')
%  xlabel('t','FontSize',11); ylabel('s_{11} ','FontSize',12,'Rotation',0);
%  title('Acetylcholine concentration in (I)','FontSize',12);
%  subplot(4,2,5)
plot(t,y(:,3),'b')
%  xlabel('t','FontSize',11); ylabel('s_{21} ','FontSize',12,'Rotation',0);
%  title('Choline concentration in (I)','FontSize',12);
%  subplot(4,2,7)
plot(t,y(:,4),'b')
%  xlabel('t','FontSize',11); ylabel('s_{31} ','FontSize',12,'Rotation',0);
%  title('Acetate concentration in (I)','FontSize',12);
%  subplot(4,2,2)
plot(t,y(:,5),'b')
%  xlabel('t','FontSize',11); ylabel('h_2 ','FontSize',12,'Rotation',0);
%  title('Hydrogen ion concentration in (II)','FontSize',12);
%  subplot(4,2,4)
plot(t,y(:,6),'b')
% xlabel('t','FontSize',11); ylabel('RasGTP','FontSize',12,'Rotation',90);
% title('Time Course of RasGTP for incoherent FFL after sudden increase in chemoattractant at 0s','FontSize',12);
%  subplot(4,2,6)
% hold on
plot(t,y(:,7),'r')
% xlabel('t','FontSize',11); ylabel('RBD_{cyt}','FontSize',12,'Rotation',90);
% title('RBD-GFP concentration for different cAMP concentration}','FontSize',12);

%  subplot(4,2,8)
%  plot(t,y(:,8),'b')
%  xlabel('t','FontSize',11); ylabel('s_{32} ','FontSize',12,'Rotation',0);
%  title('Acetate concentration in (II)','FontSize',12);
%  clf, subplot(2,1,1), 
%  plot(t,y(:,6),'b'), v = axis;
%  xlabel('t','FontSize',11); ylabel('s_{12} ','FontSize',12,'Rotation',0);
%  %if standard == 1,
%  text(v(1)+0*(v(2)-v(1)),v(4)+0.11*(v(4)-v(3)),...
%  ['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
%  ' and the standard initial value \Psi(0)'],'FontSize',14);
%  %else, text(v(1)+0.05*(v(2)-v(1)),v(4)+0.135*(v(4)-v(3)),...
%  %['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
%  %' and initial value'],'Fontsize',14)
%  %text(v(1)+0.1*(v(2)-v(1)),v(4)+0.082*(v(4)-v(3)),...
%  %['\Psi(0) = ',num2str(y0','%7.5g')],'FontSize',14); end
%  title('Acetylcholine concentration in (II)','FontSize',12);
%  subplot(2,1,2)
plot(y(:,4),y(:,6),'b')
%  xlabel([{' '},{['s_{11} ( for 0 \leq t \leq ',...
%  num2str(Tend,'%7.5g'),' )']}],'FontSize',12)
%  ylabel('s_{12} ','FontSize',12,'Rotation',0);
%  title('Phase plot of acetylcholine concentrations in (I) versus in (II)',...
%  'FontSize',12)
% clf, 
% k = length(t); Tstart = floor(0.4*k);
% plot(y(Tstart:end,4),y(Tstart:end,6)), v = axis;
% %if standard == 1,
% text(v(1)+0*(v(2)-v(1)),v(4)+0.046*(v(4)-v(3)),...
% ['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
% ' and the standard initial value \Psi(0)'],'FontSize',14);
% %else,
% %text(v(1)+0.08*(v(2)-v(1)),v(4)+0.056*(v(4)-v(3)),...
% %['Neurocycle enzyme system with h_f = ',num2str(hf,'%10.7g'),...
% %' and initial value'],'Fontsize',14)
% %text(v(1)+0.1*(v(2)-v(1)),v(4)+0.036*(v(4)-v(3)),...
% %['\Psi(0) = ',num2str(y0','%7.5g')],'FontSize',14); end
% xlabel([{' '},{['s_{11} ( for ',num2str(t(Tstart),'%7.5g'),...
% ' \leq t \leq ',num2str(Tend,'%7.5g'),' )']}],'FontSize',12);
% ylabel('s_{12} ','FontSize',12,'Rotation',0);
% title('Phase plot of acetylcholine concentrations in (I) versus in (II)',...
% 'FontSize',12);
