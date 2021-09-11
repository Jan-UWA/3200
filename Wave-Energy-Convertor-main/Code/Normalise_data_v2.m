%
% Code to calculate new performance metric for wave energy converters 
%
% v2 - 13 Aug 2021 (AK): 
% Tidy up code and interface.
% Design period now calculated iteratively.
%

clear
close all

question = 'Has standard data already been calculated?';
qtitle = 'Standard Data';
Standard_Data_answer = questdlg(question, qtitle, 'Yes', 'No', 'No');

% Constants
rho = 1025;
g = 9.80665;

switch Standard_Data_answer
    case 'No'
        f1 = msgbox('Please choose csv or text file to read from');
        uiwait(f1);
        
        [myfile, myfilepath] = uigetfile('*.*');  % prompt user to choose matlab data
        % name of matlab data file containing lambda_hat and da_hat
        M = readmatrix(fullfile(myfilepath, myfile));
        
        figure(1)
        plot((M(:,1)),(M(:,2)));
        
        xdata = M(:,1);
        ydata = M(:,2);
        
        prompt = {'Enter the characteristic dimension in metres:', ...
            'Enter the Submerged Surface Area in square metres:', ...
            'Enter water depth in metres (enter any negative number if water is deep):'};
        dlgtitle = 'Input parameters';
        answer = inputdlg(prompt, dlgtitle);
        
        B = str2double(answer{1});
        SA = str2double(answer{2});
        d = str2double(answer{3});
        
        list = {'T (s)', 'frequency (1/s)', 'rotational frequency (rad/s)', ...
            'k*x', 'T/T0', 'lambda/L'};
        [test, ~] = listdlg('PromptString', 'Select the given unit of x axis', ...
            'SelectionMode', 'single', 'listString', list);
        
        switch test
            
            case 1
                T = xdata;
                
            case 2
                f = xdata;
                T = 1./f;
                
            case 3
                w = xdata;
                T = 2*pi ./w;
                
            case 4
                prompt = ['Enter the value of x (e.g. water depth, ', ...
                    'width, radius) that has been mutiplied by the ', ...
                    'wavenumber, k:'];
                dlgtitle = 'Value of x';
                answer = inputdlg(prompt, dlgtitle);
                
                x8 = str2double(answer);
                
                k_x = xdata;
                k = k_x ./x8;
                w = sqrt(g.*k.*tanh(k.*d));
                if d <0
                    w = sqrt(g.*k);
                end
                T = 2*pi ./w;
                
            case 5
                prompt = ['Enter the value of the resonant ', ...
                    'wavelength (lambda zero):'];
                dlgtitle = 'Resonant wavelength';
                answer = inputdlg(prompt, dlgtitle);
                
                lambda_zero = str2double(answer);
                
                T_normal = xdata;
                k_zero = 2*pi ./lambda_zero;
                w_zero = sqrt(g*k_zero*tanh(k_zero*d));
                T_zero = 2*pi./w_zero;
                T = T_normal*T_zero;
                
            case 6
                prompt = ['Enter the value of L, i.e. the value the ', ...
                    'wavelength has been divided by:'];
                dlgtitle = 'Characteristic length';
                answer = inputdlg(prompt, dlgtitle);
                
                L = str2double(answer);
                
                lambda = xdata*L;
                k = 2*pi ./lambda;
                w = sqrt(g.*k.*tanh(k.*d));
                if d <0
                    w = sqrt(g.*k);
                end
                T = 2*pi ./w;
        end
        
        w = 2*pi ./T;
        
        k = wavenumber3(w, d);
        
        list = {'da (m)', 'da ratio ()', 'Power per square metre (kW/m^2)', ...
            'Power (kW)', 'da*k', 'da/Lambda'};
        [inx, ~] = listdlg('PromptString', 'Select the given unit of y axis', ...
            'SelectionMode', 'single', 'listString', list);
        
        switch inx
            
            case 1
                da = ydata;
                
            case 2
                question = 'Is da ratio presented as a decimal or percentage?';
                qtitle = 'da ratio';
                da_ratio_answer = questdlg(question, qtitle, ...
                    'decimal', 'percentage', 'decimal');
                
                switch da_ratio_answer
                    case 'decimal'
                        c9 = 1;
                    case 'percentage'
                        c9 = 0.01;
                end
                
                da_ratio = ydata*c9;
                da = da_ratio*B;
                
            case 3
                question = 'Is Power in kW or W?';
                qtitle = 'Power unit';
                Power_unit_answer = questdlg(question, qtitle, ...
                    'W', 'kW', 'kW');
                
                switch Power_unit_answer
                    case 'kW'
                        c5 = 1000;
                    case 'W'
                        c5 = 1;
                end
                
                P = ydata;
                
                De = tanh(k*d) + k*d ./ cosh(k*d).^2;   % depth function
                if d < 0
                    De = 1;
                end
                A = 1;
                
                % wave energy transport [W/m]
                J = rho * g^2 * De * A^2 ./ (4 * w);
                
                % capture width
                da = P*c5 ./ J;
                
            case 4
                question = 'Is Power in kW or W?';
                qtitle = 'Power unit';
                Power_unit_answer = questdlg(question, qtitle, ...
                    'W', 'kW', 'kW');
                
                switch Power_unit_answer
                    case 'kW'
                        c5 = 1000;
                    case 'W'
                        c5 = 1;
                end
                
                P = ydata;
                
                prompt = 'Enter incident wave amplitude in metres:';
                dlgtitle = 'Incident wave amplitude';
                answer = inputdlg(prompt, dlgtitle);
                
                A = str2double(answer);

                De = tanh(k*d) + k*d ./ cosh(k*d).^2;
                if d < 0
                    De = 1;
                end
                J = rho * g^2 * De * A^2 ./ (4 * w);
                
                da = P * c5 ./ J;
                
            case 5
                KL = ydata;
                da = KL ./k;
                
            case 6
                %       k = wavenumber3(w, d);
                lambda = 2*pi ./k;
                da_ratio_lambda = ydata;
                da = da_ratio_lambda .*lambda;
        end
        
        % Flip to avoid trapz giving negative values
        if test == 2 || test == 3 || test == 4
            T = flip(T);
            da = flip(da);
        end
        w = 2*pi ./T;
        
        k = wavenumber3(w, d);
        
        lambda = 2*pi ./k;
        
        h2 = figure(2);
        plot(lambda, da);
        xlabel('lambda');
        ylabel('da');
        title('Capture Width vs Wavelength');
        
        % Save output
        f1 = msgbox('Specify folder to save output to');
        uiwait(f1);
        outFolder = uigetdir();
        
        myfile2 = myfile(1:end-4);   
        myfile2dir = fullfile(outFolder, myfile2);
        
        % Save figure
        savefig(h2, myfile2dir); 
        
        % Save data
        save(myfile2dir, 'lambda', 'da', 'SA', 'B', 'T', 'd');
        if inx == 4
            save(myfile2dir, 'A', '-append'); % Save incident wave amp
        end
        
    case 'Yes'
        f1 = msgbox('Please choose mat file to read from');
        uiwait(f1);
        
        [myfile2, myfilepath] = uigetfile('*.mat');
        myfile2dir = fullfile(myfilepath, myfile2);
        load(myfile2dir);
        
        figure(2)
        plot(lambda, da);
        xlabel('lambda');
        ylabel('da');
        title('Capture Width vs Wavelength');
        
        fprintf('Calculating normalised data... \n');
        
        f1 = msgbox('Select folder to save normalised data to');
        uiwait(f1);
        outFolder = uigetdir();
