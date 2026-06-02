# Chapter 12: LP Strategies on Meteora

---

## You Now Know the Tool

You understand:
- What liquidity is (Ch 1)
- What a market maker does (Ch 2-3)
- How AMMs work (Ch 4-5)
- Where LP money comes from (Ch 6)
- The hidden cost of impermanent loss (Ch 7)
- Why Solana matters (Ch 8)
- Concentrated liquidity (Ch 9)
- How DLMM bins and dynamic fees work (Ch 10)
- How DLMM differs from alternatives (Ch 11)

Now: **how do you actually make money with it?**

## The Strategy Spectrum

DLMM strategies fall on a spectrum from "set it and forget it" to "actively manage every hour."

```
LOW EFFORT ←————————————————————————→ HIGH EFFORT
   Wide/Chill    Spot    Curve    Bid-Ask    20-Bin   Dynamic Vaults
```

Each has a different risk-reward profile. Let's walk through them.

---

## Strategy 1: Wide Range / "Chill"

**What it is:** Spread your liquidity across a very wide price range (e.g., ±20-30% from current price).

**How it works:**
- You pick a wide range around the current price
- Your liquidity is active as long as price stays in that range
- You barely need to check it

**Best for:** Stable pairs (USDC-USDT), pairs you believe will trade in a range for a long time, or if you just want to deposit and forget about it.

**Pros:**
- Very low maintenance
- Rarely goes out of range
- Good starting point for beginners

**Cons:**
- Lower capital efficiency (your money is spread thin)
- Lower fee earnings than concentrated strategies
- Still exposed to impermanent loss if price moves a lot

**Analogy:** You're a shop that sells everything from Rp 1,000 to Rp 1,000,000. Most customers won't buy the extreme ends, but you're always open for business.

---

## Strategy 2: Spot (Uniform Distribution)

**What it is:** Spread liquidity evenly across a moderate range (e.g., ±5-10%).

**How it works:**
- You choose a range around the current price
- Liquidity is distributed uniformly across all bins in your range
- The default and most common strategy

**Best for:** General purpose. Good when you don't have a strong directional view. The "I think it'll trade around here" strategy.

**Variations:**
| Name | Bin Count | Range Width | Use Case |
|------|-----------|-------------|----------|
| Spot-Concentrated | 1-3 bins | Very tight | Almost certain price is stable |
| Spot-Spread | 20-30 bins | Moderate | Balanced approach |
| Spot-Wide | ~50 bins | Wide | More safety, less efficiency |

**Pros:** Simple, versatile, balances efficiency with safety.
**Cons:** Not optimal for any specific market condition.

---

## Strategy 3: Curve (Concentrated Center)

**What it is:** Most of your liquidity concentrated tightly around the current price, with less at the edges.

**How it works:**
- You put heavy liquidity right at the active bin
- Less liquidity at bins further away
- Maximum capital efficiency when price stays near the center

**Best for:** Stable pairs (USDC-USDT), or any pair during a period of very low volatility.

**Pros:**
- Highest fee earnings when price stays in range
- Maximum capital efficiency

**Cons:**
- Goes out of range quickly if price moves
- Requires more frequent monitoring
- Worst impermanent loss if price trends strongly

**Analogy:** You're a coffee shop that's open 24/7 but only serves one specific type of coffee. When the neighborhood wants exactly that, you make a killing. When tastes change, you sit empty.

---

## Strategy 4: Bid-Ask (Directional)

**What it is:** Asymmetric distribution — more liquidity on one side than the other.

**How it works:**
- If you think price will go UP: put more liquidity ABOVE current price (selling into strength)
- If you think price will go DOWN: put more liquidity BELOW current price (buying the dip)
- The lighter side still earns some fees

**Best for:** When you have a directional view. You want to accumulate one asset or exit another.

**Pros:**
- Acts as automated DCA (dollar-cost averaging)
- You earn fees while waiting for your target price
- Combines trading strategy with LP yield

**Cons:**
- Requires some market judgment
- If you're wrong about direction, you miss fee opportunities on the other side

**Analogy:** You're at a fruit market. You believe mango prices will go up next week. You put more of your stall's space into buying mangoes now (at lower prices) while still selling some at a markup.

---

## Strategy 5: The 20-Bin Strategy (Current Meta)

