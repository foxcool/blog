---
title: "Where Money Comes From"
date: 2026-02-10
author: "Alexander Babenko (foxcool)"
tags: [finance, crypto, monetary-policy, central-banking, defi]
series: ["Fiat for Self-Owners"]
summary: "Three theories of the origin of money — Menger, chartalism, credit theory — and why fiat is not a bug but a natural evolution. Part 1 of the 'Fiat for Self-Owners' series."
---

> Series "Fiat for Self-Owners": **1. Where Money Comes From** · [2. How Fiat Works]({{< relref "/posts/how-fiat-works" >}}) · [3. Blockchain, Money, and Governance]({{< relref "/posts/blockchain-money-and-governance" >}})

## Introduction

The fiat system tends to trigger negative associations: "central banks print money", "the inflation tax", "dirty government paper". The blockchain world began with a maximalist idea of opposing itself to traditional banking: "one CPU, one vote", trust minimization, "digital gold". Creating a scarce resource and letting people compete for it led to a predictable outcome. "One CPU, one vote" degenerated into "one megawatt, one vote" — issuance meant to be open to anyone ended up in the hands of industrial miners with ASICs and access to cheap electricity, while the largest holders of the coin turned out to be the same old states (sometimes via confiscation) and big business.

There is a more fundamental problem, too. The 21-million-coin issuance cap is usually presented as the main virtue. The idea of "honest money that cannot be printed" seems fair — until you ask who it actually benefits. But that belongs to a later chapter, on why the world left the gold standard.

> A quick aside from money proper: there is a hypothesis that grain became the dominant agricultural product in Europe because it is easy to count, tax, and then store in granaries once it has been squeezed out of the peasants. Many vegetable crops, root vegetables in particular, are much harder to count and store. This arguably hurt the dietary diversity of ordinary people.

In other words, the very idea of accumulating and warehousing value can itself be a threat — including from the state, which has more capacity than anyone to seize a scarce resource (gold, grain, coin), lock it in a guarded vault, and control everyone else selling services. In that light, the concept of demurrage currency doesn't look so detached from reality, even if it is barely applicable to our economic world (more on money's store-of-value function later). There was even an implementation, by the way: Freicoin.

Fiat is neither a bug nor a scam. It is a distributed system in its own right, with its own properties — the result of several thousand years of humans doing business with each other. Terra burned down trying to reproduce one of fiat's most important properties — elastic issuance via two functions (`mint()` and `burn()`) — without institutions. That is exactly why it matters to develop an understanding of the philosophy, goals, and problems of money, rather than believing in simple solutions.

I am not an economist and will probably get some things wrong, so keep in mind that this is a personal lens and philosophical essay-writing. In this essay I'll describe three competing — but not mutually exclusive — theories of the origin of money, each of which illuminates the others' blind spots. In the next one I'll lay out my current view of the mechanics of the fiat system. After that, my view of a synthesis between fiat's accumulated machinery and crypto as it stands today.

*This series is called "Fiat for Self-Owners". The essays run long, so I'll be publishing the chapters as separate posts.*

---

## Three functions as a diagnostic tool

