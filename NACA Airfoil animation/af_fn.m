function [ x,y,camberx,cambery ] = af_fn(M)
% This function manipulates the defining values of a NACA MPXX airfoil
% to create (x,y) coordinates for the mean camber line and (x,y)
% coordinates for the aerofoil geometry.
%
% Where we define:
% M = Maximum Camber length as a percentage of the Chord (M/100)
% P = Position at which Maximum Camber occurs along the Chord (P/10)
% XX = The thickness over which this maximum camber is distributed
% as a percentage of the chord length (XX/100). i.e. If XX is larger, the
% airfoil is fatter around the position of the maximum camber.
%
%
%


M=M/100;
P = 6/10;
XX=20/100;
x1 = linspace(0,P,100); % 0 < x < P
x2 = linspace(P,1,100); % P < x < 1

%Defining the equations for the mean camber line
yc1 = @(x) M/P.^2 * (2*P*x - x.^2); % Defined for 0 < x < P
yc2 = @(x) M/(1-P).^2 * (1 - 2*P + 2*P*x -x.^2); % Defined for  P < x < 1

%Define derivatives of the mean camber line
dyc1dx = @(x) 2*M/P.^2*(P-x); % Defined for 0 < x < P
dyc2dx = @(x) 2*M/(1-P).^2*(P-x); % Defined for  P < x < 1

%Angles between perpendicular
theta1 = @(x) atan(dyc1dx(x)); % Defined for 0 < x < P
theta2 = @(x) atan(dyc2dx(x)); % Defined for  P < x < 1


%Thickness distribution along mean camber line
a = [0.2969,-0.1260,-0.3516,0.2843,-0.1036];
yt = @(x) XX/0.2*(a(1)*x.^(1/2) + a(2)*x + a(3) *x.^2 + a(4) *x.^3 + a(5) *x.^4);

%Use thickness dist to determine upper and lower airfoil surface (x,y)
%coords
x = [x1,x2];
theta = [theta1(x1),theta2(x2)];
yc = [yc1(x1),yc2(x2)];

xu = x - yt(x).*sin(theta);
yu = yc+yt(x).*cos(theta);

xl = x + yt(x).*sin(theta);
yl = yc - yt(x).*cos(theta);

% Plot airfoil coords
%plot(xu,yu,'.')
%hold on
%plot(xl,yl,'.')


% %Plot mean camberline
% hold on
%  plot(x1,yc1(x1),'-r')
% hold on
% plot(x2,yc2(x2),'-r')

%Group coords
x = [xu,xl];
y = [yu,yl];
camberx = [x1,x2];
cambery = [yc1(x1),yc2(x2)];


end

