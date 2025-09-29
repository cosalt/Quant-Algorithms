# The Carhart Four-Factor Model

The Carhart Four-Factor Model is an extension of the Fama-French Three-Factor Model, introducing an additional factor to account for **momentum**. Developed by Mark Carhart in 1997, the model is widely used in quantitative finance, particularly for analyzing the performance of mutual funds.

Carhart added the momentum factor to address the empirical tendency for stocks that have performed well in the recent past to continue performing well, and for past underperformers to continue underperforming. This phenomenon, often described as "winners keep winning, losers keep losing," was not captured by the Fama-French factors.

## The Formula

The expected return is calculated by adding the momentum factor to the Fama-French model:

$$
E(R_i) = R_f + \beta_{mkt}(E(R_m) - R_f) + \beta_{smb} \cdot SMB + \beta_{hml} \cdot HML + \beta_{mom} \cdot MOM
$$

## Components of the Formula

The model includes all components from the Fama-French model plus the new momentum factor:

-   **$E(R_i)$**: The **expected return** of the investment.
-   **$R_f$**: The **risk-free rate** of return.
-   **$\beta_{mkt}$**, **$\beta_{smb}$**, **$\beta_{hml}$**: Betas for the **market**, **size (SMB)**, and **value (HML)** factors, respectively.
-   **$(E(R_m) - R_f)$**: The **market risk premium**.
-   **$SMB$** and **$HML$**: The **size** and **value** risk factor premiums.
-   **$MOM$ ("Momentum")**: This is the momentum factor. It represents the historical excess return of a portfolio of past winners over a portfolio of past losers, typically constructed using the prior 12 months of returns.
-   **$\beta_{mom}$**: Measures the asset's sensitivity to the momentum factor (MOM). A positive value indicates the asset's returns tend to move with other high-momentum stocks.

## Python Implementation Example

The calculation is a straightforward extension of the Fama-French model, incorporating the fourth factor and its corresponding beta.

```python
def calculate_carhart_4(risk_free_rate, market_return, beta_mkt, beta_smb, beta_hml, beta_mom, smb_premium, hml_premium, mom_premium):
    """
    Calculates the expected return of an asset using the Carhart Four-Factor Model.

    Args:
        risk_free_rate (float): The risk-free rate of return.
        market_return (float): The expected return of the market.
        beta_mkt (float): The market beta of the asset.
        beta_smb (float): The SMB (size) beta of the asset.
        beta_hml (float): The HML (value) beta of the asset.
        beta_mom (float): The MOM (momentum) beta of the asset.
        smb_premium (float): The SMB factor risk premium.
        hml_premium (float): The HML factor risk premium.
        mom_premium (float): The MOM factor risk premium.

    Returns:
        float: The expected return of the asset.
    """
    market_risk_premium = market_return - risk_free_rate
    expected_return = (risk_free_rate + 
                       (beta_mkt * market_risk_premium) + 
                       (beta_smb * smb_premium) + 
                       (beta_hml * hml_premium) + 
                       (beta_mom * mom_premium))
    return expected_return

# --- Example Usage ---
# Given:
# Risk-Free Rate
rf = 0.02
# Expected Market Return
rm = 0.08

# Factor Premiums (historical averages, for example)
smb = 0.025
hml = 0.04
mom = 0.03  # Momentum stocks are expected to outperform by 3%

# Betas for a specific high-momentum stock
b_mkt = 1.1
b_smb = -0.2 # This stock behaves more like a large-cap stock
b_hml = 0.1  # Slight tilt towards value
b_mom = 1.4  # Very strong sensitivity to the momentum factor

# Calculate expected return
expected_stock_return = calculate_carhart_4(
    risk_free_rate=rf,
    market_return=rm,
    beta_mkt=b_mkt,
    beta_smb=b_smb,
    beta_hml=b_hml,
    beta_mom=b_mom,
    smb_premium=smb,
    hml_premium=hml,
    mom_premium=mom
)

print(f"Expected Return (Carhart-4): {expected_stock_return:.4f}")
# Expected output: Expected Return (Carhart-4): 0.1270