Economics describes three primary functions of money: a medium of exchange (you can pay for goods), a store of value (the value doesn't evaporate overnight), and a unit of account (you can express the price of anything on a single scale and compare). Good money does all three. Most instruments are a compromise.

What limits cryptocurrencies as money? As a medium of exchange, the traditional constraints were network throughput and high fees. Today these are largely solved problems: L2 solutions, ZK-rollups, and a multitude of networks with different characteristics provide sufficient connectivity and throughput. The technical infrastructure for payments exists.

The fundamental constraint is the weak network effect in the "real" world. By Menger's logic, the asset with the highest saleability becomes money — the one the largest number of counterparties will accept. Crypto still loses to fiat not on technical characteristics but on market depth: the number of merchants accepting crypto is orders of magnitude smaller than the number accepting dollars or rubles. Volatility is largely a consequence: a thin market with a speculative participant base cannot be stable. And without stability there is no unit of account — a restaurant would have to reprint its menu every hour. One caveat: volatility is a normal property of *young* money. Whether stability under a capped supply is structurally impossible is a different question — to my knowledge, there is no consensus answer.

The store-of-value picture is more complicated. Two properties usually get conflated here: censorship resistance and preservation of purchasing power. BTC is strong on the first — no government can freeze your UTXO. But sharp drawdowns make it an unreliable vault in the classical sense. Gold, for that matter, is volatile too — which is exactly why it is conventionally treated not as money but as a defensive asset people flee to in times of elevated uncertainty.

USDT and USDC are closer to "real money" functionally — the de facto unit of account of the crypto market and an acceptable medium of exchange. In times when a bank account with working international transfers is a privilege, stablecoins are routinely used to pay for goods and services directly. But they have a flaw of their own: issuer counterparty risk. USDT is Tether's promise to redeem a token for a dollar, not a dollar itself. Trust, the very thing crypto set out to escape, is back in full force.

The three functions work as a diagnostic tool: any failure of crypto-money is a failure in one of them. Terra tried to be a unit of account (a $1 peg) without a sustainable store-of-value mechanism. BTC is strong on censorship resistance but weak as a medium of exchange and unit of account. Fiat-backed stablecoins like USDT and USDC solve both problems, at the cost of returning to trust — in a specific issuer and its dollar reserves. Decentralized alternatives (DAI, algorithmic stables) try to remove that dependency — with mixed success.

---

## Menger and Szabo: money emerges from below

Money is neither an invention of the state nor a social contract. It is an instance of spontaneous order, in the Austrian School's terms. In his 1892 paper, Carl Menger explains how this order arises naturally from differences in the liquidity of goods.

Menger named the key property *Absatzfähigkeit* — saleability, the capacity of a good to be sold at any given moment without significant loss of value. Traders who notice that some goods sell more easily than others begin accepting them as an intermediary of exchange even when they have no need for them. A positive feedback loop emerges: the more people accept a good as a medium of exchange, the higher its liquidity, the more attractive it becomes to the next participant.

Within this argument, liquidity is measured along three axes: time (the good doesn't spoil), space (it can be transported reasonably conveniently), and quantity (it can be divided). Gold won on all three: it doesn't oxidize, it is compact relative to its value, and it divides without losing its properties. Silver was slightly worse: heavier per unit of value, but more convenient for small transactions. Hence centuries of bimetallism: gold for large deals, silver for everyday ones.

In Menger's model, the state doesn't create money — it merely puts a stamp on what the market has already chosen. Coinage is standardization (a guarantee of weight and fineness), not invention. For a crypto enthusiast, Menger's model is intuitively familiar. BTC looks like a pure Mengerian experiment: bottom-up adoption, no legal tender law, open market competition with other assets.

Nick Szabo, in 2002, debunks the myth of money developing out of barter, arguing instead that money evolved from collectibles that solved the problem of cooperation between hostile groups. Because of the prisoner's dilemma, animals almost never cooperate with non-kin when the exchange is stretched out in time — the risk of cheating is too high. Within small groups, humans solved this through memory and reputation. At the level of inter-tribal contact, the problem was solved with collectibles. These objects needed one key property, *unforgeable costliness*: they could not be counterfeited without costs comparable to "honest" creation.

For example, one tribe hunts bison in summer while another hunts deer in winter, following the migration cycles of the animals. To avoid starving for most of the year, they need to exchange meat. But the tribes are hostile and don't trust each other. So they need some good that is hard to fake or obtain (shells that can only be gathered far from both tribes' territories) to keep the exchange fair across the whole cycle.

For gold, this property is secured by the cost of mining and refining; for BTC, by hardware doing work within the Proof of Work mechanism. It is no accident that bitcoin maximalists are intuitive Mengerians.

A systems-minded reader will immediately recognize the network effect at play in these explanations. Metcalfe's law says the value of a network is proportional to the square of the number of its participants. Trust never disappears entirely — it migrates, as it were, from specific people to instruments and institutions. And at that point it hardly matters whether it's a shell, a special big stone, a gold coin, or an entry in a distributed ledger — what matters is that enough people trust that particular instrument, even when they don't trust whoever they're trading with. I suspect this is one of the reasons the dollar keeps working after 1971. The commodity backing vanished — and the money remained. Which means one model is not enough to explain a phenomenon this complex and varied.

---

## Chartalism: the tax-driven demand floor

In 1905, Georg Friedrich Knapp proposed a radically different and emphatically statist answer: the value of money is determined not by commodity properties but by the state accepting it in payment of taxes and designating it the primary means of payment. An important caveat: Knapp defines "money" strictly as a product of state activity. Anything arising outside the state — cigarettes in prisons, cowrie shells, cryptocurrencies — is for him not money but commodities used for exchange. This is not an empirical finding but a definitional move: he builds his categorical apparatus so that non-state media of exchange are excluded in advance. The state itself is understood as a monolithic sovereign — courts and administration merely execute its will rather than form a distributed system of checks.

With that limitation noted, chartalism's descriptive power remains high. As long as there is an obligation to pay taxes in a given currency, that currency has a guaranteed minimum demand — a *demand floor*. It doesn't matter what money is made of — gold, paper, or bits in a database. What matters is that an institution with a monopoly on coercion demands it back.

This is a descriptive claim, not a normative one. Knapp isn't saying it *ought* to be this way — he is describing a mechanism that works. Like gravity: you may disapprove of it, but it still operates.

Chartalism explains precisely what Menger cannot: why fiat keeps functioning after Bretton Woods, with the commodity base gone. The Russian ruble has non-zero value even under double-digit inflation — because 140 million people are obligated to pay taxes in rubles. That is the demand floor: not a ceiling on value, but a floor below which it cannot fall while the tax system exists.

But chartalism explains the floor, not the ceiling. It doesn't explain why the dollar dominates *globally*, far beyond US tax jurisdiction. The eurodollar market keeps trillions of dollars circulating outside the American banking system. Dozens of dollarized countries use USD without any coercion from the IRS. Oil contracts are denominated in dollars. All of this is USD demand that exists where tax coercion has no reach. To explain the ceiling you need Menger: network effects, market depth, infrastructure, habit. Institutional trust. Chartalism starts the flywheel; Mengerian network effects spin it up.

A common counterargument is that the dollar rests on US military power. That is the same Knapp scaled to empire: a mono-causal explanation that doesn't survive scrutiny. The euro dominates without an army, the yuan stalls despite the world's second-largest army, and sanctions pressure accelerates de-dollarization but doesn't crash the dollar — because liquidity and infrastructure are self-sustaining.

Nor does chartalism explain crypto. BTC works as a store of value without tax demand. So does gold. Prison cigarettes are perfectly functional money without a state. Knapp would say: "that's not *real* money." A market with a trillion-dollar capitalization disagrees.

---

## Credit theory: money is debt

In "Debt: The First 5,000 Years", anthropologist David Graeber attacked Menger's foundational assumption: that before money there was barter. Every economics textbook opens with this story — a hunter traded hides for grain, it was inconvenient, so people invented money as an intermediary. The problem: the anthropological record says the opposite. No known society used barter as its primary system of exchange. What existed instead were credit relationships: IOUs, notches on a tally stick, clay tablets recording debts. Money arose not as a replacement for barter but as a way of accounting for obligations.

I notice the same mechanisms in our time: in villages and summer-house communities there is often a shop where the owner keeps a special notebook of debts. The community is small enough for people to know each other, form networks of trust, and let locals take goods on credit until, say, pension day or payday.

Alfred Mitchell-Innes put it more sharply back in 1913: all money is someone's obligation. A coin is an obligation of the state. A banknote is an obligation of the central bank. A bank deposit is an obligation of a commercial bank. When you look at your bank account and see $10,000, it doesn't mean your ten thousand is lying in a vault somewhere. It means the bank *owes* you ten thousand. The money in your account is an asset to you and a liability to the bank.

The implication for modern fiat is fundamental. When a bank issues a loan, it doesn't take money from other people's deposits or fetch it from a safe. It creates an entry: on the asset side, a loan (you owe the bank); on the liability side, a deposit (the bank owes you). Money comes into existence out of nothing at the moment a loan is issued. This is neither metaphor nor conspiracy theory — it is accounting reality, confirmed by the Bank of England in its 2014 paper "Money creation in the modern economy". Loan repayment is the reverse process: money is destroyed, both entries are zeroed out. The detailed mechanics are the subject of the second essay.

For crypto thinking, this is the key fault line. On a blockchain, money is a *thing*: a token, a UTXO, a balance in a state tree. A thing exists in one place; it can be moved and cannot be copied (the double-spend problem is solved precisely for things). In credit theory, money is a *relationship*: an obligation of one party to another. A relationship doesn't exist "somewhere" — it exists *between* participants. These two ontologies are fundamentally incompatible. Blockchain operates on things. The fiat system operates on relationships. These are not technical limitations that can be optimized away — they are different accounts of what money *is*.

Graeber has a limitation that needs flagging. He conflates historical chronology with logical explanation. Even if barter was historically rare, that doesn't refute Menger's *logic* of how a medium of exchange emerges. That hunters and farmers weren't swapping hides for grain in the market square doesn't mean the mechanism selecting for the most liquid asset isn't real. Confusing "this is how it was" with "this is how it must be" is a common trap that economists and anthropologists fall into alike.

---

## Synthesis: three lenses, one reality

The three theories don't so much compete as describe different layers of one phenomenon. Menger explains the *mechanism*: how money emerges through spontaneous selection of the most liquid asset. Chartalism explains the *resilience*: why fiat works after losing its commodity base — tax demand creates a floor. Credit theory explains the *ontology*: what money actually is in the modern system — obligations, not things.

None of the three describes crypto completely. BTC is pure Menger, but without credit elasticity. ETH is closer to the chartalist model via fee burn, but doesn't create money through credit. Stablecoins borrow fiat's resilience but reintroduce dependence on trust in hierarchical, centralized structures. That points less to a weakness of crypto than to the fact that it is something new. Turing-complete smart contracts make it possible to build mechanisms that combine elements of different theories in ways unavailable to pure fiat or pure "digital gold". But to understand what exactly crypto offers that is new, you first need to understand what it differs from.

### Why the gold standard had to end

The gold standard was abandoned three times in a hundred years: Britain in 1931, the US de facto in 1933 (the ban on private gold ownership), and finally the Nixon shock of 1971. Each time for the same reason: in a growing economy, a fixed quantity of money leads to a deflationary spiral.

If money is fixed and the economy grows, every coin buys more over time. The hodler who does nothing gets richer simply by holding. The one who works and borrows gets poorer — debt in a deflating currency grows heavier every year. This is the well-known mechanics of the gold standard: rentiers got rich, farmers went broke, and the economy kept collapsing into banking panics. Deflationary money is feudalism dressed up as freedom: whoever accumulated first collects rent from whoever came later.

Intellectual honesty requires acknowledging the arguments of both sides. Gold bugs are partly right in their diagnosis: since 1971 US government debt has grown from ~$400 billion to ~$36 trillion, the gold anchor really did constrain issuance, and a system where debt is covered by new debt structurally resembles a pyramid. But the difference is fundamental: a state has a tax base and a monopoly on currency; Sergei Mavrodi, who ran Russia's MMM pyramid in the 1990s, had neither. The analogy is imprecise.

Where gold bugs go wrong is the prescription. Bringing back the gold standard means bringing back the very problem it was abolished for. And by Menger's own logic gold *had* to lose: the dollar turned out to be more divisible, more transportable, and deeper in market terms. Menger would have predicted exactly this — the most liquid instrument wins.

The implication for BTC: maximalism repeats the gold bug argument with a digital asset — "fixed supply = honest money". If the gold standard was abolished three times because a fixed supply is incompatible with elastic demand, why would 21 million BTC hold? Possible honest answers: BTC is not money but a store of value; Lightning Network will create a credit layer on top of a hard base layer; crypto doesn't claim to replace the entire monetary system. All three are more honest than "fiat is a scam".

### MMT: a description, not a prescription

Modern Monetary Theory is the modern development of chartalism. Its key thesis: a state with a sovereign currency technically cannot go bankrupt in that currency — it is always able to create money to service its debt. The constraint is not the budget but inflation.

As a descriptive model, MMT works reasonably well. Banks de facto operate in its logic: they create money through credit, the central bank acts as lender of last resort, and budget deficits are financed by issuing debt the central bank can buy back. This is no textbook abstraction; it describes what happens every day. Bankers and officials, meanwhile, often denounce MMT as ideology while continuing to practice its mechanics.

But as a normative program, MMT doesn't hold up. "The constraint is inflation" sounds elegant until you ask: who defines the threshold? Who decides when issuance is "too much"? MMT presupposes rational and timely state governance — the very assumption practice keeps refuting. Turkey, Argentina, Zimbabwe — all formally fit the MMT description of a sovereign currency. The results are known. MMT describes the mechanism correctly but offers no working safeguard against abuse. For an advocate of self-ownership, this is the key flaw: a system whose only limiter is the operator's good will is a single point of failure.

### ETH: a theoretical hybrid

The most interesting test case for these theories is ETH, not BTC.

In Menger's terms, ETH acquires liquidity through adoption. But its saleability is tied to the usefulness of the network (gas for transactions), not to intrinsic properties of the asset. Gold is valuable because it is gold; ETH is valuable because Ethereum runs on it. The value is derivative, not primary.

In Knapp's terms, EIP-1559 (2021) creates an *analog* of tax demand. The base fee is burned forever. To use Ethereum, you are obligated to pay in ETH. The coercion is not governmental but *architectural*: built into the protocol, not into law. Validators are a kind of "stationary bandit" in Mancur Olson's terms: they extract rent but have a stake in the system's prosperity.

A caveat: with the Pectra upgrade (2025) and account abstraction (EIP-4337), users can pay for gas in USDC or DAI via a *paymaster*. At first glance this kills the chartalist analogy. But the chain goes: user pays USDC → paymaster converts it to ETH → the base fee is burned *in ETH*. The paymaster is a currency exchange booth at the entrance to the tax office, not the abolition of the tax. Account abstraction reduces the *visible* demand for ETH, but not the *structural* one.

Under credit theory, ETH doesn't fit. It is not created through credit and not destroyed when obligations are repaid. Fee burn is supply deflation, not de-issuance in the credit sense.

### The irony of stablecoins

Tether is one of the largest holders of US government debt in the world. The crypto industry, created as an alternative to the fiat system, became one of the biggest buyers of fiat debt. Rather than hypocrisy, this is credit theory confirmed in practice. USDT is Tether's obligation to redeem a token for a dollar, backed by treasuries — obligations of the US government. An obligation on top of an obligation. Layers of debt all the way down. Mitchell-Innes, who wrote about this in 1913, would not have been surprised.

### Hayek: an unfinished experiment

In "Denationalisation of Money" (1976), Friedrich Hayek proposed an idea ahead of its time: let private institutions issue competing currencies, and let the market choose the best one. Hayek assumed issuers would compete on stability of purchasing power — because users are rational and will prefer the currency that preserves value best.

Crypto is an unintended implementation of this experiment. Thousands of tokens compete on an open market without a central arbiter. But the outcome differs from Hayek's forecast: instead of competition on quality, we got competition on liquidity and hype. This doesn't refute Hayek; if anything, it shows he underestimated the role of speculative behavior and network effects in the early stages of a market. Menger would explain: it is not the "best" currency that wins but the most *liquid* one — and liquidity in a young market is determined by attention, not fundamentals.

The experiment is not over, though. Infrastructure is maturing, regulatory frameworks are taking shape, and smart contracts create room for mechanisms Hayek could not have foreseen — programmable issuance rules, transparent reserves, automatic stabilizers. The question is not whether Hayek's experiment failed, but what stage it is at.

---

## In lieu of a conclusion

Fiat is neither an anomaly nor a fraud. It is an evolution from commodity liquidity to credit liquidity: from gold, which is valuable because it is scarce, to obligations, which are valuable because institutions compel their acceptance and habit makes them convenient. Understanding this spectrum is a prerequisite for an honest conversation about what blockchain can do — and what it cannot.

We've covered *where* money comes from — liquidity, taxes, debt. But *how exactly* does the machine that creates 95% of the money supply work? How does a central bank steer a system in which money is created by commercial banks? And why are these mechanics fundamentally incompatible with trustless systems?

That is the subject of the second essay: ["How Fiat Works"]({{< relref "/posts/how-fiat-works" >}}).

---

Sources:
- Menger, "On the Origins of Money" (1892)
- Knapp, "The State Theory of Money" (1905)
- Mitchell-Innes, "What is Money?" (1913)
- Graeber, "Debt: The First 5,000 Years" (2011)
- Hayek, "Denationalisation of Money" (1976)
- Szabo, "Shelling Out" (2002)
- Bank of England, "Money creation in the modern economy" (2014)
- Eichengreen, "Globalizing Capital" (2008)
- EIP-1559
- EIP-4337
