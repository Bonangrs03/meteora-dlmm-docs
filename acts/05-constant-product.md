# Chapter 5: The Math Inside the Machine

---

## The Simplest Possible Formula

The AMM needs one rule to set prices. Remember Budi's instinct: *when people buy, price goes up. When people sell, price goes down.*

The most famous AMM formula — the one that launched a trillion-dollar industry — captures this with middle-school math:

> **x × y = k**

That's it. That's the formula.

Let's unpack it.

## What x, y, and k Mean

Imagine a pool containing two assets: **SOL** (a cryptocurrency) and **USDC** (a digital dollar, always worth ~$1).

| Variable | Meaning | Example |
|----------|---------|---------|
| **x** | How much SOL is in the pool | 10 SOL |
| **y** | How much USDC is in the pool | 2,000 USDC |
| **k** | x × y — this number NEVER changes | 10 × 2,000 = **20,000** |

The pool starts with 10 SOL and 2,000 USDC. k = 20,000.

**The pool's job:** keep x × y = 20,000, no matter what trades happen.

## A Trade: Buying SOL from the Pool

You walk up and say: *"I want to buy 1 SOL from this pool. How much USDC do I need to pay?"*

Before your trade:
- x = 10 SOL, y = 2,000 USDC
- Price of 1 SOL = y / x = 2,000 / 10 = **$200 per SOL**

Now you take 1 SOL out. The pool will have 9 SOL left. But k must stay at 20,000.

```
After: x = 9 SOL
       x × y = 20,000
       9 × y = 20,000
       y = 20,000 / 9
       y = 2,222.22 USDC
```

So y changed from 2,000 to 2,222.22. That means **you must deposit 222.22 USDC** to take out 1 SOL.

You paid 222.22 USDC for 1 SOL. The "original" price was 200 USDC. You paid more.

**The price went up because you bought.** Budi's instinct, now formalized in math.

## The Trade in the Other Direction: Selling SOL

Now someone else comes and sells 1 SOL into the pool.

```
Before: x = 9 SOL, y = 2,222.22 USDC, price = 222.22 / 9 ≈ $246.91
After:  x = 10 SOL
        10 × y = 20,000
        y = 2,000 USDC
```

The pool gives them 222.22 USDC for their 1 SOL. The price went down. Just like Budi said.

## The Important Thing You Just Saw

Let's compare prices:

| Action | Price Before | Price After | Direction |
|--------|-------------|-------------|-----------|
| Someone BUYS SOL | $200 | $246.91 | 📈 Up |
| Someone SELLS SOL | $246.91 | $200 | 📉 Down |

**The formula automatically adjusts prices based on supply and demand.** No human. No order book. No auction. Just x × y = k.

## Why This Is Beautiful

This formula has properties that make it perfect for an automated market:

1. **It always works.** No matter how much someone wants to trade, the formula gives a price.
2. **It never runs out.** You can keep trading forever — the price just gets more and more extreme.
3. **It's predictable.** You can calculate exactly what you'll get before you trade.
4. **It has "slippage."** Big trades move the price more than small trades. This matches real markets.

That last point is important. Let's see it:

| Trade Size | SOL Bought | USDC Paid | Effective Price per SOL |
|------------|-----------|-----------|------------------------|
| Small | 0.1 SOL | ~19.61 USDC | ~$196 |
| Medium | 1 SOL | ~222.22 USDC | ~$222 |
| Large | 5 SOL | ~2,000 USDC | ~$400 |

Bigger trades get worse prices. This is called **price impact** or **slippage.** It's the AMM's way of protecting itself from being drained.

## The Pool as a See-Saw

Here's an intuitive way to think about x × y = k:

Imagine a see-saw with SOL on one side and USDC on the other. The see-saw must always balance at a constant "weight" (k).

- If SOL leaves the pool (someone buys), the SOL side gets lighter. To rebalance, USDC must increase. That means the price of SOL (USDC/SOL) goes UP.
- If SOL enters the pool (someone sells), the SOL side gets heavier. To rebalance, USDC must decrease. Price of SOL goes DOWN.

It's just a balancing act.

## One Concept to Take Away

> **x × y = k**: the constant product formula. It automatically sets prices so that buying pushes prices up and selling pushes prices down — exactly like a human market maker would, but run entirely by math.

You now understand the engine that powers almost all of DeFi. The pool is the market. The formula is the price. No middleman required.

---

*Next: The pool needs inventory. Where does it come from? And why would anyone provide it?*
