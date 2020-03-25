# sirModel

### SIR(Susceptible, Infectious, Recovered) compartmental model in epidemiology

The system can be expressed by the following set of ordinary differential equations:


```Latex

\tfrac{dS}{dt} = \tfrac{-\beta IS}{N}

\tfrac{dI}{dt} = \tfrac{\beta IS}{N} - \gamma I

\tfrac{dR}{dt} = \gamma I
```

where **S** is the stock of susceptible population, **I** is the stock of infected, **R** is the stock of recovered population, and **N** is the sum of these three.

The system don't have so-called vital dynamics (birth and death.

![alt text](https://github.com/AgustinPardo/sirModel/blob/master/Figure_1.png)
