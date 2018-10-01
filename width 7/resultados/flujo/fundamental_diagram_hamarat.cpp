#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

#define PI 3.14159265359

/*
Este codigo toma el archivo de configuraciones (posiciones x y para todos los individuos dentro del recinto
para cada instante de tiempo - segun cada cuanto se haga el dump en lammps). 
Devuelve una tabla con 3 columnas: tiempo, cantidad de individuos en el recinto y densidad en la zona cercana a la puerta
El centro de la puerta y el radio del semicirculo que sirve para calcular la densidad se pasan como parametros 

*/

double function_f(double x, double y, double x_center, double y_center, double R);
void function_flujo(double function_f, double vx, double vy,vector<double> &vector_flujo);
void escribir(vector<double> &vector_time,vector<int> &vector_N, vector<double> &vector_density,vector<double> &vector_flow_x,int n_samples,int density);

int main(int argc, char const *argv[]){
	for (int density_raw = 1; density_raw < 10; ++density_raw){
		char buffer [50];
  		sprintf (buffer, "config_density%d_width7", density_raw);

		int n_samples = 0;
		vector<double> vector_time;
		vector<int> vector_N;
		vector<double> vector_density;
		vector<double> vector_flow_x;
		string archivoDatos;
		double integration_step = 0.0001;
		double R = 1.0;  		 
		double x_center =  14.0;  
		double y_center = 3.5;   
		archivoDatos = buffer;
		
		string line;
		int cantAtoms, n_time,i;
		double x,y,vx,vy;

		ifstream fileIn(archivoDatos.c_str());

		while(fileIn.good()){

			getline(fileIn,line,'P');
			getline(fileIn,line,'I');
			n_time=atoi(line.c_str());
			vector_time.push_back(n_time*integration_step);
			getline(fileIn,line,'S');
			getline(fileIn,line,'I');
			cantAtoms=atoi(line.c_str());
			vector_N.push_back (cantAtoms);
			getline(fileIn,line,'y');
			getline(fileIn,line,'y');
			getline(fileIn,line,' ');		
			// Inicializacion //
			i = 0;
			double density = 0.0;
			vector<double> vector_flujo(2,0.0);
			/////////////////////
			while(i<cantAtoms){		
				getline(fileIn,line,' ');
				x=atof(line.c_str());
				getline(fileIn,line,' ');
				y=atof(line.c_str());
				getline(fileIn,line,' ');
				vx=atof(line.c_str());
				getline(fileIn,line,' ');
				vy=atof(line.c_str());

				double f = 0.0;
				f = function_f(x,y,x_center,y_center,R);
				density = density + f;

				function_flujo(f,vx, vy,vector_flujo); 
				i++;
			}
			vector_density.push_back(density);
			vector_flow_x.push_back(vector_flujo[0]);		
			n_samples++;

		}
		fileIn.close();
		escribir(vector_time,vector_N,vector_density,vector_flow_x,n_samples,density_raw);
	}
	
}


// formula 1 del paper de Helbing
double function_f(double x, double y, double x_center, double y_center,double R){

	double dx = x-x_center;
	double dy = y-y_center;
	double dist2 = dx*dx + dy*dy;
	double area = PI*R*R;
	double f = exp(-dist2/(R*R))/area;
	//printf("%lg\n",f);
	return f;
}

// Formula 7 del paper de Helbing 
void function_flujo(double function_f, double vx, double vy,vector<double> &vector_flujo){

	vector_flujo[0] +=  vx*function_f;
	vector_flujo[1] +=  vy*function_f;

}


void escribir(vector<double> &vector_time,vector<int> &vector_N, vector<double> &vector_density,vector<double> &vector_flow_x,int n_samples,int density){
	
	FILE *fp;
	char buffer [50];
	sprintf (buffer, "density_flow_%d_vd1_pasillo7m.txt", density); 
	fp=fopen(buffer,"w");
	for (int i = 0; i < n_samples; ++i){
		fprintf(fp,"%.2f %i %.3f %.3f\n",vector_time[i],vector_N[i],vector_density[i],vector_flow_x[i]);
	}
	fclose(fp);
}

