
"""
 _____                                                                                                                                  _____ 
( ___ )                                                                                                                                ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   | ████████╗██╗  ██╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗    ██╗███████╗                                                 |   | 
 |   | ╚══██╔══╝██║  ██║██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║██╔════╝                                                 |   | 
 |   |    ██║   ███████║██║███████╗    ██║     ██║   ██║██║  ██║█████╗      ██║███████╗                                                 |   | 
 |   |    ██║   ██╔══██║██║╚════██║    ██║     ██║   ██║██║  ██║██╔══╝      ██║╚════██║                                                 |   | 
 |   |    ██║   ██║  ██║██║███████║    ╚██████╗╚██████╔╝██████╔╝███████╗    ██║███████║                                                 |   | 
 |   |    ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝╚══════╝                                                 |   | 
 |   |                                                                                                                                  |   | 
 |   | ██████╗ ███████╗██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗                                  |   | 
 |   | ██╔══██╗██╔════╝██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝                                  |   | 
 |   | ██║  ██║█████╗  ██║   ██║█████╗  ██║     ██║   ██║██████╔╝█████╗  ██║  ██║    ██████╔╝ ╚████╔╝                                   |   | 
 |   | ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔═══╝ ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝                                    |   | 
 |   | ██████╔╝███████╗ ╚████╔╝ ███████╗███████╗╚██████╔╝██║     ███████╗██████╔╝    ██████╔╝   ██║                                     |   | 
 |   | ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═════╝     ╚═════╝    ╚═╝                                     |   | 
 |   |                                                                                                                                  |   | 
 |   | ██████╗ ██╗  ██╗ ██████╗ ███████╗███╗   ██╗██╗██╗  ██╗     ██╗ █████╗ ███╗   ███╗██╗██████╗ ██████╗ ███████╗███████╗ █████╗ ██╗  |   | 
 |   | ██╔══██╗██║  ██║██╔═══██╗██╔════╝████╗  ██║██║╚██╗██╔╝    ██╔╝██╔══██╗████╗ ████║██║██╔══██╗██╔══██╗██╔════╝╚══███╔╝██╔══██╗╚██╗ |   | 
 |   | ██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║██║ ╚███╔╝     ██║ ███████║██╔████╔██║██║██████╔╝██████╔╝█████╗    ███╔╝ ███████║ ██║ |   | 
 |   | ██╔═══╝ ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║██║ ██╔██╗     ██║ ██╔══██║██║╚██╔╝██║██║██╔══██╗██╔══██╗██╔══╝   ███╔╝  ██╔══██║ ██║ |   | 
 |   | ██║     ██║  ██║╚██████╔╝███████╗██║ ╚████║██║██╔╝ ██╗    ╚██╗██║  ██║██║ ╚═╝ ██║██║██║  ██║██║  ██║███████╗███████╗██║  ██║██╔╝ |   | 
 |   | ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                                                (_____)
"""


