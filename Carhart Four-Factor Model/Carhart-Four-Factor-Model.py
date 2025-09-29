from IPython.display import display, Math

# The LaTeX for the Carhart Four-Factor Model
formula = r'E(R_i) = R_f + \beta_{mkt}(E(R_m) - R_f) + \beta_{smb} \cdot SMB + \beta_{hml} \cdot HML + \beta_{mom} \cdot MOM'

display(Math(formula))