import numpy as np 
def sharpe_ratio(returns): 
    return (returns.mean()/returns.std())*(252**0.5) 
