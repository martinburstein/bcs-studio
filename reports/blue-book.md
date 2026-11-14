# Adversarial Economics
## A short guide to incentives, feedback, and crypto

**The Big Crypto Short**  
**As of 14 November 2026 · Public educational edition**

This public edition is based on an AI-assisted synthesis with internal review. Internal review is not external scholarly peer review.

Markets join people, firms, contracts, rules, and software. Outcomes can turn on who knows what, who may decide, which promise binds, and who ultimately absorbs a loss. This guide uses **adversarial economics** as a practical lab framework assembled from established fields. It is not a unified science, and it does not assume that every institution is deceptive. The examples are fictional and teach mechanisms; they describe no issuer, exchange, account, or current market.

The method is simple: state a proposed mechanism, trace how it could affect cash flows, then look for the strongest reason it might not. The companion working paper, source-reading records, finite-model replay and public company casebook are available in this repository. The private lab retains drafts and the full research history. This booklet is a quick introduction to the questions that make those investigations useful.

## 1. Begin with incentives and authority

A principal delegates a task or decision to an agent. The principal might be a client or owner; the agent might be a manager, trustee, broker, adviser, or software service. Their goals, information, and ability to observe performance may differ. That difference creates an **agency problem**; it does not prove bad intent.

Jensen and Meckling’s theory of the firm treats firms as arrangements of contracts and analyzes costs that arise when control and financial claims are divided. Monitoring, commitments by the agent, and residual losses are all possible agency costs. Their framework helps explain why oversight and incentives matter even when participants act lawfully and an arrangement is efficient under its conditions. [R1]

Imagine an investment committee asking a manager to “protect capital.” The instruction is incomplete. Does it mean limiting a short-term decline, preserving purchasing power, meeting withdrawals, or avoiding permanent loss? The manager may be evaluated against quarterly results while the investor needs cash for a near-term expense. Before judging performance, identify the objective, decision rights, constraints, and who bears each outcome.

Delegation can create value: a specialist may have time or knowledge the principal lacks. Constant monitoring can be costly or can prevent useful discretion. So ask who set the goal, what the agent can observe, which actions it can take, and what evidence could show whether the task was carried out.

## 2. Ask who knows what

A price can hide a difference in quality. If sellers know more than buyers, a buyer may offer a price based on average quality. Sellers with stronger goods may then leave because the price is too low; the remaining mix can worsen, pushing the average estimate down again. This is the conditional adverse-selection mechanism in Akerlof’s famous used-car model—not a claim that uncertainty always destroys trade. Akerlof calls the automobile example a “finger exercise” chosen for clarity, and also discusses institutions that can counteract the problem, including reputation, guarantees, and enforcement. [R2]

Translate the question carefully. A reserve label, audit statement, insurance claim, or “decentralized” description may be accurate yet incomplete. What assets back a promise? At what valuation and maturity? Who can redeem, inspect, pause, or change the arrangement? Who verifies the information at the time a buyer must decide?

A fictional buyer looking at a pool of short-term bills and longer-term loans may not know what can be sold near face value today. If both types are grouped under one label, the buyer may price the whole pool cautiously. That price could discourage holders of the stronger claims from staying. This illustrates what would matter if quality were hard to distinguish; it establishes no defect at any real issuer.

**Stabilizers matter too.** Reputation, disclosure, independent verification, guarantees, custody, and enforcement can improve trust or allocate losses. Akerlof directly discusses some institutions; modern examples such as third-party custody and collateral haircuts are extensions, not findings tested in his article. A missing document is uncertainty, not proof of hidden damage. The practical question is which verification and recourse work in the case being studied.

## 3. Follow the crowd and the balance sheet

A useful service can create a vulnerability. A bank funds longer-lived loans with deposits that customers expect to withdraw on demand. The transformation supplies liquidity to depositors and funding to borrowers, but creates a timing mismatch. Diamond and Dybvig show how, under their model’s assumptions, a demand-deposit contract can support useful risk sharing and multiple equilibria, including a costly run. A run can force early liquidation even when the bank was viable under patient funding. Their analysis also studies ways contracts and policy can prevent runs; its result is not a template for every token or exchange. [R3]

