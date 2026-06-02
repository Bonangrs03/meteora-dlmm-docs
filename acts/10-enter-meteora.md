# Chapter 10: Enter Meteora DLMM

---

## The Next Evolution

We've built up, piece by piece:

- Chapter 5: The AMM formula x × y = k — a pool that trades automatically
- Chapter 9: Concentrated liquidity — putting your money only where it matters

Now: what if we took concentrated liquidity and rebuilt it from scratch — specifically for a blockchain with near-zero fees and sub-second finality?

That's Meteora DLMM.

## What DLMM Stands For

**D**ynamic **L**iquidity **M**arket **M**aker.

Each word matters:

| Word | What It Means |
|------|---------------|
| **Dynamic** | Fees adapt to market conditions. More volatility = higher fees. |
| **Liquidity** | It's about providing assets for trading — just like Budi. |
| **Market Maker** | It replaces the human middleman with code — just like the AMM. |

## The Core Idea: Bins

Remember how concentrated liquidity (Chapter 9) lets you choose a price range? DLMM takes this further by dividing the price range into discrete steps called **bins.**

Think of a ladder. Each rung is a specific price. Your liquidity sits on specific rungs.

```
Price Ladder for a SOL-USDC pool:

$180.00  ← Bin 0
$180.50  ← Bin 1    (if bin step = 0.25%)
$181.00  ← Bin 2
$181.50  ← Bin 3
$182.00  ← Bin 4     ← CURRENT PRICE (Active Bin)
$182.50  ← Bin 5
$183.00  ← Bin 6
  ...
```

Only ONE bin is active at a time — the bin where the current market price sits. That's where all the trading happens.

## What Happens Inside a Bin

Here's something surprising: trades inside a single bin have **zero price impact.**

Remember back in Chapter 5, every trade moved the price in a traditional AMM? Not here. Inside a single bin, the price is fixed. You can trade up to that bin's capacity at exactly that price.

The price only changes when a bin is fully drained and the active bin shifts to the next one — just like stepping to the next rung on a ladder.

This means DLMM provides better prices for traders (no slippage on small trades) while still protecting LPs (the price can't run away within a single bin).

## The Bin Step

The gap between bins is called the **bin step,** measured in basis points (bps).

> 1 bp = 0.01%

| Bin Step | Price Gap (at $200 SOL) | Best For |
|----------|------------------------|----------|
| 1 bps (0.01%) | $0.02 | Stable pairs (USDC-USDT) — very tight, very precise |
| 10 bps (0.10%) | $0.20 | Major pairs (SOL-USDC) — balanced |
| 25 bps (0.25%) | $0.50 | Moderate volatility |
| 100 bps (1%) | $2.00 | Volatile pairs — wider coverage |
| 400 bps (4%) | $8.00 | Extreme volatility — maximum range |

**Smaller bin step = tighter ladder, more precision, higher capital efficiency** (if you guess the right range).
**Larger bin step = wider coverage per bin,** better for volatile assets where price moves fast.

This is a choice you make when you provide liquidity — and it's one of the most important decisions.

## The Dynamic Fee: Market-Aware Pricing

Most AMMs charge a fixed fee on every trade (0.3%, 1%, etc.). Whether the market is calm or chaotic — same fee.

DLMM's fees are **dynamic.** They have two components:

### 1. Base Fee (Always Charged)

The minimum fee, set when the pool is created. Depends on the bin step and some pool parameters. Think of this as the "floor."

### 2. Variable Fee (Volatility Bonus)

When the market gets volatile — when trades cross lots of bins, when price is moving fast — the variable fee kicks in and rises. When things calm down, it decays back to zero.

**Total Fee = Base Fee + Variable Fee** (capped at 10% maximum)

### Why This Matters

| Market Condition | What Happens to Fees | Why |
|-----------------|---------------------|-----|
| Calm, sideways market | Low fees (near base) | Attract more trading volume |
| Volatile, fast-moving | High fees (base + variable) | Protect LPs from being picked off by arbitrage |
| Extreme volatility | Very high fees | Compensate LPs for the risk of impermanent loss |

This is smart. In traditional finance, market makers widen their spreads during volatile periods. DLMM does the same thing automatically.

Think of it like this: when the market is calm, your shop is open with competitive prices. When a storm hits and everyone panics, you raise your prices because serving customers is riskier. Makes sense, right?

## Fee Collection: You Choose What You Get Paid In

When you earn fees as an LP, DLMM gives you two choices:

| Mode | What You Receive |
|------|-----------------|
| **Input Only** | Fees are split between both tokens — you get some SOL and some USDC. Balanced. |
| **Only Y** | All fees are paid in the quote token (USDC in SOL-USDC pool). You only accumulate USDC. |

Why would you choose "Only Y"? If you believe SOL will go up, you might want your fees in USDC so you're not forced to hold more SOL at potentially inflated prices. Or maybe you just want predictable stablecoin income without adding to your SOL exposure.

It's a small detail that gives you more control.

## Bins Are Grouped: Bin Arrays

Behind the scenes, bins are organized into groups of 70 called **BinArrays.** This is a technical optimization — you don't need to worry about it as a user, but it explains why you see certain limits in the UI.

The default pool can handle trades across about 1,024 bin arrays (from index -512 to +511), covering a massive price range. For extreme cases, an extension mechanism handles bins far outside that range.

## One Concept to Take Away

> **DLMM** = concentrated liquidity organized into discrete price bins (like a ladder), with dynamic fees that rise during volatility and fall during calm markets.

You put your liquidity into specific bins around the current price. Only the active bin processes trades. When it's drained, the ladder steps to the next bin. Your fees adapt to how crazy the market is.

---

*Next: How is DLMM different from Uniswap V3 (the most famous concentrated liquidity protocol)? What makes it uniquely suited to Solana?*
