---
title: "How Fiat Works"
date: 2026-02-19
author: "Alexander Babenko (foxcool)"
tags: [finance, crypto, monetary-policy, central-banking, defi]
series: ["Fiat for the Self-Sovereign"]
summary: "Engineering documentation for the fiat system: credit-based money creation, the M0–M2 hierarchy, central bank tooling, crises and failure modes. Part 2 of the 'Fiat for the Self-Sovereign' series."
---

> Series "Fiat for the Self-Sovereign": [1. Where Money Comes From]({{< relref "/posts/where-money-comes-from" >}}) · **2. How Fiat Works** · [3. Blockchain, Money, and Governance]({{< relref "/posts/blockchain-money-and-governance" >}})

In the first essay we went through three theories of the origin of money and found that fiat is not an anomaly but a natural evolution from commodity liquidity to credit liquidity. Credit theory holds that money is obligations, not things. That is, money is one representation of private relationships, not something material you can simply appropriate and hold.

So how exactly is the machine built that creates most of the money in circulation? What are its levers, its safety valves, its failure points? This essay is engineering documentation for the fiat system. Minimum philosophy, maximum mechanics. The goal: after reading it, a crypto engineer should be able to explain not just *why* fiat works, but *how*.

---

## Who creates money (and who destroys it)

### The myth of the "money printer"

"The central bank prints money" is not just imprecise — it is a harmful simplification. It builds a false mental model in which the central bank is the sole issuer and inflation is a direct consequence of its greed or incompetence. From this model follow mistaken prescriptions: "ban the central bank from printing", "return to the gold standard", "replace it with an algorithm with fixed supply".

In reality, **the bulk of money is created by commercial banks** through the process of lending. The central bank sets the rules of the game and the price of resources, but it doesn't press a "print" button. This is a fundamental distinction: issuance in the fiat system is *distributed*. Every licensed bank is essentially a node in a network with the right to create money. To borrow a blockchain analogy: a loan is `mint()` and repayment is `burn()`, except `mint()` is available not to the protocol but to every bank that has passed the regulator's KYC.

### Balance sheet mechanics: how money is born

Take a concrete situation. Bank A has 100 units on its balance sheet: 10 in required reserves at the central bank and 90 in excess reserves. On the liability side — 100 units of customer deposits.

A borrower comes in asking for a loan of 200. The key moment: **the bank does not pull those 200 out of other people's deposits and does not take them from a vault.** It creates *two entries simultaneously*:

On the asset side, a loan appears (the borrower owes the bank 200). On the liability side, a deposit appears (the bank owes the borrower 200 — sitting in their new account). The balance sheet expanded from 100 to 300 on both sides. Money came into being from an accounting entry. This is neither metaphor nor conspiracy theory — it is documented mechanics, described by the Bank of England in its 2014 paper "Money creation in the modern economy".

Next, the borrower transfers the 200 to another bank. Bank A has to move reserves, but it only has 90 in excess. What happens? Bank A takes a free intraday credit from the central bank for the missing 110, transfers 200 of reserves to Bank B, and closes its debt to the central bank by the end of the day via the interbank market. If it can't — the intraday credit turns into a paid overnight loan at a rate above market.

This is why "the central bank prints money" is a harmful model. In reality the bank created 200 units of money *without prior permission from the central bank*, and then settled its reserve position after the fact. **There is no in-the-moment constraint on reserve volume.** Reserves can be sourced later.

### Symmetry: repayment = destruction

When the borrower repays the loan, both entries are zeroed out. The loan (asset) disappears; the deposit (liability) disappears. The money that was created when the loan was issued is literally destroyed on repayment. The money supply is elastic — it expands with the economy when credit grows and contracts when debts are paid down.

For the central bank, liquidity operations work the same way: a loan to a bank creates reserves (the monetary base grows), repayment writes them off (the base shrinks). Under standard operations (repo, overnight lending) the issuance is temporary and automatically "burned" on repayment.

### What constrains banks

