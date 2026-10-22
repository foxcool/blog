---
title: "On the Uses and Prospects of Blockchain for Money and Governance"
date: 2026-03-06
author: "Alexander Babenko (foxcool)"
tags: [finance, crypto, monetary-policy, central-banking, defi, governance]
series: ["Fiat for Self-Owners"]
summary: "Why blockchain cannot reproduce credit-based money creation directly, what stablecoins and DeFi actually bridge, and why CBDC is a regression. Part 3 of the 'Fiat for Self-Owners' series."
---

> Series "Fiat for Self-Owners": [1. Where Money Comes From]({{< relref "/posts/where-money-comes-from" >}}) · [2. How Fiat Works]({{< relref "/posts/how-fiat-works" >}}) · **3. Blockchain, Money, and Governance**

## Introduction

When the blockchain world was just beginning, the dominant opinion even in technical circles was skepticism. Most people spoke in simplified chartalist narratives: "Money is whatever the state forces you to treat as money." The intellectuals operated with more interesting material — references to the deflationary spiral problem, network effects, and other things that are, I hope, familiar by now.

A decade and a half later, people in perfectly mainstream professions sometimes get paid for their services on a blockchain, and offline exchange desks flourish wherever business and people from different countries concentrate. Some places are even abandoning the idea of a CBDC and drafting plans to integrate "real world assets" (RWA) and banking with blockchain projects independent of states. All this against the backdrop of a radical decay in the morals and performance of traditional institutions in recent years: account freezes, attempts to restrict financial and informational connectivity, attacks on privacy and other elements of a full individual life. For many, cryptocurrencies have become just about the only reliable means of saving and exchange.

The world is changing so fast that some of the problems and limitations described in the sections of this essay may soon lose relevance. In part, that is the joy of belonging to the philosophical-technological frontier of the global community — the chance to touch not only the consequences of politicians' reactionary activities, but also something beautiful, something that lifts us to a new level.

But as I write this, the SEC and CFTC are signing an agreement on joint crypto regulation, and the Treasury is proposing to extend the Patriot Act to DeFi. The convergence is moving faster than it seemed...

---
## The problem of implementing credit issuance on a blockchain

In the second essay we saw that credit issuance is a distributed `mint()` available to every licensed bank. But that `mint()` works only because the bank *knows* the borrower. Not in the KYC-checkbox sense — in the sense of three things without which credit is impossible:

**Identity** — who is taking the money. Not an abstract address but a specific person or company with a history, assets, reputation. The bank assesses creditworthiness not because it enjoys bureaucracy, but because it creates money out of nothing and risks its own capital.

**Intent** — what the money is for. A loan to build a factory and a loan for casino bets carry different risks. Intended use affects the probability of repayment, and therefore the price of the loan and whether it can be issued at all.

**Recourse** — what happens if the borrower doesn't pay. Collateral, litigation, bankruptcy, restructuring. The whole apparatus of enforcement that makes an obligation *binding* rather than voluntary.

Trustless systems, by definition, operate with none of the three. Code executes what is signed, without asking "who are you", "what do you need it for", and "what happens if you don't pay it back". This is elegant for transferring existing assets. But it is incompatible with *creating* new money through credit.

An important caveat: the banking world itself has drifted some distance from the ideas of the past. It used to be that a bank was a mostly local institution that could know enough about the residents of its town and surroundings to form judgments about a potential borrower's solvency and adequacy. Our generation deals not with the movie-style local banker but with branches of centralized banking networks. The decision to grant a loan or issue a credit card is made not even at the branch but by a scoring system, most likely located in the capital. And it is made not on the basis of any special trust in a specific person, but on the contents of various registries: credit history, employment records, and so on. Often the judgment about someone's creditworthiness is produced by statistical models — age, gender, education level and the like — not by their personal qualities.

Banks' willingness to lend also correlates with market conditions. If another crisis is underway, appetite for risk falls not only among traders but among bankers. Conversely, in an overheated economy loans may be handed out without any serious risk management to not-very-solvent citizens. These are the well-known causes of pseudo-cyclicality, self-reproduction, and amplification of crises.

