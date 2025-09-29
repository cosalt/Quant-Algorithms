from IPython.display import display, Math

# The LaTeX for the Fama-French Three-Factor Model
formula = r'E(R_i) = R_f + \beta_{mkt}(E(R_m) - R_f) + \beta_{smb} \cdot SMB + \beta_{hml} \cdot HML'

display(Math(formula))