Consider a fictional warehouse with 10 million one-dollar claims and $10 million of assets: $8.5 million in cash-like assets and $1.5 million in loans carried at par. These are teaching assumptions, not observed data. If holders request $9.5 million at once, the cash leaves a $1 million gap. With no other assets or credit, and a 20% sale discount, each dollar of loans sold yields 80 cents. To raise $1 million, the warehouse must sell $1 million ÷ 0.80 = $1.25 million of loans, realizing a $250,000 loss against par. It then has $500,000 of claims left but only $250,000 of unsold loans, a $250,000 shortfall under these assumptions. A credit facility, different redemption terms, or assets realizable at par would change the result.

To study a coordination-based run, examine what holders expect others to do, redemption priorities, and incentives to wait or withdraw. The cash-flow arithmetic alone does not establish a coordination mechanism. Relevant evidence includes redemption rights, asset maturity, reserve access, queue design, payment rails, credit lines, and loss-allocation rules. Liquidity buffers, insurance, gates, suspension rules, and emergency lending can slow a rush; each can carry costs or shift losses to someone else.

Funding and market liquidity can also reinforce one another. A leveraged trader facing a collateral call may sell; the sale can depress prices and reduce the value of collateral, prompting more sales. Minsky’s financial-instability hypothesis examines how payment commitments and financing structures can amplify movements. His cash-flow categories—covering payments, refinancing principal, or failing to cover commitments—describe financing, not moral character or a mechanical forecast. [R4]

Brunnermeier and Pedersen formalize a two-way link between traders’ funding capacity and the liquidity they provide to markets. Under specific conditions, margins, funding constraints, and losses can interact in a liquidity spiral. Their model also contains stabilizing conditions, including informed financiers or adequate capital, and does not test whether automation adds to the mechanism. [R5]

Keep four terms distinct:

- **Market liquidity:** how much can be traded, how quickly, and with what price impact.
- **Funding liquidity:** whether cash or credit is available when an obligation falls due.
- **Solvency:** whether assets cover liabilities under a stated valuation and recovery rule.
- **Systemic harm:** whether disruption spreads to other institutions, credit, or payments.

A solvent entity may run short of cash before assets mature; a quoted price alone does not establish solvency. Cash buffers, long-term funding, diverse counterparties, lenders with capital, and credible support can interrupt a spiral. Whether those brakes exist is an empirical question. Trace the sequence: which shock changes which collateral requirement, who must sell, what depth exists at that size, and who can finance the next step?

## 4. A price is evidence, not an oracle

Prices combine orders submitted for different reasons. In Kyle’s sequential-auction model, an informed trader, random noise traders, and competitive market makers interact. Noise orders make it harder for market makers to distinguish informed trades, giving the informed trader camouflage. The model helps analyze information in prices and market liquidity; it does not tell us that a particular price move reflects private information or that real crypto order flow follows the model. [R6]

A sudden decline might reflect new information, forced liquidation, hedging, a redemption, or thin market depth. A chart alone rarely identifies the cause. Size, venue, timing, settlement, and counterparty affect the price an investor can actually obtain. A displayed quote and an executable exit are different observations.

Markets can aggregate information and arbitrage can correct stale prices. But arbitrage needs capital, financing, short availability, settlement access, and workable rules. The price remains useful evidence, but it is produced by the very system under study. Avoid treating it as independent confirmation of a causal story that already assumes what caused the move.

## 5. Rules and software shape the result

Economic activity happens inside contracts, property rights, and enforcement. A protocol can distribute authority among developers, token holders, validators, service providers, users, and a legal issuer. “Decentralized” alone does not identify who can change software, pause a feature, choose an input, reverse an error, or enforce a promise.

Map four things: **objective** (what outcome is rewarded or protected); **information** (what is available, verified, delayed, or missing); **authority** (who can act, and within what limits); and **loss allocation** (who bears an error, shortfall, or interruption). The same software can play very different roles depending on permissions. A program that recommends a price is not equivalent to one that can set a binding price or spend delegated funds.

Herbert Simon challenged decision models that assume complete information and unlimited calculation. People and organizations use simplified procedures because their information and computational capacities are limited. Applying that insight to contemporary software is a modern extension, not Simon’s claim about AI. [R7]

