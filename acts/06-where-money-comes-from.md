# Chapter 6: Where Does the Money Come From?

---

## The Pool Needs Stuff

The AMM pool we built in Chapter 5 held 10 SOL and 2,000 USDC. That inventory came from somewhere.

In Budi's world, Budi used his own money to buy inventory. He put up Rp 5,000,000 of his own savings to buy pulsa vouchers. He bore all the risk, and he kept all the profit.

But crypto pools are different. The inventory doesn't come from one person. It comes from **anyone who wants to participate.**

## The Liquidity Provider (LP)

A **liquidity provider** (LP for short) is someone who deposits their assets into an AMM pool so the pool has inventory to trade with.

> **LP** = you, depositing your tokens into a pool so the AMM can function as a market maker.

In return for providing your assets, you earn a share of the fees from every trade that happens in that pool.

## How It Works, Step by Step

Let's say you have 1 SOL and 200 USDC. You notice a SOL-USDC pool exists.

**Step 1: You deposit.**
You put your 1 SOL and 200 USDC into the pool. The pool now has more inventory.

**Step 2: The pool uses your assets.**
Traders come and trade against the pool. Every trade pays a small fee (typically 0.3% or less).

**Step 3: You earn your share.**
If your deposit represents 10% of the total pool, you earn 10% of all fees collected.

**Step 4: You can withdraw anytime.**
When you want your money back, you withdraw your share of the pool — your original assets plus the fees you've earned.

## A Concrete Example

Let's trace it with numbers:

| Event | Pool State | Your Share |
|-------|-----------|------------|
| Pool starts | 10 SOL + 2,000 USDC | — |
| You deposit | 1 SOL + 200 USDC | 1/11 = 9.09% of pool |
| Pool now | 11 SOL + 2,200 USDC | — |
| 100 trades happen | Fees collected: ~10 USDC | Your cut: ~0.91 USDC |
| You withdraw | You get back your share | 1 SOL + ~200.91 USDC |

You earned ~0.91 USDC just for leaving your assets in the pool. Not life-changing, but imagine this running for a year with thousands of trades per day.

## Why Is This Good for the Pool?

The pool needs depth. A pool with 10 SOL can't handle a 5 SOL trade without massive price impact (remember Chapter 5). A pool with 1,000 SOL can handle that trade smoothly.

More LPs → deeper pool → less slippage → better trading experience → more traders → more fees → happier LPs.

It's a virtuous cycle. The entire DeFi ecosystem runs on it.

## Why Would Anyone Do This?

Three reasons:

| Reason | Explanation |
|--------|-------------|
| **Earn fees passively** | Your assets work for you while you sleep. Like interest in a bank account, but the yield comes from trading fees, not lending. |
| **Support a project you believe in** | Early LPs provide the liquidity that makes a new token tradable. Without LPs, new tokens have no market. |
| **Portfolio diversification** | Instead of just holding SOL, you can put it to work earning additional yield. |

## The Deal: What You Give vs What You Get

| You GIVE | You GET |
|----------|---------|
| Your assets (SOL, USDC, etc.) | A share of all trading fees |
| Your ability to sell at any moment (assets are locked in pool) | The right to withdraw anytime (no lockup period) |
| You bear inventory risk | You earn passive yield |

That third row — "you bear inventory risk" — is important enough to deserve its own chapter.

---

*Next: The hidden cost of being an LP. Why "just deposit and earn" isn't the full picture.*