If banks can create money out of thin air — why don't they do it endlessly? Several mechanisms:

**Capital requirements (Basel III)** — the hardest constraint. A bank is obligated to hold its own capital in a set proportion to risk-weighted assets. By issuing a loan, the bank increases its risky assets and must either have a capital buffer or raise capital. That is expensive.

**Risk management.** "Spare" liquidity doesn't automatically flow into credit expansion — banks assess credit risk. Lending to unreliable borrowers leads to defaults and losses. Any banker will tell you the problem isn't issuing a loan; it's getting it back.

**Demand for credit.** Banks can't force loans on anyone. At high rates, demand falls. In a recession, likewise. The willingness of businesses and households to borrow is a key limiter.

**Trust on the interbank market.** If a bank's policies raise doubts, other banks won't lend it reserves. The central bank as lender of last resort will provide liquidity, but with extra costs and questions from supervisors.

---

## The hierarchy of money: M0 → M2

### Not all money is equal

Economists distinguish several "layers" of money. These are not different currencies — they are different levels of trust and liquidity.

**M0 (monetary base)** — bank reserves in accounts at the central bank plus cash in circulation. These are the central bank's obligations — the "hardest" layer. Created only by the central bank: via lending to banks, bond purchases (OMO), currency interventions. In the US at the end of 2025: over $5 trillion.

**M1** — cash in circulation plus demand deposits (checking accounts). This is the level where the credit issuance described above happens. When a bank issues a loan and credits the borrower's checking account, M1 grows and M0 doesn't change. Those 200 units in the Bank A example appeared in M1 as a new deposit, without any prior creation of reserves. For the US: about $19 trillion at the end of 2025 (important: in May 2020 the Fed redefined M1 to include savings accounts — before that M1 was ~$4 trillion; the jump is methodological, not economic).