The problem of "digitizing trust" and partially removing the human factor clearly extends beyond blockchain. This, apparently, is why the world is so drawn to social ratings of every kind and to universal transparency: if you can gather enough information about a specific person's decisions, promises, and actions, then hypothetically you can predict their behavior in matters of finance and risk with higher quality. Ratings and transparency seem all but predetermined. The question is how it will be organized, and whether the whole thing will have a "centralized" and omnipotent operator capable of inflicting civic death and debanking on any person who crossed "the wrong people".

---
## Protocol issuance

Fortunately, credit is not the only way to create new money. Blockchain protocols conduct issuance differently: through rules written in code. Usually as a reward for those who keep the system running (miners, stakers, and so on).

Bitcoin mining evokes gold digging for many: work requiring access to energy and specialized equipment lets you claim not only the fees for transfers within the network but also a share of new coins while issuance lasts. Back before the previous hype cycles, I criticized this method of issuance for lacking the now-famous factor — skin in the game: a PoW miner does not fundamentally depend on the resilience of the whole network, has no resources locked in it (no stake), and therefore, as I see it, such miners should not be given the status of decision-makers at the level of the entire ecosystem. That said, the mechanism lives on quite well in its current form, and its conservatism performs useful functions. Even though this issuance is not elastic and does not depend on demand, market conditions, or any other context, it does allow value to be "sealed in" — value that can serve as an analog of commodity money and, probably, as one of the reserves for decentralized finance.

As I've mentioned before, modern Ethereum looks significantly more interesting to me. The premium to stakers minus the burning of part of the transaction fees lets net issuance turn positive or negative moment to moment depending on network activity. De facto this is a simplified but *functioning* automation of monetary policy: the total quantity of coins in the system is adjusted by the use of the network. Not credit-elastic, but not constant either.

But let's not forget what makes the cryptocurrency world beautiful: it is not limited to the known, already-established large players. Hundreds of projects create their own tokens: some use existing blockchains, some create their own. Some ecosystems, like Polkadot, build a framework for creating your own chains that interoperate with others by following shared protocols. Each such project can have its own set of characteristics: issuance rules, utility, economics. It is something between money and exchange-traded assets: protocols get "mined", pull dollar liquidity toward themselves, compete for users and capital. Some lose, and value flows to competitors or back into fiat. Others survive and grow organic demand through real use (settlement, computation, storage). This is closer to Hayek's "competition of private currencies" than stablecoins are, with one substantial caveat: most of these "currencies" behave like capital in infrastructure projects, not like media of exchange. On the other hand, many crypto assets are no longer so easy to accuse of purely speculative purpose without exposing the limits of the accusation.

Protocol issuance doesn't replace credit elasticity, but it creates a base money layer analogous to gold in the gold standard era. Protocol tokens are something like reserves with value of their own — via the Mengerian or chartalist principles described in part one — while DeFi layers on top can create fundamentally new financial solutions. Including ones connected to the fiat world and to "real world" assets.

---
## Bridges between the systems

### Fiat stablecoins

USDT and USDC are the dominant instruments of the crypto market. They don't create new money — they *bridge* fiat liquidity onto crypto rails. By Mengerian logic this is only natural: the most liquid instrument wins, and the dollar is the most liquid asset on the planet. Stablecoins inherit its liquidity while adding blockchain properties: 24/7 operation, programmability, cross-border movement without SWIFT.

The irony deserves attention. Tether is one of the largest holders of US Treasuries in the world. An industry created as an alternative to fiat became one of the largest buyers of fiat debt. This is not hypocrisy — it is credit theory confirmed in practice. USDT is an obligation of Tether, backed by obligations of the US government. Layers of debt all the way down. Mitchell-Innes would not have been surprised.

### DAI and the drift toward RWA

