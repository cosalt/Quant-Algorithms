# The Fama-French Three-Factor Model

This folder contains the Fama-French Three-Factor Model Python script and related Jupyter notebook for quantitative analysis.

- `Fama-French-Three-Factor-Model.py`: Python implementation of the CAPM model.
- `ipython.ipynb`: Jupyter notebook for interactive analysis and visualization.

The Fama-French Three-Factor Model is a widely recognized asset pricing model that expands on the Capital Asset Pricing Model (CAPM) by adding two additional risk factors to better explain stock returns. Developed by Eugene Fama and Kenneth French, the model asserts that beyond the market risk captured by CAPM, the returns of a diversified portfolio are also sensitive to the risks associated with company size and value.

The model arose from the empirical observation that, over time, small-cap stocks and value stocks (those with a high book-to-market ratio) have tended to outperform the overall market.

## The Formula

The expected return of an asset is calculated using the following linear relationship:

$$
E(R_i) = R_f + \beta_{mkt}(E(R_m) - R_f) + \beta_{smb} \cdot SMB + \beta_{hml} \cdot HML
$$

## Components of the Formula

The model includes the standard CAPM components plus two new factors:

-   **$E(R_i)$**: The **expected return** of the investment.
-   **$R_f$**: The **risk-free rate** of return.
-   **$\beta_{mkt}$**: The **beta** of the investment with respect to the market risk (identical to the beta in CAPM).
-   **$(E(R_m) - R_f)$**: The **market risk premium**.
-   **$SMB$ ("Small Minus Big")**: This is the size risk factor. It represents the historical excess return of small-cap companies over large-cap companies.
-   **$HML$ ("High Minus Low")**: This is the value risk factor. It represents the historical excess return of value stocks (high book-to-market ratio) over growth stocks (low book-to-market ratio).
-   **$\beta_{smb}$**: Measures the asset's sensitivity to the size risk (SMB). A positive value indicates a tilt towards small-cap stocks.
-   **$\beta_{hml}$**: Measures the asset's sensitivity to the value risk (HML). A positive value indicates a tilt towards value stocks.

## Python Implementation Example

The practical application of the Fama-French model requires a multiple linear regression to determine the betas for each factor. However, for a simple calculation where the betas and factor premiums are already known, the function is straightforward.

```python
def calculate_fama_french_3(risk_free_rate, market_return, beta_mkt, beta_smb, beta_hml, smb_premium, hml_premium):
    """
    Calculates the expected return of an asset using the Fama-French Three-Factor Model.

    Args:
        risk_free_rate (float): The risk-free rate of return.
        market_return (float): The expected return of the market.
        beta_mkt (float): The market beta of the asset.
        beta_smb (float): The SMB (size) beta of the asset.
        beta_hml (float): The HML (value) beta of the asset.
        smb_premium (float): The SMB factor risk premium.
        hml_premium (float): The HML factor risk premium.

    Returns:
        float: The expected return of the asset.
    """
    market_risk_premium = market_return - risk_free_rate
    expected_return = risk_free_rate + (beta_mkt * market_risk_premium) + (beta_smb * smb_premium) + (beta_hml * hml_premium)
    return expected_return

# --- Example Usage ---
# Given:
# Risk-Free Rate
rf = 0.02
# Expected Market Return
rm = 0.08

# Factor Premiums (historical averages, for example)
smb = 0.025  # Small-cap stocks are expected to outperform large-caps by 2.5%
hml = 0.04   # Value stocks are expected to outperform growth stocks by 4%

# Betas for a specific small-cap value stock
b_mkt = 1.1  # More volatile than the market
b_smb = 0.9  # Strong sensitivity to the size factor
b_hml = 1.2  # Very strong sensitivity to the value factor

# Calculate expected return
expected_stock_return = calculate_fama_french_3(
    risk_free_rate=rf,
    market_return=rm,
    beta_mkt=b_mkt,
    beta_smb=b_smb,
    beta_hml=b_hml,
    smb_premium=smb,
    hml_premium=hml
)

print(f"Expected Return (Fama-French): {expected_stock_return:.4f}")
# Expected output: Expected Return (Fama-French): 0.1565