%Dynamic slider allows us to manipulate the max camber value in the
%af_fn.m script to visualise the affect on the geometry of the aerofoil.

function sliderAirfoil
FigH = figure('position',[360 500 400 400]);
axes('XLim', [0 1], 'units','pixels', ...
     'position',[100 50 200 200], 'NextPlot', 'add');
[x,y,camberx,cambery] = af_fn(0);
LineH = plot(x,y,'r-');
LineA = plot(camberx,cambery,'b-');
title('Geometry deformation vs Max Camber length')
TextH = uicontrol('style','text',...
    'position',[170 340 40 15]);
SliderH = uicontrol('style','slider','position',[100 280 200 20],...
    'min', 0, 'max', 10);
addlistener(SliderH, 'Value', 'PostSet', @callbackfn);
movegui(FigH, 'center')
    function callbackfn(source, eventdata)
    num          = get(eventdata.AffectedObject, 'Value');
    [z1,z2,camberx,cambery] = af_fn(num);
    LineH.YData  = z2;
    TextH.String = num2str(num);
    LineA.YData  = cambery;
    TextA.String = num2str(cambery);
    end
  end