MakerDAO began as a purely crypto-collateralized stablecoin — the embodiment of the trustless ideal. By 2026, a significant share of DAI's collateral is Real World Assets: US Treasuries, corporate paper. DAI became a wrapper around fiat collateral with on-chain governance. Capitulation and pragmatism at once: pure crypto collateral is too volatile, and the hybrid model works — on-chain transparency and governance combined with the resilience of fiat collateral. It is the same collateral-base story: diversifying collateral reduces correlation but reintroduces dependence on the off-chain world.

The explanation suggests itself. The US dollar is an obligation of the Federal Reserve System. Pegging a token's price to it presupposes a link to that system and to government debt. Without that link, pegging to a currency's price means constant risk of mass liquidations due to crypto asset volatility, or excessive collateral lockups as overinsurance. The solution would be either the volatility decline expected over the years in the most popular cryptocurrencies, or the emergence of stable tokens not pegged to the dollar. But that same solution would automatically reduce the need for dollar stablecoins — a closed loop that converges on the world economy's shared dependence on US government debt as the most stable asset.

### Implementing trust mechanisms on-chain

Elastic issuance requires Identity, Intent, Recourse. Trustless systems renounce them. But this is a false dichotomy — if you treat trustless as a binary switch. Vitalik has shown that trustless is a spectrum. The same logic applies to credit.

On-chain reputation, the social graph, trust networks — these are a decentralized implementation of all three pillars:

**Identity** — verifiable reputation: transaction history, fulfilled obligations, counterparty attestations. Soulbound tokens (non-transferable NFTs), decentralized identity protocols (DID), on-chain credentials — infrastructure for identity without a central registry.

**Intent** — an on-chain track record. Patterns of credit behavior: how previous loans were used, what the repayment rate was, which protocols the borrower participated in. No bank clerk evaluates a business plan — an algorithm analyzes history.

**Recourse** — social. Loss of reputation = loss of access to future credit, airdrops, and so on. In a p2p trust network, a default destroys not only the current relationship but future opportunities. Banks and courts remain as an *optional* enforcement layer — for large sums, complex disputes, physical assets. But the base enforcement is social and algorithmic.

In this model, a bank is one node with a high trust score. It lends against smaller collateral thanks to information and better-coordinated work with the instruments of state coercion. The state is the arbiter of last resort in a specific physical jurisdiction, but not the operator of a universal and only database. Everyone keeps their roles but loses their monopoly. This is not a replacement of the credit system but its *democratization*: self-banking, where every agent can be a lender and a borrower without a banking license, though with differing capabilities.

Some cryptocurrencies will remain "commodity", non-credit — digital things, an analog of gold. BTC as a reserve, a store of value — and that is fine; not every asset has to be a credit asset. But DeFi *must* develop credit layers coupled to individual sovereignty: p2p trust networks instead of centralized rating agencies, decentralized credit scores based on on-chain history.

In practice — still pre-alpha. Unsolved problems: Sybil resistance, privacy in credit scoring, enforcement without a legal system. But the counterargument "this will stay niche forever" is refuted by precedent: passkeys. Mass adoption of trustless infrastructure is possible when it is *more convenient* than legacy.

The democratization of banking also requires the democratization of protection. Self-banking gives the individual capabilities previously available only to banks, but simultaneously strips away institutional safety valves. Integrity of intent — the authenticity of intention — becomes the fourth element of security alongside identification, authentication, and authorization. How do you protect a person from actions they perform themselves, but under pressure or manipulation? This problem — the paradox of control: total control = total vulnerability — deserves a conversation of its own, the subject of a separate essay on the problem of coerced will.

The architectural metaphor is two-layered, as in the gold standard era:

Base money layer: protocol issuance (§1) — BTC, ETH, protocol tokens. New money created through code, not credit. The analog of gold.
Credit layer: p2p trust networks (this section) — on-chain reputation, DID, the social graph. Elastic issuance on top of base money. The analog of bank credit.

Fiat: trust centralized → state monopoly → CBDC as the logical limit of centralization.
Crypto: trust distributed → individual sovereignty → protocol base money + p2p credit as the logical limit of decentralization.

### Pull and push payment architectures