Simon also examined computer programs as factors of production and compared software with human labor in certain tasks. This is a way to analyze productive capability, not a claim that programs own assets, hold legal standing, or have personal intentions. [R8]

## 6. Adaptation is a mechanism, not a motive

Some models hold decision rules fixed; others let them adjust through feedback. Arthur describes inductive reasoning as forming hypotheses, comparing them with results, and revising them when performance weakens. Such models can explore how different rules interact. They are tools for examining assumptions, not forecasts that agents converge on one outcome. [R9]

Calvano and coauthors studied Q-learning algorithms in a simulated repeated pricing game. In their specified environment, the algorithms learned prices above the competitive level without communicating. The result depends on the study’s model and parameters; the authors discuss limitations, including the time needed for learning. It does not show that deployed firms’ systems collude, that all learning systems produce this result, or that software has human intentions. [R10]

For economic analysis, describe a computational system by what it does: its reward rule, available signals, choice of actions, ability to update, control over resources, and whether an action is binding or can be rejected. A fixed inventory rule differs from a service that selects suppliers, negotiates within a budget, observes delivery outcomes, and repeats. Neither needs psychological desires for the distinction to matter.

Automation can also stabilize. It may process information quickly, lower costs, enforce risk limits, or supply liquidity. The relevant comparison asks whether a deployed system’s actual permissions and feedback create a mechanism beyond what a human or fixed-rule baseline would produce. Software has long routed orders and executed human-selected rules; a claim of novelty needs a specific comparison, not a slogan about the first nonhuman actor.

## 7. Carry the questions into crypto

Crypto combines familiar relationships in varied technical and legal forms. An exchange may match traders and hold custody. A stablecoin issuer may promise conversion at par while investing reserves. A lending protocol may require collateral and liquidate it at a threshold. A bridge may rely on a limited set of signers. A governance token may vote on a parameter that affects users. These arrangements differ; “crypto” is not one balance sheet or one contract.

For any proposed fragility story, ask:

1. **Agency:** Who chose the objective, delegated authority, wrote the rule, and can upgrade it?
2. **Information:** Can users verify assets, liabilities, collateral, and maturity when they transact?
3. **Coordination:** Could withdrawals, votes, or redemptions reward moving before others?
4. **Funding:** What obligation forces a sale after a price move, and who can supply cash?
5. **Market structure:** Is there enough executable depth at the necessary size, venue, and time?
6. **Institutions:** Which promises are enforceable, and who can halt or repair the system?
7. **Computation:** Are actions proposed or binding, fixed or adaptive, independent or correlated?

A conditional hypothesis could be: *If many participants rely on the same collateral valuation, if falling prices trigger mandatory sales, if those sales materially reduce market depth, and if alternative funding is unavailable, then a common shock could amplify losses.* Each “if” needs evidence. The chain could fail at any link: the valuation may not be shared; liquidation may be small; buyers may step in; credit may remain available; or a rule may pause the process.

The strongest opposing account is that ordinary fundamentals, leverage, market design, or legal obligations may explain observed stress without any additional role for AI. Traders can have different goals and move in different directions. Algorithms may enforce useful limits or provide liquidity. Reserves, better collateral terms, outside financing, public transaction records, or regulatory changes may stabilize a system. The analysis should change if these explanations fit the evidence better.

An AI-enabled fragility claim requires an additional demonstration: deployed systems have consequential authority; their goals, inputs, or update rules create correlated actions; those actions interact with contracts or balance sheets; and the resulting loop is stronger than a suitable non-automated comparison. Fast computation alone is not systemic risk. The literature cited here supplies mechanisms from distinct settings; it does not establish a unified AI-driven crypto fragility effect or a present-day prediction.

A useful case file follows **observation → mechanism → trigger → binding constraint → response → cash-flow effect → loss bearer → counterevidence**. For a reserve claim, inspect reserve composition and redemption terms. For a liquidation claim, inspect the trigger, price source, margin rule, and executed sale. For a computational claim, inspect the deployed version, permissions, inputs, overrides, and logs. If the evidence cannot connect an event to an actual cash flow or authorized instrument, the conclusion may be “not established.”

