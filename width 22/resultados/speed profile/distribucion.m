clc 
clear all

load tf_config_density9_width22.txt;
data=tf_config_density9_width22;

si=size(data,1);

ancho = 22.0;
bin = 1.0;
f = ancho / bin;

y = zeros(1,f);
v = zeros(1,f);

vec_v=zeros(1,floor(si/2));
vec_y=zeros(1,floor(si/2));

matriz=zeros(f,floor(si/2));
vec_b=zeros(1,f);

a = 1;

for i=floor(si/2):si 
    vv = sqrt(data(i,3)*data(i,3)+data(i,4)*data(i,4));
    ybin = floor(data(i,2)/bin)+1;
    
    vec_b(ybin)=vec_b(ybin)+1;
    matriz(ybin,vec_b(ybin))=vv;
    
    y(ybin) = y(ybin) + 1;
    v(ybin) = v(ybin) + vv;
    
    vec_v(a)= vv;
    vec_y(a)= data(i,2);
    
    a = a+1;
end

vprom = zeros(1,f);

for i=1:f
    if y(i)>0
      vprom(i) = v(i) / y(i);
    end
end

y=zeros(1,f);
media=zeros(1,f);
err=zeros(1,f);

for i=1:f
    y(i)=i*bin;
    if vec_b(i)>0
      media(i)=mean(matriz(i,1:vec_b(i)));
      err(i)=std(matriz(i,1:vec_b(i)));
    end
 end

T = [y' media' err'];

length(data)
dlmwrite('speed_profile_w22_density9_kappa96.txt',T,'delimiter','\t','precision',3,'-append');


plot(bin-bin/2:bin:ancho-bin/2,media,'Linewidth',3);
hold on
errorbar(bin-bin/2:bin:ancho-bin/2,media,err);