Fiat payment infrastructure is largely built on a pull model. When you give a bank, a merchant, or a subscription service your card details, you grant them the right to *withdraw* money from you. Direct debits and recurring payments are the example: someone else initiates the movement of *your* money. Historically this was a convenient solution. In practice, the pull model became an architectural hole and a vector for mass fraud: compromised details allow funds to be withdrawn without the owner's knowledge, and disputing transactions turns into bureaucratic hell.

Blockchain is push-only by design. No one can withdraw funds from someone else's wallet without an authorization pre-signed by the owner. Every payment is an act of the sender's will. This is a fundamentally different architecture: not "I allow you to take" but "I send to you". Over time, analogs have appeared and gained popularity in fiat as well: QR transfers, instant payment systems like Russia's SBP, and so on.

The lack of native recurring payments on blockchain is a frequent criticism. But the subscription model in fiat breeds its own abuses. Dark UX patterns have become an industry standard: subscribing takes one click, unsubscribing takes ten screens, a call to support, and a waiting period. Entire businesses live off users who forgot to unsubscribe. The pull model creates ideal conditions for this: money is withdrawn by default, and inaction works in favor of the service owners.

The push model returns control to the sender: making a payment requires attention and motivation, not the other way around. And where there is a healthy need for regular payments — donations to open projects, periodic transfers to services you actually use — the infrastructure is already emerging. For example, [Kalatori](https://github.com/Kalapaja/Kalatori) is an open-source daemon for processing blockchain payments in the Polkadot/EVM ecosystems that solves payment acceptance without the pull model, including regular donations, convenient payment for goods and services online, and so on. This is not a replacement for subscriptions — it is an alternative architecture in which recurrence is a deliberate act of the payer, not a passive permission to withdraw.

### Convergence and its price

The GENIUS Act of 2025 at first glance protected self-custody, but obligated stablecoins to implement freeze functions. Sovereignty with reservations. It even seems fair in a way: stablecoins, being a representation of the US dollar, which is an obligation of the Fed and a bridge to government debt, may reasonably carry some regulatory elements of their own.

But the reservations multiply. In March 2026 the Treasury published a report (an obligation under the GENIUS Act) in which it acknowledged the legitimacy of mixers for privacy — in one paragraph. In the remaining pages: a proposed "hold law" (freezing without a court), a sixth special measure under the Patriot Act to block DeFi transfers, "incentivizing digital identity tools". The right exists, but the conditions of its exercise (enforcement) make it decorative.

In parallel, the SEC and CFTC launched Project Crypto and later signed a Memorandum of Understanding — a unified asset taxonomy, joint inspections, coordinated enforcement. A familiar plot develops, as in the old parables: failed attempts at prohibition give way to attempts at co-optation and placement inside a supervisory perimeter on the supervisor's terms.

One hand grants self-custody; the other builds an identity layer on top. Not a choke point through banks (Operation Choke Point, 2013), not through lawsuits (Gensler, 2022), but through verification infrastructure. More elegant and more frightening.

The Hayekian experiment from the first essay is not over — but the competition turned out to be not monetary but identity-architectural:

- The state panopticon: CBDC + social credit. China as the example.
- The corporate panopticon: passkeys from Apple/Google + eIDAS 2.0. Europe.
- The sovereign model: self-custody + Decentralized IDentifiers and the like. The GENIUS Act as the legal basis — while executive agencies like the Treasury build the identity layer through another door.

Whoever controls identity controls access to money. As usual, political processes never stop — at every stage of society's development, statists and regulators of every stripe will try to restrict your ability to dispose of yourself and your property "in special cases and in the name of good". But that is what political and social life consists of: every attempt to close off one possibility or regulate some sphere is followed by the emergence of new options for geo-arbitrage, workarounds, cypherpunk solutions. Competition is a process, not a state (Hayek). Equilibrium is the death of the market. If bureaucrats gain total control over something, liquidity and entrepreneurial activity will simply seek an exit elsewhere. This becomes especially clear when you recall the ideas of the first part: money is not gold in a vault and not a coin on a chain. Money is one person's willingness to hand over goods or render services to another. An obligation. Total control over people's identity, transactions, obligations and their fulfillment is, in essence, a variant of slavery.

### Debanking as the real reason to fight for privacy

Censorship-resistant settlement sounds academic or even marginal — until you become its target audience. In Canada in 2022, for instance, they decided to freeze truckers' accounts over participation in a protest. The accounts were later unfrozen and the courts found the actions unlawful, but the aftertaste remained. Russians after 2022 have had Swiss and EU banks mass-close their accounts *by passport*, not by sanctions list.

In some countries you are not granted the right to open an account even with a residence permit, let alone long-term visas or tourist status. Meanwhile, a great deal hangs on having an international card: one typical problem is paying for insurance and receiving payouts on it when Russian bank accounts are not considered at all, and obtaining — or even keeping — a functional bank account is a separate challenge. The same, incidentally, applies to getting and keeping SIM cards, to which you are forced to tie various accounts in systems like delivery services and so on.

**The ratchet effect**: instruments created for discriminated groups expand to everyone else. For a growing group of people — not ideologues or activists, but ordinary citizens caught inside an expanding perimeter of control and chaotic repression — blockchain stops being an investment and becomes survival infrastructure.

### Frontends as the new choke point

After the Tornado Cash sanctions, most blocks were built by builders complying with OFAC requirements. DeFi protocol frontends blocked users by geolocation. Safe{Wallet} is unavailable from a number of jurisdictions even though the contract itself is permissionless.

Ethereum's answer is FOCIL (EIP-7805), planned for the Hegota upgrade: a mechanism forcing validators to include all valid transactions, making protocol-level censorship technically difficult. But frontends remain the vulnerable point.

Hence the logic: if centralized frontends become choke points, a local interface to the contracts is the sovereign fallback. Not a replacement for convenient apps, but a reliable way of "voting with your feet" that shapes developer incentives. As Gavin Wood put it: "If you can't run a full-node yourself then it's just another bank." Likely, the development of LLMs will gradually replace the old web interfaces on which dark UX patterns are actively deployed, including by large corporations.

### CBDC and "Gold Standard 2.0" as regression

The central banks of some countries are developing digital currencies. At first glance it looks like convergence: the state borrows programmability, uptime, and execution speed from blockchain. In reality it is a regression — the antithesis of self-banking and even of fiat itself.

A CBDC is a centralized mutable database with a direct wire from the state to every citizen's wallet: total transparency for the state with zero transparency in the opposite direction, programmable restrictions on spending, and the potential liquidation of the banking layer along with credit elasticity. The bureaucratic friction of traditional banking is not a bug but a protective mechanism: every intermediate step had someone responsible for it and created a point where abuse could be noticed and contested. CBDC removes that friction, leaving the citizen the role of terminal operator rather than a subject with rights. The irony of automation applies: the more convenient the CBDC, the faster the skill of financial self-reliance atrophies — and the more helpless the citizen at the moment the system turns *against* them. A detailed analysis of CBDC as the antithesis of sovereignty belongs to a separate essay.

Digital currencies are not the only attempt by states to enter blockchain territory. In parallel, there are attempts to create an interstate settlement layer. A sort of "Gold Standard 2.0" in crypto wrapping.

The reality is more modest than the marketing. There are, for example, two separate projects that some channels blend into one. The Unit is a pilot by the IRIAS research institute: 100 tokens on Cardano, 40% gold, 60% a basket of BRICS currencies, launched in October 2025. Not a currency but a settlement instrument. mBridge is a separate project: a wholesale CBDC bridge using a modified consensus called "Dashing", based on HotStuff. Both projects illustrate one pattern: technology created to eliminate intermediaries is used to create a new closed club of intermediaries. A "decentralized gold storage system" under Chinese control is an oxymoron: whoever audits the vaults controls the system.

Gold is not chosen by accident here. Physicality, as I said earlier, is a means of control through custody. For authoritarian regimes gold is convenient precisely because it is confiscatable. Hence the expected bundle: CBDC for citizens, a closed gold-for-goods circuit for the "sovereigns", control of the exchange points into cryptocurrencies.

The economics potentially doesn't add up either. 100% gold backing of government debt is impossible: the combined debt of the BRICS countries is comparable to the gold reserves of the entire world. A peg constrains the money supply: the economy must grow, while less and less gold will be mined.

The practical outcome is predictable: the system launches with loud declarations of "100% backing", then quietly introduces leverage, then the backing slides to 20%, then to 5%. The history of the original Bretton Woods, only with blockchain in the slide deck. Hayek criticized exactly this pattern: a state monopoly on money inevitably degrades into inflationary abuse, no matter what anchor you start with. This is not a new financial system — it is a rebranding of the old one. The solution is the denationalization of money, not a rearranging of the beds.

---
## Governance: blockchain as a constitutional protocol

The title of this essay promises "money *and governance*". The most important bridge between fiat and crypto is not stablecoins and not RWA, but blockchain as a layer of transparency and consistency for the monetary — and even the political — system itself. Fiat gains the accountability it lacks; crypto institutions gain legitimacy.

### Who should be transparent to whom

CBDC makes citizens transparent to the state. On-chain governance makes the state transparent to citizens. The asymmetry of observation is not a technical detail but a political choice. CBDC implements *Bentham's Panopticon*: the warden sees the prisoners, the prisoners don't see the warden. On-chain governance moves toward the reverse: power is transparent, citizens are private.

### The black box of monetary policy

In the second essay we described the fiat machine as a *mechanism*. But not as a source of abuse. And the abuses are systemic, because discretionary decisions in monetary policy are hidden by default.

**The central bank's discount window**: which bank receives emergency liquidity, on what terms, against what collateral — these are decisions that determine who survives a crisis and who doesn't. They are published with delays, once the political consequences for the officials involved are no longer possible.
**QE allocations**: in 2020 the Fed began buying corporate bonds — which companies exactly, how the funds were selected, who lobbied for inclusion — opaque.
**Currency interventions**: the Bank of Japan regularly intervenes in the currency market without officially confirming the fact of intervention until the data appears in a quarterly report.
**Rescue decisions**: Bear Stearns was saved, Lehman was not; the criteria of that choice are not fixed in any protocol.

The ratchet effect works in monetary policy just as it does in surveillance: every crisis expands the perimeter of the central bank's discretionary powers, and no expansion is ever rolled back.

And the problem is not only corruption or political pressure. Monetary science exists — but its application depends on specific people in specific institutions. Turkey: Erdoğan pressured the central bank for years, replaced three governors in two years, the lira lost 80%+ — political subordination. Japan: decades of deflation under an independent central bank — institutional inertia. Argentina, Venezuela, Zimbabwe — from incompetence to deliberate destruction. Different failure stories, but one root: a concentration of discretionary decisions without effective feedback.

The answer is not to abandon monetary science, but to have an execution mechanism independent of those it constrains.

### What this looks like in one example

Take the discount window — emergency central bank lending to banks.

**Now:** the central bank decides who gets liquidity, against what collateral, on what terms. The decision is made behind closed doors. It is published two years later in aggregated form. By then the guilty have received their bonuses and the victims have written off their losses.

**On-chain:** the decision is recorded in a block at the moment it is made. Append-only — you cannot retroactively change the terms, substitute the collateral valuation, or conceal the fact. The timestamp is unforgeable. The central bank's balance sheet is verifiable by any participant in real time, not weekly in aggregates (like the Fed's H.4.1). Lending parameters live in a smart contract: the rate is accessible to the `CB_GOVERNOR` role, expanding the collateral list requires a `CB_BOARD + PARLIAMENT` multisig, an emergency program is a time-locked contract with automatic rollback.

