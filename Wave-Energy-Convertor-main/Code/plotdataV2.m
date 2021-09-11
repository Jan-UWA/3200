%
% Plot da_hat vs lambda_hat
%
clear
close all

clear
close all

figure(1)
xlabel('lambda hat')
ylabel('da hat')
hold on

figure(2)
str = '$$ \hat{T} $$';
str1 = '$$ \hat{d}_a $$';
xlabel(str, 'Interpreter','Latex')
ylabel(str1, 'Interpreter','Latex')
hold on
% ax.XAxis.FontSize = 15;
% ax.YAxis.Fontsize = 24;
set(gca,'FontSize',23)

g = 9.80665;


  fprintf('Select Folder to read from:\n');
  
    myFolder = uigetdir(); % Ask for a new one.

        
%  f1 = msgbox('Select folder to save output data to');
%  uiwait(f1);
%  outFolder = uigetdir();
% Get a list of all files in the folder with the desired file name pattern.

f1 = msgbox('Select folder to save output data to');
uiwait(f1);
outFolder = uigetdir();
% Get a list of all files in the folder with the desired file name pattern.

filePattern = fullfile(myFolder, '*.mat'); % Change to whatever pattern you need.
theFiles = dir(filePattern);
legendTitle = cell(1,length(theFiles));
for k = 1 : length(theFiles)
    baseFileName = theFiles(k).name;
    fullFileName = fullfile(theFiles(k).folder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    
     filename = baseFileName;
    load(filename);
     filename = filename(1:end-4);
    figure(1); plot(lambda_hat, da_hat, 'linewidth', 4)
        legendTitle{1,k} = filename;
    
        figure(2); plot(T_hat_new, da_hat_new, 'linewidth', 4)
  
        legendTitle{1,k} = filename;
end
figure(1); clickableLegend([legendTitle]);
figure(2); clickableLegend([legendTitle]);

   % Save data
[pathstr,name,ext] = fileparts(myFolder);
  myfile2dir = fullfile(outFolder, name);
 savefig(myfile2dir);