end

[~, name, ~] = fileparts(myfile2dir);


%% 
D = sqrt(SA); % square root of surface area

% Using square root of surface area
T_hat = T * sqrt(g/D);
da_hat = da/D;
lambda_hat = lambda/D;
sigma = sqrt(lambda/D);

% Using characteristic dimension
T_hat2 = T * sqrt(g/B);
da_hat2 = da /B;
lambda_hat2 = lambda/B;
sigma2 = sqrt(lambda/B);

% Various metrics, without integration limits
product = lambda_hat .* da_hat;
NM_lambda_hat = abs(trapz(lambda_hat, product));

product = T_hat .* da_hat;
NM_T_hat = abs(trapz(T_hat, product));

product = sigma .* da_hat;
NM_sigma = abs(trapz(sigma, product));

product = lambda_hat2 .* da_hat2;
NM_lam_hat2 = abs(trapz(lambda_hat2, product));

product = T_hat2 .* da_hat2;
NM_T_hat2 = abs(trapz(T_hat2, product));

product = sigma2 .* da_hat2;
NM_sigma2 = abs(trapz(sigma2, product));

%% Wave period limits

prompt = {'Enter full-scale design period in seconds:', ...
    'Enter full-scale lower cut-off period in seconds:', ...
    'Enter full-scale upper cut-off period in seconds:'};