**What changes:** not the impossibility of "manual override", but its *costliness*. The security services and the executive are not stripped of their instruments — but every use of them becomes a public event with specific people accountable.

The same logic scales to QE, currency interventions, corporate rescue decisions. Not "trust but verify" — "verify, because otherwise it doesn't execute". The state audit office stops being a bureaucratic machine and becomes an interface to the blockchain — not the body that *inspects*, but the body that *interprets* publicly available data.

### Practice: the hybrid and its limits

The compromise option is PoA (Proof of Authority): nodes in the regions or at licensed banks, separation of powers in code (executive = `freeze()`, judiciary = `unfreeze()` upon a warrant, rule changes via a parliamentary majority in hardcoded form, and so on). The ratchet effect here works in reverse as well: the state adopts transparency to control the lower levels — but thereby binds itself too, reinforcing the separation of powers and the rule of law. A protocol is harder to roll back than a law.

But PoA is a half-measure. The state controls the validators — and can change the rules. A permissioned chain under executive control is a distributed database with append-only properties, but without independence from those whose actions it records.

The alternative is public chains. By 2026 the US is moving exactly there: the GENIUS Act protected permissionless transactions, RWA and stablecoins are being deployed on Ethereum and L2s, Chainlink is integrating the stock market through oracles. The trade-off is different: the state delegates part of its sovereignty to the network — but that is precisely what constrains its arbitrariness. Miners can censor (OFAC + Tornado Cash), whales influence governance — but that is the distributed arbitrariness of thousands of actors with divergent interests, not the concentrated arbitrariness of one.