Cash is the only form of central bank money directly available to the public. When a depositor withdraws cash, their deposit (a commercial bank's obligation) is converted into banknotes (a central bank obligation). M1 doesn't change — one form replaces another. But the bank loses reserves: the central bank debits its correspondent account when the cash is dispensed. Withdrawing cash is literally a climb up the hierarchy of trust, from private money into state money. In normal times the difference is invisible. In a crisis, it's a bank run.

**M2** includes everything in M1 plus savings accounts, small time deposits, and retail money market funds — money you can access quickly but not instantly. For the US: over $22 trillion at the end of 2025.

The gap between layers is telling. M1/M0 ≈ 3.6 — a direct consequence of credit issuance: for every dollar of central bank reserves, commercial banks created another ~2.6 dollars of deposits (using the expanded M1 definition; before 2020 the ratio was lower, but the trend is the same). M2/M0 ≈ 4.2 adds a less liquid layer on top. Before the QE of 2020–2021 these ratios were higher — the mass creation of reserves "inflated" M0, narrowing the gap.

The direction of flows is counterintuitive. The common model — "cash comes into a bank, the bank keeps part in reserves and lends out the rest" — describes movement from the bottom up: M0 → M1 → M2. The real causality is the reverse: credit *creates* the deposit (M1 grows), and reserves (M0) are sourced *afterwards*, to settle interbank payments. Money is born in the middle of the hierarchy and only later requires backing at the bottom layer. This is the inverted causality the Bank of England confirmed in 2014 — the one that makes the multiplier model false, more on which below.

Perry Mehrling, one of the leading scholars of monetary systems, describes the hierarchy of money as a key structural characteristic. In normal times the difference between levels is barely noticeable — your bank deposit feels like "real money". But in a crisis everyone runs up the hierarchy: out of deposits into cash, out of private obligations into state ones. A bank run is a mass climb up the hierarchy of money.

### The money multiplier: textbook vs reality

The classic textbook explains money creation through the multiplier: the central bank gives a bank reserves, the bank keeps 10% and lends the rest, the next bank keeps 10% and lends again, and so on — $100 of reserves begets $1000 of money at a 10% reserve ratio.

**This description is false.** The same 2014 BoE report stated it directly: banks do not "multiply" reserves. They create deposits when issuing loans and *then* look for reserves to settle. The causality is reversed: not reserves → loans → deposits, but loans → deposits → search for reserves.

For crypto thinking, this is a radical shift. On a blockchain you can't spend what you don't have — the balance is checked *before* the transaction. In the banking system, the obligation is created *before* the backing. This is not a bug — it is an architectural decision that provides elasticity. But it also creates the systemic risk: what if the backing can't be found?

### Where M0 comes from

The central bank sets the *price* (the key rate), and the market determines the *quantity*. The channels for creating M0:

**Lending to banks** — the central bank lends to commercial banks against securities as collateral. Reserves are created; on repayment, they are destroyed.

**Open market operations (OMO)** — the central bank buys or sells government bonds. Buying creates reserves; selling withdraws them.

**Currency interventions** — the central bank buys foreign currency with domestic currency, creating reserves. Or sells it, withdrawing them.

---

## The central bank's toolkit

### The key rate: the price of money

The key rate is exactly what it sounds like: the price at which banks can obtain central bank money. Formally, the rate at which the central bank lends to banks on standard terms. But its influence cascades:

key rate → interbank market rate → lending rates → bond yields → cost of capital → investment decisions → aggregate demand → inflation.

The lag between a rate change and its effect on inflation is 3–6 quarters. Every link in the chain can weaken or distort the signal. It is not a switch — it is a thermostat with a lot of inertia.

### The interest rate corridor

The central bank doesn't fix the rate rigidly; it sets a corridor. With a key rate of 15% (a hypothetical example):

Lower bound: 14% — the rate at which the central bank accepts overnight deposits from banks. If a bank has a surplus, it earns at least 14%. Upper bound: 16% — the rate at which the central bank lends overnight. If a bank has a deficit, it pays at most 16%.

The logic: Bank A with surplus liquidity and Bank B with a deficit have an incentive to deal directly — any rate between 14% and 16% benefits both. Competition on the interbank market pushes the rate toward the key rate. The corridor provides soft steering instead of hard control — an important architectural parallel with DeFi protocols, which use bonding curves instead of fixed prices.

Where does the central bank get the money to pay interest on overnight deposits? It creates it — the interest accrual increases the balance on the bank's correspondent account. The central bank is the issuer of reserves and in that sense cannot "run out". But it is an expense: the central bank's income comes from interest on loans to banks and on its bond portfolio, while deposit payouts are a cost. When rates are high and banks park liquidity en masse in deposits, the central bank's expenses grow, its profit falls, and less flows to the budget. The Fed ran into exactly this after QE: rising rates turned payments on reserve balances into an operating loss.

### Repo: collateralized credit in the trillions

A repo (repurchase agreement) is technically a sale of securities with an obligation to buy them back. In essence — a short-term collateralized loan. Bank A "sells" Treasuries to the Fed for $100M and "buys" them back tomorrow slightly dearer. The difference is one day's interest.

The repo market is one of the largest in the world, with volumes in the trillions of dollars daily. For the Fed it is the main instrument of liquidity fine-tuning: repo (buying securities) adds reserves to the system; reverse repo (selling) withdraws them.

The hierarchy of rates in normal times: ON RRP rate ≤ SOFR ≤ Fed Funds ≤ Discount Window. ON RRP is the floor (the Fed takes money from money market funds), the Discount Window is the ceiling (the Fed lends to banks). A violation of this hierarchy is a stress signal.

### QE and QT: unconventional policy

**Quantitative Easing (QE):** the central bank buys long-dated assets (government bonds, mortgage securities) from banks at scale, creating reserves. QE creates M0 but not necessarily M2 — banks receive reserves but are not obligated to transform them into loans. If credit demand is weak, reserves get "parked" in accounts at the Fed. That is exactly what 2020–2021 looked like: M0 nearly doubled, but lending grew more slowly.

This is a key misunderstanding widespread in the crypto community: QE ≠ "printing money into the economy". QE creates reserves — money that exists only between banks and the central bank. For it to become money in the economy (M2), a bank must issue a loan and a borrower must want to take it. With weak demand, reserves pile up in accounts at the Fed without turning into inflation. This is why the QE of 2008–2014 did not produce the hyperinflation its critics predicted.

**Quantitative Tightening (QT):** the Fed stops reinvesting maturing bonds — securities "run off" the balance sheet, and reserves leave with them. The QT of 2022–2025 shrank the Fed's balance sheet from almost $9 trillion to ~$6.6 trillion by early 2026. Why did this go relatively smoothly? Because the ON RRP facility was draining in parallel — money market funds rotated into Treasury bills, releasing liquidity. The system had a "cushion" that absorbed the tightening.

### Inflation targeting

Most large central banks today operate under inflation targeting: they publicly announce a target (usually ~2% for developed economies; the Bank of Russia targets 4%, reflecting higher structural risks and volatility), use the rate as the main instrument, keep a floating exchange rate, and communicate actively with the market.

Why 2% exactly? A historical compromise. Zero inflation is dangerous — under a shock, the economy can easily slide into deflation, and nominal rates can't go far below zero (the zero lower bound). 2% provides a buffer. 4% would be even safer, but it's politically harder to sell "we are targeting a 4% debasement of your money".

An important insight: **trust in the central bank matters more than the specific instrument.** The IMF study "Navigating the 2022 Inflation Surge" showed that during the supply shock, strict adherence to inflation-targeting rules yielded no statistically significant advantage. Flexible responses (including currency interventions) sometimes worked better. The method is secondary — provided trust in the monetary authorities is already established.

For a crypto enthusiast this is illogical. Trustless systems prize precisely the *absence* of trust in an operator. But the fiat system works on the opposite principle: it is optimized for trust, and centralized trust at that — concentrated in the state and the institutions it regulates. This is not an argument for one approach over the other — it is a statement of an architectural choice, and that choice has consequences.

---

## When the system breaks

### Minsky: stability breeds instability

Hyman Minsky described a cycle the fiat system reproduces again and again. In good times, borrowers and lenders grow ever bolder:

**Hedge phase:** the borrower services both principal and interest out of cash flow. The credit is healthy.

**Speculative phase:** cash flow covers only the interest. Repaying principal requires refinancing. The borrower depends on the availability of credit.

**Ponzi phase:** cash flow doesn't even cover the interest. The borrower depends on the asset's price rising in order to refinance or sell. Any price decline means collapse.

The system drifts from hedge to Ponzi not out of malice but out of adaptive behavior: when things are good, caution looks like foregone profit. Banks that don't expand lending in a boom lose market share. Managers who don't take risk don't get bonuses. The market selects out the cautious and rewards the aggressive — as long as the music keeps playing.

### Bank run: the built-in vulnerability

The banking model is based on maturity mismatch: a bank takes short deposits (withdrawable tomorrow) and issues long loans (a 30-year mortgage). In normal times this works because not all depositors show up at once. But if panic starts, the bank cannot return all the deposits, because the money is frozen in long-term loans. This is not a defect of a particular bank — it is a property of the model.

Walter Bagehot formulated the rule for such situations back in 1873: in a crisis, the central bank should lend freely, against good collateral, at a penalty rate. Lender of last resort is not charity — it is a systemic function. Without it, any bank run becomes a self-fulfilling prophecy.

### Why "let them fail" doesn't work

A common libertarian argument: let the bad banks go bankrupt, the market will cleanse itself. The problem is that a bank run is indiscriminate. Banks that managed risk thoughtfully, created value, and practiced a risk-based approach go down together with those that deserved it. Panic doesn't read balance sheets. The collapse of a banking system is a loss of what economists call "knowledge capital": the accumulated expertise in risk assessment, liquidity transformation, credit relationships. Recovery takes years and hits people who did nothing wrong.

2008 provided a practical demonstration. Bear Stearns was saved — the contamination of its assets was relatively manageable, and the chain reaction was contained. Lehman Brothers was allowed to fall — and that set off a cascade: pass-through effects across counterparties, risk-off on global markets, capital flight from emerging economies. Institutions and economies that had nothing to do with the mortgage bubble were hurt. Inaction proved costlier than a bailout.

A concrete example of second-order effects: a small business owner, solid and debt-free, builds savings in a pension fund. The fund invested in MBS and CDOs (mortgage-backed securities — pools of mortgage loans packaged into tradable paper; CDOs — collateralized debt obligations — a secondary packaging of the same pools into risk tranches). Lehman burst — the savings burned. In the general panic people started saving more and spending less — his business's revenue fell, debts piled up, the business died. The man did everything right — he's not a financier, he's a shopkeeper. But a systemic crisis doesn't sort the guilty from the innocent. There are millions of such stories.

An important distinction: the argument for bailouts applies to the banking system as infrastructure, not to any large company. When the CEO of a tech company declares that half of GDP growth depends on his company and everyone therefore needs to "pull together" — that is rent-seeking, not systemic risk. The banking system is different: it is the infrastructure of trust on which the credit-based monetary system rests. If it collapses, everyone suffers, because what collapses is the very mechanism of credit issuance described in the first chapter. This is not an argument for saving particular managers — it is an argument for preserving the infrastructure, with accountability for the guilty at the same time. Tellingly, Hayek himself in his later period revised the early Austrian prescription of "let the world crash" — he acknowledged the second-order effects of crises and the need for proactive instruments. Rothbard stayed on the extreme position; Friedman openly criticized that orthodoxy as harmful.

### The 2019 repo crisis: a "distributed" system breaks

In September 2019, rates on the repo market spiked to 10% against a 2% target. Why? Three factors coincided: corporate tax payments (a reserve drain), a large Treasury issuance (demand for cash), and — crucially — reserves were concentrated at a few large banks, while regulatory requirements (LCR) prevented them from lending.

A system that is supposed to be "distributed" turned out to have points of concentration. "Ample reserves" ≠ "well-distributed reserves". The Fed was forced to launch emergency daily repo operations to stabilize the market. Later, in 2021, this experience was formalized into the Standing Repo Facility (SRF) — a permanent mechanism allowing banks to borrow from the Fed against Treasury collateral. The SRF essentially institutionalized the lesson of 2019: the system needs a backstop that is available before the panic starts, not after.

For a crypto engineer this is a familiar pattern: liquidity can be formally sufficient in aggregate yet fragmented across pools. DeFi solves this with composability — protocols can use each other's liquidity. Fiat solves it through the lender of last resort — the central bank as a single point of access to liquidity. Both approaches have their costs.

### Bank rescues: socializing the losses

When a bank does become insolvent, the central bank carries out a rescue — injecting money into the bank's capital. This is not a loan (which would be repaid) but a recapitalization. Issuance for a rescue is not automatically burned and stays in the system.

Formally, rescues are not financed by taxpayers. Economically, they are financed by everyone: through the inflation tax (issuance dilutes purchasing power), through the budget's opportunity costs (75% of the Bank of Russia's profit is remitted to the budget — less profit means higher taxes or lower spending), through the systemic risk premium (priced into the rates on all loans).

