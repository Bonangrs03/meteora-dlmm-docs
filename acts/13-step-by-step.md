# Chapter 13: Step-by-Step Walkthrough

---

> **Reality check:** This chapter describes the Meteora dApp interface conceptually. UIs change. Buttons move. The principles don't. If a specific button isn't where I describe it, look for the concept — "create position," "choose pool," "set range" — not the exact pixel location.

---

## Step 0: Before You Touch Anything

You need three things:

| What | Why | How |
|------|-----|-----|
| **A Solana wallet** | To hold your tokens and sign transactions | Phantom, Solflare, or Backpack wallet |
| **Some SOL** | To pay for transactions (~0.000005 SOL each) | Buy on an exchange, transfer to your wallet |
| **Tokens to LP with** | The assets you'll deposit into the pool | SOL + USDC is the most common pair |

For this walkthrough, we'll assume you're LPing into a SOL-USDC pool. It's the most liquid pair on Solana and the safest starting point.

## Step 1: Create/Get a Solana Wallet

If you don't have one:

1. Go to [phantom.app](https://phantom.app) and install the browser extension (or mobile app)
2. Create a new wallet
3. **Write down your seed phrase on paper.** Not a screenshot. Not a notes app. Paper. Store it somewhere safe.
4. Set a strong password

## Step 2: Fund Your Wallet

1. Buy SOL from an exchange (any major exchange sells SOL)
2. Withdraw SOL to your wallet address (a long string starting with letters/numbers — find it in Phantom under "Receive" or "Deposit")
3. Optionally, swap some SOL for USDC using Jupiter (jup.ag) inside your wallet

**Minimum starting amount:** With $20-50 worth of SOL + USDC, you can open a small LP position and learn the mechanics. On Ethereum this would be impossible due to gas fees. On Solana, it's real.

## Step 3: Navigate to Meteora

1. Go to [app.meteora.ag](https://app.meteora.ag)
2. Connect your wallet (click "Connect Wallet" in the top right, choose Phantom)
3. Approve the connection in your wallet popup

## Step 4: Find Your Pool

You'll see the Meteora interface with various pools listed. For your first position:

1. Click the **"Pools"** or **"DLMM"** tab
2. Search for **SOL-USDC**
3. You'll see multiple SOL-USDC pools with different bin steps (e.g., 5 bps, 20 bps, 50 bps)

**Which bin step to choose for your first position:**

| Bin Step | What It Means | Recommendation |
|----------|---------------|----------------|
| 5 bps | Very tight, very efficient | Skip for now — too aggressive |
| 20 bps | Moderate, popular choice | Good starting point |
| 50 bps+ | Wider, more forgiving | Safe for beginners |

Pick a 20 or 50 bps SOL-USDC pool.

## Step 5: Examine the Pool

Before depositing, look at:

- **Current price:** Where is SOL trading right now?
- **24h Volume:** How much trading activity? More volume = more fees.
- **TVL (Total Value Locked):** How much liquidity is already in this pool? Higher TVL means less of the fee pie for you, but also more stability.
- **24h Fees:** How much did LPs earn yesterday?
- **APR:** Approximate annual return (this fluctuates — don't fixate on it)

## Step 6: Open a Position

1. Click **"Create Position"** or the **"+"** button
2. You'll see a chart with the current price and a bin ladder

### Step 6a: Choose Your Strategy

Meteora's interface offers presets:

| Preset | What It Does |
|--------|-------------|
| **Spot** | Even distribution across your chosen range |
| **Curve** | Concentrated around current price |
| **Bid-Ask** | Heavier on one side |

For your FIRST position, choose **Spot** with a moderate range.

### Step 6b: Set Your Range

- Look at the current price (let's say SOL is $200)
- Set your minimum price (e.g., $180 — 10% below current)
- Set your maximum price (e.g., $220 — 10% above current)
- The interface shows how many bins this covers

**Range width guide:**

| Range Width | Risk Level | Maintenance |
|-------------|-----------|-------------|
| ±2-5% | High | Check daily |
| ±5-15% | Medium | Check every few days |
| ±20%+ | Low | Check weekly |

### Step 6c: Enter Your Deposit Amount

- You can deposit both tokens equally (requires you to have both)
- Or deposit one token and let the interface handle the swap (may involve a small cost)
- Start small — $20-50 total value for your first position

## Step 7: Review and Confirm

Before hitting confirm, check:

1. **Price range:** Is it where you want it?
2. **Amount:** Are you comfortable losing this if things go wrong?
3. **Bin step and fee:** Does the fee structure make sense?
4. **Estimated APR:** Is this reasonable (not a crazy number)?

When ready, click **"Create Position"** or **"Deposit."**

Your wallet will ask you to approve the transaction. The fee will be ~0.000005 SOL (a fraction of a cent). Confirm it.

## Step 8: You're an LP

Your position is live. You'll see it in your Meteora dashboard with:

- Current value of your position (in USD)
- Range (min-max prices)
- Unclaimed fees (these accumulate in real-time)
- Status: "In Range" (earning fees) or "Out of Range" (not earning)

## Step 9: What to Do Next

### Immediately:
- Bookmark your position URL or take a screenshot of the pool address
- Note the current SOL price — this is your reference point for measuring IL later

### First 24 hours:
- Check how much fees you've earned (even on a $50 position, you'll see fractions of a cent accumulating — that's real money from real trades)
- Observe whether your position stays in range

### First week:
- If the price approaches your range boundary, consider adjusting (widening or moving your range)
- Claim your fees if you want to see the yield compound (or leave them — they'll stay in the pool)

---

## Step 10: Managing Your Position

### How to Claim Fees

1. Go to your position
2. Click "Claim Fees" or find the fees section
3. Approve the transaction in your wallet
4. Fees are deposited to your wallet

### How to Adjust Your Range

1. Go to your position
2. Click "Edit" or "Adjust Position"
3. Drag the range sliders to your new desired range
4. Confirm the transaction

### How to Close Your Position

1. Go to your position
2. Click "Close Position" or "Withdraw"
3. You'll receive your share of the pool's current assets
4. IMPORTANT: The assets you receive will NOT be the same ratio as what you deposited. This is impermanent loss becoming permanent. Compare the value to what you would have had by just holding.

---

## The Most Important Habit

Every time you close a position, do this calculation:

```
What I received from closing:    X SOL + Y USDC = $Z
What I would have if I just held: Original SOL × current SOL price + Original USDC = $W

If Z > W: you profited (fees exceeded IL)
If Z < W: you lost (IL exceeded fees)
If Z = W: you broke even on the position, kept the learning
```

This single habit — comparing your actual result to the "just hold" baseline — is what separates profitable LPs from those who lose money without understanding why.

---

*Next: How do you track performance over time? What tools help? When do you know it's time to exit?*