The likely outcome is a hybrid: state operations on a permissioned layer, anchored to a public chain via ZK proofs. The state publishes a proof of the correctness of its operations without revealing the details of the transactions. Its own chain — for sovereignty; the public one — for trust. That is the bridge mBridge *could have* built — but chose a closed circuit instead.

No one is designing a "crypto-state" — but cost optimization is building its infrastructure. Financial institutions adopt on-chain to cut settlement costs, not out of ideology. The path of least resistance: financial markets → RWA → property registries → government spending. Blockchain lowers the cost of exit — and the exit option disciplines the government. But the rule of law is a requirement, not a consequence: El Salvador adopted Bitcoin as legal tender (substantially curtailed in early 2025 under IMF pressure), yet without the rule of law this created neither transparency nor accountability.

---
## Concluding the "Fiat for Self-Owners" series

Money is a complex, many-sided phenomenon. A system of relationships that has been evolving for thousands of years. Fiat is an institution performing the function of an elastic credit machine, with specific properties and limitations. Cryptocurrencies are not a replacement but a new meta-architecture of parallel institutions — solving some problems while carrying limitations of their own.

Blockchain is a layer of consistency, transparency, and accountability — for crypto infrastructure and for the fiat machine itself. Bridges between the worlds arise in different forms: stablecoins, oracles, RWA, prediction markets, or, say, the potential application to monetary policy: a ledger of central bank operations that cannot be rewritten after the fact, smart-contract constraints on discretionary powers, ZK bridges to public networks. Fiat keeps its elasticity, while blockchain makes abuses expensive and public. Paradoxically, implementing such solutions works to strengthen statehood: less shadow arbitrariness at the center and on the ground makes observing your own laws more profitable than playing at exceptions and privileges.

