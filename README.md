# Decentralised Lending Platform

A Flask website prototype based on the **Blockchain-Based Decentralised Lending Platform** course-project presentation.

## Features
- Project overview and traditional-lending problem statement
- Five-step flow: Supply, Collateralise, Borrow, Repay, Liquidate
- System architecture layers
- Core smart-contract modules
- Technology stack summary
- Security and risk management table
- Nine-month project roadmap
- Supply/Borrow/Repay/Withdraw demo form (simulated only)

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000

## Deploy from GitHub with Render
1. Create a GitHub repository and upload `app.py`, `requirements.txt`, and the `templates/` directory.
2. In Render, create a **New Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Deploy. Render will provide a public URL.

## Important
This is a course-project frontend prototype. The demo form only simulates actions; it does not connect to MetaMask or submit blockchain transactions. Market/APY values are intentionally marked as unavailable rather than fabricated. Smart contract integrations, live oracle data, wallet handling, and security audits must be implemented separately before real use.