This deserves special attention because it's become popular in the Meteora LP community as of 2026.

**What it is:** A specific configuration: 20-bin range with a smaller bin step (often 20 bps or less), aiming for high-frequency fee capture.

**How it works:**
- You use approximately 20 bins centered around the current price
- Small bin step means tight price granularity
- The idea: capture lots of small trades with high capital efficiency

**Why it's popular:**
- Good balance between efficiency and range safety
- Works well for medium-volatility pairs
- Community-tested and discussed extensively

**Real example:** During active trading periods, some 20-bin positions on volatile pairs have captured daily fees approaching 10% of position value. These returns are NOT typical or sustainable — they happen during short bursts of extreme volume — but they show what's possible when you're positioned correctly during volatility.

**The catch:** These high-return periods are episodic. A position that earns 10% one day might earn 0.3% the next.

---

## Strategy 6: Single-Sided / DCA

**What it is:** Deposit only ONE token type into a specific bin (or narrow range).

**How it works:**
- You deposit only USDC into a bin above current price → acts as a limit sell order
- You deposit only SOL into a bin below current price → acts as a limit buy order
- When price reaches your bin, your token converts to the other token

**Best for:** Accumulating an asset at a target price without watching charts. Or exiting at a target price.

**Pros:**
- Automated, emotion-free entry/exit
- No impermanent loss (you only hold one asset)
- You earn fees while your limit order waits

**Cons:**
- If price never reaches your bin, you earn nothing
- Opportunity cost: your capital is committed, not available for other uses

---

## How to Choose: A Decision Framework

Ask yourself these questions:

### 1. How stable is this pair?

| Pair Type | Example | Recommended Strategy |
|-----------|---------|---------------------|
| Stable-stable | USDC-USDT | Curve, very tight range |
| Major pair | SOL-USDC | Spot spread (20-50 bins) |
| Volatile | Memecoin-USDC | Wide, or Bid-Ask |
| New token | Launch pool | Very wide, or single-sided |

### 2. How much time do you have?

| Time Commitment | Strategy |
|-----------------|----------|
| Check once a week | Wide / Chill |
| Check daily | Spot |
| Check multiple times/day | Curve, Bid-Ask |
| Actively monitor | 20-Bin, Dynamic Vaults |

### 3. What's your market view?

| View | Strategy |
|------|----------|
| "It'll stay in a range" | Spot, Curve |
| "It'll go up" | Bid-Ask (more above current price) |
| "It'll go down" | Bid-Ask (more below current price) |
| "I want to buy at X price" | Single-sided below X |
| "I want to sell at Y price" | Single-sided above Y |
| "No idea" | Wide / Chill |

---

## Risk Management: The Non-Negotiables

Before you deploy a single dollar:

### 1. Check Total Fees Generated

The most important metric, according to experienced Meteora LPs: **total fees a pool has generated historically.**

A pool that has earned 500 SOL in cumulative fees is far more trustworthy than one with 5 SOL. Low total fees often indicate low genuine volume — or worse, fake volume designed to attract LPs.

> **Rule of thumb:** Don't LP into a pool with less than 25 SOL in total generated fees.

### 2. Vet the Token

If you're LPing into a token you don't know well:

- Check Rugcheck.xyz for token contract safety
- Check Bubblemaps for supply concentration (if 3 wallets hold 90% of supply, run)
- Look at the chart — is there real trading history or just a pump?
- Check social channels — is there a real community or just bots?

### 3. Start Small

Your first position should be an amount you're comfortable losing entirely. Treat it as tuition. Learn the mechanics, observe how fees accumulate, experience impermanent loss in real time — with money that won't hurt.

### 4. Don't Chase Extreme APR

If a pool shows 1000% APR, ask: why? Usually it's because:
- The token is volatile and you'll get wrecked by IL
- The volume is temporary (token launch hype)
- There's hidden risk you're not seeing

Sustainable returns come from genuine, consistent trading volume — not hype spikes.

---

## One Concept to Take Away

Your strategy choice answers three questions simultaneously:
- How much you'll earn (fee concentration)
- How much you'll lose if price moves (IL exposure)
- How much attention you'll need to pay (management frequency)

There's no best strategy — only the strategy that matches your capital, your time, and your risk tolerance.

---

*Next: Open the app. Let's actually do this. Step by step.*