Abandoning the most maximalist reading of the term trustless (as a total renunciation of trusting anyone) in favor of the idea of decentralizing trust and the primacy of institutionalism ("all power to no one") makes it possible to overcome fundamental problems of many financial and political systems at once. On-chain reputation, p2p trust networks, self-banking — a decentralized implementation of Identity/Intent/Recourse, compatible with existing institutions but stripping them of their monopoly.

CBDC and its companion projects are attempts to turn progress against its own nature: to centralize what was created for decentralization. A permissioned blockchain between central banks is the maximum irony. Gold Standard 2.0 is a repetition of a mistake economists diagnosed a century ago. The direction of transparency (*who is transparent to whom*) is the key line of conflict.

Convergence is inevitable. The question is how it will proceed, and whether the monopoly on Identity can be dismantled. But that, I suppose, is a subject for future essays.

---

## Sources

### Theoretical foundation (series)

- Menger, "On the Origins of Money" (1892)
- Mitchell-Innes, "What is Money?" (1913)
- Hayek, "Denationalisation of Money" (1976)
- Minsky, "Stabilizing an Unstable Economy" (1986)
- Eichengreen, "Golden Fetters: The Gold Standard and the Great Depression" (1996)
- Mehrling, "The New Lombard Street: How the Fed Became the Dealer of Last Resort" (2010)
- Bank of England, "Money creation in the modern economy" (2014)

