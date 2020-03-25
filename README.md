# sirModel

### SIR(Susceptible, Infectious, Recovered) compartmental model in epidemiology

The system can be expressed by the following set of ordinary differential equations:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{300}&space;\tfrac{dS}{dt}&space;=&space;\tfrac{-\beta&space;IS}{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{300}&space;\tfrac{dS}{dt}&space;=&space;\tfrac{-\beta&space;IS}{N}" title="\tfrac{dS}{dt} = \tfrac{-\beta IS}{N}" /></a> 

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{300}&space;\tfrac{dI}{dt}&space;=&space;\tfrac{\beta&space;IS}{N}&space;-&space;\gamma&space;I" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{300}&space;\tfrac{dI}{dt}&space;=&space;\tfrac{\beta&space;IS}{N}&space;-&space;\gamma&space;I" title="\tfrac{dI}{dt} = \tfrac{\beta IS}{N} - \gamma I" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{300}&space;\tfrac{dR}{dt}&space;=&space;\gamma&space;I" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{300}&space;\tfrac{dR}{dt}&space;=&space;\gamma&space;I" title="\tfrac{dR}{dt} = \gamma I" /></a>


where **S** is the stock of susceptible population, **I** is the stock of infected, **R** is the stock of recovered population, and **N** is the sum of these three.

The system don't have so-called vital dynamics (birth and death).


This is an example of the output running with beta= 0.2 and gamma 0.1 (Basic reproduction mumber, R0=2):

![alt text](https://github.com/AgustinPardo/sirModel/blob/master/Figure_1.png)
