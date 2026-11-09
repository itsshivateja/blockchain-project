from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret-key"

# Course-project prototype: figures below are illustrative, not live market data.
ASSETS = [
    {"symbol": "ETH", "name": "Ethereum", "price": 0, "supply_apy": "—", "borrow_apy": "—"},
    {"symbol": "USDC", "name": "USD Coin", "price": 0, "supply_apy": "—", "borrow_apy": "—"},
    {"symbol": "DAI", "name": "Dai", "price": 0, "supply_apy": "—", "borrow_apy": "—"},
    {"symbol": "WBTC", "name": "Wrapped Bitcoin", "price": 0, "supply_apy": "—", "borrow_apy": "—"},
]

CONTRACTS = [
    ("LendingPool", "Holds deposits and processes borrows."),
    ("CollateralManager", "Enforces loan-to-value limits and health factors."),
    ("InterestRateModel", "Sets interest rates based on pool utilisation."),
    ("LiquidationEngine", "Handles unsafe positions and liquidation incentives."),
    ("PriceOracle", "Reads trusted Chainlink price feeds."),
    ("Governance", "Supports token voting, timelocks, and treasury fees."),
]

ARCHITECTURE = [
    ("Presentation", "Web dApp with MetaMask or WalletConnect wallet connection."),
    ("Data & API", "Indexer and ethers.js for reads, events, and analytics."),
    ("Smart contracts", "Lending pool, collateral, interest model, and liquidation logic."),
    ("Oracles", "Chainlink price feeds for collateral valuation."),
    ("Blockchain", "Ethereum or a low-fee Layer 2 such as Polygon or Arbitrum."),
]

RISKS = [
    ("Smart contract bugs", "Independent audits, formal verification, and public bug bounty."),
    ("Oracle manipulation", "Chainlink feeds, TWAP checks, and circuit breakers."),
    ("Liquidity crunch", "Dynamic rates, reserve factor, and supply/borrow caps."),
    ("Governance attacks", "Timelock, multisig guardians, and voting thresholds."),
]

ROADMAP = [
    ("Months 1–2", "Design", "Requirements, tokenomics, and contract specifications."),
    ("Months 3–4", "MVP on testnet", "Pool, borrow, repay, and liquidation flows."),
    ("Months 5–6", "Audit and beta", "Security audits, bug bounty, and mainnet beta readiness."),
    ("Months 7–9", "Scale", "Governance token, L2 expansion, and analytics."),
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        assets=ASSETS,
        contracts=CONTRACTS,
        architecture=ARCHITECTURE,
        risks=RISKS,
        roadmap=ROADMAP,
    )

@app.route("/demo-action", methods=["POST"])
def demo_action():
    action = request.form.get("action", "Action")
    asset = request.form.get("asset", "asset")
    amount_raw = request.form.get("amount", "")

    try:
        amount = float(amount_raw)
        if amount <= 0:
            raise ValueError
    except (TypeError, ValueError):
        flash("Enter a valid amount greater than zero.", "error")
        return redirect(url_for("home") + "#demo")

    flash(
        f"Demo only: {action} {amount:g} {asset} was simulated. "
        "No wallet was connected and no blockchain transaction was sent.",
        "success",
    )
    return redirect(url_for("home") + "#demo")

if __name__ == "__main__":
    # Render and other hosting services provide PORT as an environment variable.
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