### Blockchain, identity, and trust

- Vitalik Buterin, "Trust Models" (2020) and "The Meaning of Decentralization" (2017) — the trustless spectrum
- Weyl, Ohlhaver, Buterin, "Soulbound Tokens" (2022)
- Balaji Srinivasan, "The Network State" (2022)
- W3C, "Decentralized Identifiers (DIDs) v1.0" (2022)
- FIDO Alliance, "Passkeys: A Global Adoption Report" (2025)
- Lisanne Bainbridge, "Ironies of Automation" (1983)
- EIP-1559: Fee market change for ETH 1.0 chain
- EIP-7805: Fork-Choice Enforced Inclusion Lists (FOCIL)

### US regulation

- White House, Executive Order "Strengthening American Leadership in Digital Financial Technology" (2025-01-23)
- GENIUS Act (S.1582), signed 2025-07-18 — [congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/1582)
- SEC & CFTC, Joint "Project Crypto" announcement (2026-01-29) — [sec.gov](https://www.sec.gov/newsroom/speeches-statements/atkins-remarks-joint-sec-cftc-harmonization-event-project-crypto-012926)
- SEC & CFTC, Memorandum of Understanding (2026-03-11) — [sec.gov](https://www.sec.gov/newsroom/press-releases/2026-26-sec-cftc-announce-historic-memorandum-understanding-between-agencies)
- U.S. Treasury, "Innovative Technologies to Counter Illicit Finance Involving Digital Assets" (2026-03-06) — [treasury.gov (PDF)](https://home.treasury.gov/system/files/246/GENIUS-Act-Illicit-Finance-Innovation-Congressional-Report-March-2026.pdf)
- Operation Choke Point, OIG Report, U.S. Department of Justice (2013)
- Galaxy Research, "Senate Crypto Bill: Biggest Surveillance Expansion Since the Patriot Act" (2026-01-14) — [theblock.co](https://www.theblock.co/post/385525/galaxy-senate-crypto-bill-could-mark-biggest-financial-surveillance-expansion-since-patriot-act)

### Debanking and precedents

- Federal Court of Canada, _Canadian Civil Liberties Association v. Canada_, 2024 FC 42 (2024-01-23) — Emergencies Act use ruled unlawful
- Federal Court of Appeal of Canada, unanimous ruling upholding FC 42 (2026-01)

### CBDC, mBridge, and the BRICS Unit

- BIS Innovation Hub, "Project mBridge: Connecting economies through CBDC" (2024)
- Finance Magnates, "BIS Exits from mBridge CBDC Project After BRICS Summit" (2024-10)
- OMFIF, "Gold-backed digital currency for BRICS" (2024-12-22)
- IRIAS / The Unit pilot on Cardano (2025-10-31) — [CCN overview](https://www.ccn.com/education/crypto/dollar-debasement-fears-brics-gold-backed-unit-currency-explained/)
- Fisher Investments, "Squashing Fears of the BRICS 'Unit'" (2025-12-11)
- TFIG Global News, "BRICS Gold-Backed Unit" (2025-12-19)

### DeFi, stablecoins, and infrastructure

- Chainlink blog, "24/5 US Equities Streams" (2026-01-20)
- DeFi Education Fund, annual review (2025)
- Kalatori — open-source payment daemon — [github.com/Kalapaja/Kalatori](https://github.com/Kalapaja/Kalatori)

### Data

- FRED (M2SL, BOGMBASE) — [fred.stlouisfed.org](https://fred.stlouisfed.org)
- CoinGecko — [coingecko.com](https://www.coingecko.com)
- DeFi Llama — [defillama.com](https://defillama.com)