**The MKB case (2024, Russia):** a 2.5 trillion ₽ portfolio, 668 billion of bad loans identified (27% of the portfolio). Provisions before the inspection — 5 billion. After — ~200 billion. Risk underestimated by a factor of 40. The pattern is typical: aggressive growth → deferred recognition → change of management → audit → shock.

**The SVB case (2023, US):** classic maturity mismatch. The bank loaded up on long bonds during the low-rate period. When the Fed raised rates, the market value of the portfolio fell. The depositors (mostly startups) ran — a 21st-century bank run looks like mass online transfers within a few hours. The FDIC stepped in, guaranteeing all deposits including uninsured ones.

The moral hazard is plain: profits are privatized (management bonuses), losses are socialized (onto everyone). This creates incentives for excessive risk. The crypto answer to moral hazard is not only "code is law" but also transparency of positions, individual responsibility, and decentralized governance. The fiat answer is regulation and supervision. Both are imperfect.

---

## What fiat cannot do

The first four sections described how fiat works. This one is about what it *cannot* do — and this is where the space for blockchain begins.

### Censorship resistance

The state can freeze an account, reverse a transaction, confiscate funds. For law enforcement, this is a tool. For a person living in a jurisdiction with arbitrary enforcement, it is an existential risk. The fiat system is *by design* not censorship-resistant. That is not a bug but a feature for some — and a threat model for others.

