# The Capital Asset Pricing Model (CAPM)

This folder contains the CAPM-Model Python script and related Jupyter notebook for quantitative analysis.

- `CAPM-Model.py`: Python implementation of the CAPM model.
- `ipython.ipynb`: Jupyter notebook for interactive analysis and visualization.

The Capital Asset Pricing Model (CAPA) is a fundamental theory in finance used to determine the theoretically appropriate required rate of return for an asset. It provides a linear relationship between the systematic risk of an asset and its expected return.

The model's central idea is that investors should be compensated for their investment in two ways: **the time value of money** and **risk**. The time value of money is represented by the risk-free rate ($R_f$) and compensates investors for placing money in any investment over a period. The risk component compensates investors for taking on additional, non-diversifiable risk.

## The Formula

The relationship is expressed through the following formula:

$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$

## Components of the Formula

-   **$E(R_i)$**: The **expected return** of the investment. This is what you are solving for.
-   **$R_f$**: The **risk-free rate**. This is the theoretical rate of return of an investment with zero risk, typically represented by the yield on a government bond.
-   **$\beta_i$ (Beta)**: The **beta** of the investment. It measures the volatility or systematic risk of the asset in comparison to the market as a whole.
    -   $\beta = 1$: The asset's price moves in line with the market.
    -   $\beta > 1$: The asset is more volatile than the market.
    -   $\beta < 1$: The asset is less volatile than the market.
-   **$E(R_m)$**: The **expected return of the market**. This is the average return of a broad market index, like the S&P 500.
-   **$(E(R_m) - R_f)$**: This is the **market risk premium**, which represents the excess return that investors expect for taking on the risk of investing in the market over and above the risk-free rate.

## Python Implementation Example

Here is a simple Python function to calculate the expected return using the CAPM formula.

```python
def calculate_capm(risk_free_rate, beta, market_return):
    """
    Calculates the expected return of an asset using the CAPM formula.

    Args:
        risk_free_rate (float): The risk-free rate of return.
        beta (float): The beta of the asset.
        market_return (float): The expected return of the market.

    Returns:
        float: The expected return of the asset.
    """
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return expected_return

# --- Example Usage ---
# Given:
# Risk-Free Rate (e.g., 10-year Treasury yield)
rf = 0.02
# Beta of the stock (e.g., a tech stock)
b = 1.3
# Expected Market Return (e.g., historical S&P 500 average)
rm = 0.08

# Calculate expected return for the stock
expected_stock_return = calculate_capm(risk_free_rate=rf, beta=b, market_return=rm)

print(f"Expected Return (CAPM): {expected_stock_return:.4f}")
# Expected output: Expected Return (CAPM): 0.0980