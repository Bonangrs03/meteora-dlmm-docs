# Chapter 7: The Hidden Cost — Impermanent Loss

---

## Back to Budi

Remember Budi's inventory risk from Chapter 3? He bought pulsa vouchers at Rp 9,800, and then the provider dropped the price to Rp 8,000. His inventory was suddenly worth less.

LPing has the exact same risk. But in DeFi, it has a specific name: **impermanent loss.**

## What Is Impermanent Loss?

Impermanent loss happens when the price of the assets you deposited changes relative to each other — and the change makes your position worth *less* than if you had just held the assets separately.

Let's make that concrete.

## The Scenario

You deposit into a SOL-USDC pool:

| Your Deposit | Amount | USD Value |
|-------------|--------|-----------|
| SOL | 1 SOL | $200 (at $200/SOL) |
| USDC | 200 USDC | $200 |
| **Total** | | **$400** |

The pool functions. Trades happen. You earn some fees.

Then SOL's price doubles. It's now $400 per SOL.

If you had just held your 1 SOL and 200 USDC separately:

| Asset | Amount | New Value |
|-------|--------|-----------|
| SOL | 1 SOL | $400 |
| USDC | 200 USDC | $200 |
| **Total if held** | | **$600** |

$600. You'd be up $200.

But you didn't hold separately — you put your assets in the pool. Let's see what happens inside the pool.

## What the Pool Does When SOL Doubles

The pool's formula is x × y = k. When SOL's market price doubles, arbitrage traders rush in. They buy SOL from the pool (which is still priced around $200) and sell it on the open market at $400, pocketing the difference.

This buying drains SOL from the pool and adds USDC. After arbitrage settles, the pool rebalances:

| Pool Asset | Before (SOL at $200) | After (SOL at $400) |
|------------|----------------------|---------------------|
| SOL in pool | 10 SOL (from all LPs) | ~7.07 SOL |
| USDC in pool | 2,000 USDC | ~2,828 USDC |

Your share (let's say 10%):

| Your Share | Amount | Value at $400/SOL |
|------------|--------|-------------------|
| SOL | 0.707 SOL | $282.80 |
| USDC | 282.80 USDC | $282.80 |
| **Total from pool** | | **$565.60** |

Compare:

| Scenario | Value |
|----------|-------|
| If you just HELD | $600.00 |
| If you LP'd | $565.60 |
| **Impermanent Loss** | **$34.40 (5.7%)** |

You lost $34.40 compared to just holding. That's impermanent loss.

## Why "Impermanent"?

The loss is called *impermanent* because it's not locked in until you withdraw. If SOL's price returns to $200, your pool share returns to 1 SOL + 200 USDC. The loss disappears. It was temporary.

But if you withdraw while the price is still $400? The loss becomes **permanent.**

## The Cruel Math

Here's how impermanent loss scales with price change:

| Price Change | Impermanent Loss |
|-------------|------------------|
| 1.25× (25% up) | ~0.6% |
| 1.5× (50% up) | ~2.0% |
| 2× (100% up) | ~5.7% |
| 3× (200% up) | ~13.4% |
| 5× (400% up) | ~25.5% |
| 10× (900% up) | ~42.5% |

The more the price moves — in EITHER direction — the more you lose compared to simply holding.

## The Mental Model

Think of the AMM pool as a force that **fights price changes.**

When SOL price goes up, the pool sells SOL (to arbitrage traders) to push the price back down.
When SOL price goes down, the pool buys SOL to push the price back up.

As an LP, you're on the wrong side of every major price move. The pool automatically "buys high and sells low" from your perspective. That's the source of impermanent loss.

## Can Fees Make Up for It?

Yes — that's the whole game.

If you earn enough in fees to outweigh the impermanent loss, you're profitable. If not, you'd have been better off just holding.

| Scenario | Fees Earned | Impermanent Loss | Net Result |
|----------|------------|------------------|------------|
| Stable pair (USDC-USDT) | 5% APR | ~0% | ✅ Profitable |
| Moderate volatility (SOL-USDC) | 30% APR | 5.7% IL | ✅ Profitable |
| Extreme volatility (new memecoin) | 200% APR | 42.5% IL | ❌ Net loss |

This is why experienced LPs prefer:
- **Stable pairs** (low IL, steady fees)
- **High-volume pairs** (lots of fees to offset IL)
- **Short time horizons** (less chance of big price moves)

## One Concept to Take Away

> **Impermanent loss** = the difference between what your assets are worth inside the pool vs what they'd be worth if you just held them. It grows as the price moves away from your entry point. Fees must outweigh it for you to profit.

This is the single most important concept to understand before you become an LP. If you only remember one thing from this entire document, make it this: **LPing is not free money. You are selling volatility and getting paid in fees.**

---

*Next: We've been talking about pools in the abstract. Now let's look at a specific blockchain — why Solana? Why not Ethereum? What difference does the underlying technology make?*
