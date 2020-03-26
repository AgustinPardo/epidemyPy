# epidemyPy

### SIR(Susceptible, Infectious, Recovered) compartmental model in epidemiology


<img src="https://docs.google.com/drawings/d/1NWG2WbfMzvFtk4DH1_-G1MgRGpo_cAl8piFJrNjRLpY/export/png"/>

The system can be expressed by the following set of ordinary differential equations:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{120}&space;\\\&space;\bullet&space;\;&space;\frac{dS}{dt}&space;=&space;-&space;\frac{\beta&space;IS}{N}&space;\\&space;\\\&space;\bullet&space;\;&space;\frac{dI}{dt}&space;=&space;\frac{\beta&space;IS}{N}&space;-&space;\gamma&space;I&space;\\&space;\\&space;\&space;\bullet&space;\;&space;\frac{dR}{dt}&space;=&space;\gamma&space;I" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;\\\&space;\bullet&space;\;&space;\frac{dS}{dt}&space;=&space;-&space;\frac{\beta&space;IS}{N}&space;\\&space;\\\&space;\bullet&space;\;&space;\frac{dI}{dt}&space;=&space;\frac{\beta&space;IS}{N}&space;-&space;\gamma&space;I&space;\\&space;\\&space;\&space;\bullet&space;\;&space;\frac{dR}{dt}&space;=&space;\gamma&space;I" title="\\\ \bullet \; \frac{dS}{dt} = - \frac{\beta IS}{N} \\ \\\ \bullet \; \frac{dI}{dt} = \frac{\beta IS}{N} - \gamma I \\ \\ \ \bullet \; \frac{dR}{dt} = \gamma I" /></a>


where **S** is the stock of susceptible population, **I** is the stock of infected, **R** is the stock of recovered population, and **N** is the sum of these three.

The system don't have so-called vital dynamics (birth and death).

This is an example of the output running with beta= 0.2 and gamma 0.1 (Basic reproduction mumber, R0=2):
![alt text](https://github.com/AgustinPardo/sirModel/blob/master/Figure_1.png)
