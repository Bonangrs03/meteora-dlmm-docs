# Chapter 14: Monitoring, Exiting, and Measuring Profit

---

## The LP Lifecycle

LPing isn't "deposit and forget." It's a cycle:

```
DEPOSIT → MONITOR → DECIDE → (ADJUST or EXIT) → EVALUATE → DEPOSIT AGAIN
```

This chapter covers the middle three steps: monitor, decide, act.

## Monitoring: What to Watch

### Daily Check (30 seconds)

Open your position. Ask three questions:

1. **Is my position in range?** If yes → earning fees. If no → not earning. Simple.
2. **How close is the price to my range boundary?** If approaching, you need to decide soon.
3. **How much fees have I earned today?** Compare to position value. 0.1% daily = 36% annualized (if sustained).

### Weekly Review (5 minutes)

| Metric | What to Check | Why |
|--------|--------------|-----|
| **Position PnL** | Current value vs "just hold" value | Your true profit/loss |
| **Fee APR** | Fees earned this week ÷ position value × 52 | Is the yield sustainable? |
| **Price trend** | Is the pair trending strongly in one direction? | Might need to adjust strategy |
| **Volume trend** | Is trading volume rising or falling? | Rising = more fees ahead. Falling = maybe exit. |
| **IL magnitude** | What would you have if you just held? | Don't fool yourself about profitability |

### Tools That Help

| Tool | What It Does | URL |
|------|-------------|-----|
| **Meteora dApp** | Your position dashboard — the source of truth | app.meteora.ag |
| **Birdeye** | Token price charts, volume, analytics | birdeye.so |
| **DEX Screener** | Real-time DEX data, trending pairs | dexscreener.com |
| **Jupiter** | Best swap prices, routing data | jup.ag |
| **Rugcheck** | Token contract safety verification | rugcheck.xyz |
| **GMGN** | Memecoin tracking, wallet analysis | gmgn.ai |

For a simple LP on a major pair like SOL-USDC, the Meteora dApp + occasional Birdeye check is sufficient.

---

## The Decision: When to Act

### Scenario 1: Price Approaching Your Upper Bound

```
Your range: $180–$220
Current price: $215 (97.7% of range, approaching top)
```

**Options:**

| Action | When to Take It |
|--------|----------------|
| **Do nothing** | You believe price will stay in range or return |
| **Widen range upward** | You want to stay in range and keep earning fees |
| **Move range upward** | You believe the price has found a new level |
| **Close position** | You think the trend will continue strongly and IL will worsen |