### Transparency

Bank balance sheets are a black box for depositors. The MKB case shows that even the regulator may not know the real state of affairs. Audits are after-the-fact, not realtime. The difference between a declared 5 billion in provisions and a real need for 200 billion can go undetected for years.

In DeFi, every liquidity pool, every collateral position, every exposure is visible on-chain in real time. This doesn't automatically make DeFi safer (smart contracts have their own vulnerabilities), but it changes the trust model: verify, don't trust.

### Settlement

Bank settlement: T+1 or T+2 (one to two business days), batch processing, weekends and holidays are downtime. An international transfer through SWIFT and correspondent accounts takes days and percentage fees (with a floor of around $30 per transfer, at that). Every intermediary bank adds latency and cost.

Blockchain settlement: seconds to minutes, 24/7/365, atomic (it either happens completely or not at all). This is an objective technical advantage — fiat infrastructure cannot compete with it in its current architecture.

### Programmability

Conditional payments, composability (one financial instrument using another as a lego brick), automatic execution of terms — impossible in traditional banking infrastructure. Every integration is a separate project with APIs, approvals, compliance. In DeFi, a smart contract can call another smart contract, which calls a third — all within a single transaction.

### Cross-border movement

The dollar dominates globally, but *moving* dollars across borders remains complicated, expensive, and supervised. The correspondent account system, compliance requirements, AML checks — all of it adds cost and time. For a person earning a salary in one country and paying rent in another, a stablecoin on a fast L2 network is already the superior transfer technology.