def Battery_Storage(REN_GEN_POWER, DEMAND_POWER, INPUT_SIZE_BATT):

    import numpy as np

    DOD = 0.8  # Depth of discharge
    eta_inv = 0.95
    Battery_capacity = INPUT_SIZE_BATT  # MWh   utility scale
    Initial_SOC = 40  # Initial value for the state of charge (SOC)
    SOC_max = 80  # Maximum value for the SOC 
    eta_ch = 0.95  # Charging efficiency
    sigma = 0.005  # Rate of self-discharge
    eta_dch = 0.95 # Discharging efficiency 
    delta_t = 24  # Time interval (Adjust based on the resolution used to analyze)
    cyclic= True # Boolean operator to ensure the SOC remains equal between the end of certain period and start of the next period 

    discharge_duration = 4   # 4-hour duration for discharging

    E_max = float(Battery_capacity)   # MWh
    P_max = E_max / discharge_duration   # MW
    SOC_min = (1 - DOD) * SOC_max   # (%)
    E0 = (Initial_SOC / 100) * E_max
    E_up = (SOC_max / 100) * E_max  # Higehr end
    E_down = (SOC_min / 100) * E_max # Lower end


    REN_GEN_POWER = np.asarray(REN_GEN_POWER, dtype=float)
    DEMAND_POWER = np.asarray(DEMAND_POWER, dtype=float)

    surplus = np.maximum(0, REN_GEN_POWER - DEMAND_POWER)
    deficit = np.maximum(0, DEMAND_POWER - REN_GEN_POWER)

    

    T1 = len(REN_GEN_POWER)


    #=========================================================================================================================================================================================#
    #                                  THE PURPOSE OF THE FOLLOWING FUNCTION IS TO MANAGE POWER DISPATCH CONSIDERING HOURS AHEAD WHICH NEED TO BE SHAVED                                      #                             #
    #=========================================================================================================================================================================================# 


    def simulation (cap):     

        SHAVE_NEED  = (deficit > cap)

        SHAVE_HOUR_FUTUE = np.cumsum(SHAVE_NEED[::-1]).astype(int)[::-1]

        E = E0

        P_grid_values = []                     
        P_PEME_values = []
        P_discharge_values = []
        P_charge_values = []
        Energy_charge_values = []
        Energy_discharge_values = []

        SOC_battery = [100 * E / E_max]
        E_B = [E]


        for t in range(T1):
            
            Surplus_t = surplus[t]
            Need_shave = max(0, deficit[t] - cap)
     

            if Need_shave > 0:    ##### Discharge to meet the cap
                
                P_discharge = min(P_max, Need_shave, max(0, (E - E_down)) * eta_dch / delta_t)
            else:

                P_discharge = 0   

            P_grid = deficit[t] - P_discharge

            
            if P_grid > cap + 1e-6:   
                    
                    return False, None
            
            ##### Charging from Renewable source

            if (Surplus_t > 0) and (SHAVE_HOUR_FUTUE[t] > 0) and (E < E_up - 1e-10):

                P_charge = min(P_max, Surplus_t, max(0, (E_up - E)) / (eta_ch * delta_t))
                
            else:

                P_charge = 0

            ####### Any leftover surplus goes to the PEME 

            P_PEME = max(0 , Surplus_t - P_charge)

            ####### Update energy state of the battery       
           
            E_next = (E * (1.0 - sigma)) + eta_ch * P_charge * delta_t - (P_discharge / eta_dch) * delta_t
        
            if (E_next < E_down - 1e-9) or (E_next > E_up + 1e-9):
                
                return False, None
            
            E = E_next

            P_grid_values.append(P_grid)
            P_PEME_values.append(P_PEME)
            P_discharge_values.append(P_discharge)
            P_charge_values.append(P_charge)
            Energy_charge_values.append(eta_ch * P_charge * delta_t)    # MWh stored
            Energy_discharge_values.append(P_discharge * delta_t)         # MWh delivered
            E_B.append(E)
            SOC_battery.append(100.0 * E / E_max)


            ###### SOC Cyclic true (end = start)

        #if cyclic and (abs(E - E0) > 1e-3): 

            #return False, None

            #print(f"Predicted needed time to shave", SHAVE_HOUR_FUTUE[t])

                  
        P_insufficient = [0.0] * T1
        outputs = [
            P_PEME_values,
            P_grid_values,
            P_discharge_values,
            P_charge_values,
            P_insufficient,
            E_B,
            SOC_battery,
            Energy_charge_values,
            Energy_discharge_values
        ]
        return True, outputs
    


    #=========================================================================================================================================================================================#
    #                                                       FIND THE SMALLEST FEASIBLE CAP BY THE BISECTION METHOD (NUMERICAL METHOD)                                                         #                             
    #=========================================================================================================================================================================================#

    lo = max(0.0, float(np.max(deficit - P_max)))        # lower bound on grid cap (zero import, 100% BESS)
    hi = float(np.max(deficit))                          # at/above this, no discharge is needed
    best_out = None

    for _ in range(60):
        mid = 0.5 * (lo + hi)
        ok, out = simulation (mid)
        if ok:
            best_out = out
            hi = mid   # try shaving further (lower cap)
        else:
            lo = mid   # need a higher cap
        if hi - lo < 1e-10:
            break


    # Fallback if nothing feasible (should be rare)

    if best_out is None:
        # No BESS effect: send all surplus to PEME, grid import = deficit

        P_peme = surplus.tolist()
        P_grid = deficit.tolist()
        zeros = [0.0] * T1
        E_traj = [E0] * (T1 + 1)
        SOCpct = [Initial_SOC] * (T1 + 1)
        best_out = [P_peme, P_grid, zeros, zeros, zeros, E_traj, SOCpct, zeros, zeros]

    return best_out        
          