This is where the short guide ends and detailed casework begins. The public Black Book presents dated company cases, competing explanations and unresolved evidence. The companion AI/crypto working paper remains unsubmitted and has no external peer review. Personal portfolio scenarios and account-specific material remain in the private lab.

## A compact checklist

Before accepting an attractive explanation, write down:

- What does the consensus story assume will continue?
- Which outcome has been ignored rather than tested?
- Who has the strongest evidence and reason to disagree?
- What information, decision right, or contract term is missing?
- What rule forces a response, and whose cash flow changes?
- What stabilizer could interrupt the chain?
- Which observation would make the explanation weaker or lead us to abandon it?

A strong investigation can end without an investment conclusion. Missing data, an unverified event-to-payoff bridge, unavailable funding, or an unworkable exit may be the main result.

## Ten references

R1. Jensen, Michael C., and William H. Meckling. “Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure.” *Journal of Financial Economics* 3 (1976): 305–360. [Article copy](https://www.liuyanecon.com/wp-content/uploads/JensenMeckling-1976.pdf).

R2. Akerlof, George A. “The Market for ‘Lemons’: Quality Uncertainty and the Market Mechanism.” *Quarterly Journal of Economics* 84, no. 3 (1970): 488–500. [Article scan](https://pims.math.ca/files/Akerlof1970.pdf).

R3. Diamond, Douglas W., and Philip H. Dybvig. “Bank Runs, Deposit Insurance, and Liquidity.” *Journal of Political Economy* 91, no. 3 (1983): 401–419. [Article scan](https://users.econ.umn.edu/~tkehoe/classes/DiamondDybvig.pdf).

R4. Minsky, Hyman P. “The Financial Instability Hypothesis.” Levy Economics Institute Working Paper 74 (May 1992; prepared for a 1993 handbook). [Working paper](https://www.levyinstitute.org/pubs/wp74.pdf).

R5. Brunnermeier, Markus K., and Lasse Heje Pedersen. “Market Liquidity and Funding Liquidity.” *Review of Financial Studies* 22, no. 6 (2009): 2201–2238. [Article copy](https://www.edegan.com/pdfs/Brunnermeier%20Pedersen%20%282009%29%20-%20Market%20Liquidity%20and%20Funding%20Liquidity.pdf).

R6. Kyle, Albert S. “Continuous Auctions and Insider Trading.” *Econometrica* 53, no. 6 (1985): 1315–1335. [Article scan](https://www.edegan.com/pdfs/Kyle%20%281985%29%20-%20Continuous%20Auctions%20and%20Insider%20Trader.pdf).

R7. Simon, Herbert A. “A Behavioral Model of Rational Choice.” *Quarterly Journal of Economics* 69, no. 1 (1955): 99–118. [Article scan](https://cooperative-individualism.org/simon-herbert_a-behavioral-model-of-rational-choice-1955-feb.pdf).

R8. Simon, Herbert A. “Programs as Factors of Production.” Archival proceedings reprint, catalogued 1967; exact meeting year and printed pagination unconfirmed in the retained copy. [Archival reprint](https://iiif.library.cmu.edu/file/Simon_box00065_fld04984_bdl0001_doc0001/Simon_box00065_fld04984_bdl0001_doc0001.pdf).

R9. Arthur, W. Brian. “Inductive Reasoning and Bounded Rationality.” *American Economic Review* 84, no. 2, Papers and Proceedings (1994): 406–411. [Article scan](https://ocw.tudelft.nl/wp-content/uploads/ElFarolArtur1994.pdf).

R10. Calvano, Emilio, Giacomo Calzolari, Vincenzo Denicolò, and Sergio Pastorello. “Artificial Intelligence, Algorithmic Pricing, and Collusion.” *American Economic Review* 110, no. 10 (2020): 3267–3297. This booklet’s retained source is the authors’ December 2019 manuscript. [Manuscript](https://www.tse-fr.eu/sites/default/files/TSE/documents/ExEdu/paper_1_calvano.pdf).

These are ten distinct theoretical, archival, and simulation works, not ten replications. The references support mechanisms within their stated settings, not current crypto behavior, an inevitable collapse, or an estimated crash probability. Page locators, source-host provenance, retained-body hashes, and reading limits are recorded in the public source-reading ledger, `evidence/blue-book-sources.json`.