dlgtitle = 'Design periods';
definput = {'9', '4', '14'}; % Default values (preferred) 
answer = inputdlg(prompt, dlgtitle, 1, definput);

t0 = str2double(answer{1}); % design period (taken as centroid of area under curve) 
tl = str2double(answer{2}); % lower integration limit
tu = str2double(answer{3}); % upper integration limit

%% Using characteristic dimension

product = T_hat2 .* da_hat2;
first_area = abs(trapz(T_hat2, product));

Area = abs(trapz(T_hat2, da_hat2));
t0_hat = first_area / Area; 

t0_hat_old = 0;
countitr2 = 0;

while abs(t0_hat - t0_hat_old) > 1e-3
    t0_hat_old = t0_hat;

    d_scaled2 = g/((t0_hat/t0)^2); % scaled to match design period
    
    tl_hat = tl*sqrt(g/d_scaled2);
    tu_hat = tu*sqrt(g/d_scaled2);
    
    % Apply limits, interpolate, and extrapolate (if necessary)
    T_hat_new = tl_hat:0.01:tu_hat;
    da_hat_new = interp1(T_hat2, da_hat2, T_hat_new, 'linear', 'extrap');
    
    % Calculate metric score
    product = T_hat_new .* da_hat_new;
    first_area = abs(trapz(T_hat_new, product));
    
    Area = abs(trapz(T_hat_new, da_hat_new));
    t0_hat = first_area / Area;
    
    countitr2 = countitr2 + 1;
end

NM_T_hat_withlimit2 = first_area;

%% Using square root of surface area

product2 = T_hat .* da_hat;
first_area = abs(trapz(T_hat, product2));

Area = abs(trapz(T_hat, da_hat));
t0_hat = first_area/Area;

t0_hat_old = 0;
countitr = 0;

while abs(t0_hat - t0_hat_old) > 1e-3
    t0_hat_old = t0_hat;
    
    d_scaled = g/((t0_hat/t0)^2);
    
    tl_hat = tl*sqrt(g/d_scaled);
    tu_hat = tu*sqrt(g/d_scaled);
    
    T_hat_new = tl_hat:0.01:tu_hat;
    da_hat_new = interp1(T_hat, da_hat, T_hat_new, 'linear', 'extrap');
    
    product = T_hat_new .* da_hat_new;
    first_area = abs(trapz(T_hat_new, product));
    
    Area = abs(trapz(T_hat_new, da_hat_new));
    t0_hat = first_area / Area;

    countitr = countitr + 1;
end

NM_T_hat_withlimit = first_area;

%%
figure(3)
subplot(2,1,1)
plot(T_hat_new, da_hat_new, 'g', 'LineWidth', 2)
hold on
plot(T_hat, da_hat, 'b')
title('T hat Vs da hat with set limits and extrapolation')
strx = '$\hat{T}$';
stry = '$\hat{d}_a$';
xlabel(strx, 'Interpreter','Latex')
ylabel(stry, 'Interpreter','Latex')
xlim([0, tu_hat + 3])
ylim([0, max(da_hat)*1.1])
xline(tu_hat)
xline(tl_hat)

subplot(2,1,2)
plot(lambda_hat, da_hat)
ylim([0, max(da_hat)*1.1])
strx = '$\hat{\lambda}$';
stry = '$\hat{d}_a$';
xlabel(strx, 'Interpreter','Latex')
ylabel(stry, 'Interpreter','Latex')

currentfile2 = [name, '_normalised_with_Tlimits'];

currentfile3 = fullfile(outFolder, currentfile2);
savefig(currentfile3);
save(currentfile3, 'da_hat','T_hat','T_hat_new','lambda_hat', ...
    'da_hat_new','NM_T_hat_withlimit','NM_T_hat_withlimit2', ...
    'NM_lambda_hat', 'NM_T_hat', 'NM_sigma', 'NM_sigma2', ...
    'NM_lam_hat2','NM_T_hat2','d_scaled','d_scaled2');

f1 = msgbox('All Data and Figures Saved Successfully');