**If you do nothing and price goes above $220:**
- Your position goes "out of range"
- All your assets are now in USDC (you effectively sold all your SOL at the top of your range)
- You earn zero fees until price comes back down
- Your downside is protected (you're in stablecoins)

### Scenario 2: Price Approaching Your Lower Bound

```
Your range: $180–$220
Current price: $185 (barely in range, approaching bottom)
```

| Action | When to Take It |
|--------|----------------|
| **Do nothing** | You believe in the asset long-term, willing to accumulate |
| **Widen range downward** | You want to stay active and keep earning |
| **Close position** | You think the downtrend will continue and you want to cut losses |

**If you do nothing and price drops below $180:**
- Position goes out of range
- All assets convert to SOL (you bought more SOL at declining prices)
- You're now 100% exposed to SOL's price movement
- You earn no fees

### Scenario 3: Position Deeply Out of Range

```
You opened at $200, range ±10%
Price is now $280 (40% above your max)
You've been out of range for 2 weeks
```

You have three choices:

1. **Wait.** If you believe price will return, your position reactivates automatically when it does. No transaction needed.
2. **Close and reopen.** Withdraw, accept the IL, and open a new position at the current price level. This crystallizes your loss but gets you earning fees again.
3. **Adjust existing position.** Widen or move your range to cover current price. Your position reactivates immediately.

---

## When to Exit: The Red Flags

### Hard Exits (Close Immediately)

- **The token is rugging.** Sudden 90%+ drop, liquidity disappearing, team wallets dumping. Don't wait. Close.
- **Pool is abandoned.** Volume dropped to near zero, no trades for days. Your capital is doing nothing.
- **You need the money.** LP funds should be "capital you don't need soon." If life happens, exit.

### Soft Exits (Consider Closing)

- **Fee APR dropped below 5% annualized** for more than a month. You could earn more in a savings account with zero risk.
- **IL has been growing for weeks and shows no sign of reversing.** The trend is your friend until it isn't.
- **You've found a better opportunity.** Capital should flow to its highest risk-adjusted return.
- **The pool's total volume is declining month over month.** Interest is fading.

---

## Measuring True Profit

This is the most important skill in LPing, and most people don't do it.

### The Framework

Track these numbers for every position:

| Metric | How to Calculate |
|--------|-----------------|
| **Gross deposit value** | Value of tokens you put in (at deposit-time prices) |
| **Fees earned** | Accumulated fees from the position dashboard |
| **Current withdrawal value** | Value of tokens you'd receive if you closed right now |
| **HODL value** | Value if you'd just held the original tokens |

### The Only Two Numbers That Matter

```
LP Profit = Current Withdrawal Value - Gross Deposit Value

vs

HODL Profit = HODL Value - Gross Deposit Value
```

- If LP Profit > HODL Profit → you won. LPing added value.
- If LP Profit < HODL Profit → you would have been better off not LPing.
- If LP Profit is negative → you lost money in absolute terms.

### A Realistic Example

```
Deposited: 0.5 SOL ($100 when SOL = $200) + 100 USDC = $200 total

After 3 months:
- SOL is now $300 (+50%)
- Position contains: 0.38 SOL + 115 USDC
- Current withdrawal value: 0.38 × $300 + 115 = $229
- HODL value: 0.5 × $300 + 100 = $250

LP Profit: $229 - $200 = +$29 (+14.5% in 3 months)
HODL Profit: $250 - $200 = +$50 (+25% in 3 months)

Verdict: LPing underperformed holding. The IL from SOL's 50% rise cost more than the fees earned.
```

This doesn't mean LPing was a "failure." It means: in a strongly trending market, concentrated LP strategies underperform simply holding the appreciating asset. Knowing this helps you choose strategies appropriate for market conditions.

---

## The Monthly LP Health Check

Once a month, ask yourself:

1. **Am I tracking my PnL honestly?** (HODL comparison, not just "fees look good")
2. **Is my strategy still appropriate for current market conditions?**
3. **Am I checking my positions at the right frequency?** (Too little = caught off guard. Too much = overtrading.)
4. **Are the fees I'm earning worth the time I'm spending?**
5. **Do I understand WHY my position performed the way it did?**

Question #5 is the most important. A profitable position you don't understand is more dangerous than an unprofitable one you do understand — because the profitable one gives you false confidence.

---

## The Next Step After This Document

You've completed the story. From Budi at the bus terminal to your first DLMM position on Solana.

Where to go from here:

1. **Open a tiny test position** ($20-50). Experience the full lifecycle.
2. **Join the LP Army community** (lparmy.com) — the Meteora LP Discord where active LPs share strategies.
3. **Read the official docs** (docs.meteora.ag) — now that you have the conceptual foundation, the technical docs will make sense.
4. **Track your positions honestly** — the HODL comparison, every time.
5. **Scale up gradually** — as you develop intuition, not before.

---

## One Final Concept to Take Away

There are no get-rich-quick strategies in LPing. There are only **risk-adjusted returns.** The question isn't "how much can I earn?" — it's "how much risk am I taking to earn that?"

If someone shows you a screenshot of 1000% APR, ask: *"What was the impermanent loss? What's the HODL comparison? Is this sustainable or was this one good day in a month of losses?"*

The ones making real money in DeFi aren't chasing the highest numbers. They're tracking their PnL honestly, understanding their risks, and compounding steadily over time.

Just like Budi at the bus terminal — showing up every day, managing inventory, earning the spread. No magic. Just math and consistency.

---

**Good luck. Start small. Track honestly. Stay curious.**
