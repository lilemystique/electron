Data = fileread('new 28.txt');
Data = strrep(Data, ',', '.');
FID = fopen('28.txt', 'w+');
fwrite(FID, Data, 'char'); 
fclose(FID);

M = readtable('28.txt');
S.Var2 = mean(M{:,'Var2'}, 'all', 'default');

gr = groupfilter(M, 'Var1', @(x) max(x)<= S.Var2);

x=gr{:, 'Var1'};
y=gr{:, 'Var2'};

plot(x,y);
title('graph')
ylabel('y')
xlabel('x')