---

## In lieu of a conclusion

The second essay of the series predictably came out dense: a pile of abstractions and non-obvious design decisions, all clearly anchored in centralized trust. But I believe understanding these mechanisms at least in outline is necessary if new ideas and products on blockchain are to have a real connection to the needs of the existing economy.

The fiat system can be pictured as a set of intricately connected vessels. In some places liquidity is added or "mined"; in others it "evaporates". This partly explains why monetarists look at classic bitcoin as something of a child's toy that could never, by itself, perform the functions of full-fledged modern money. But why is trust centralized? Why does everything converge on the state? Why are networks of trust built out of supervised commercial banks? Can modern technology build systems with more decentralized and democratic trust mechanisms, in which the individual gets a completely different level of agency — one previously available only to banks?

That is the subject of the third essay.

---

## Sources

- Bank of England, "Money creation in the modern economy" (2014)
- Mehrling, "The New Lombard Street: How the Fed Became the Dealer of Last Resort" (2010)
- Minsky, "Stabilizing an Unstable Economy" (1986)
- Bagehot, "Lombard Street: A Description of the Money Market" (1873)
- Joseph Wang, "Central Banking 101" (2021)
- IMF Working Paper, "Navigating the 2022 Inflation Surge"
- FRED: M1SL, M2SL, BOGMBASE, MBCURRCIR, WALCL
- Federal Reserve, H.6 Money Stock Measures (Dec 2025)
- Federal Reserve, Monetary Policy Report (Feb 2025)
- MKB (Credit Bank of Moscow) figures: estimates by @helicoptermacro
- SVB figures: FDIC failure summary, Matt Levine / Bloomberg
- G. Bazhenov, discussion of Austrian business cycle theory and the lender of last resort (in Russian): https://t.me/furydrops/4136
- M. Friedman, R. Epstein, interviews on the Austrian School (Hoover Institution)
