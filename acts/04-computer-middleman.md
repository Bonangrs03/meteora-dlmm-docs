# Chapter 4: What If the Middleman Was a Computer Program?

---

## Budi Has a Problem

Remember Budi from Chapter 3? He's doing well. But he's exhausted. Standing at the bus terminal 14 hours a day. He has to be physically present for every single trade.

One night, Budi has an idea: *"What if I wrote a computer program that does my job?"*

He calls his nephew, a programmer.

"Listen," Budi says. "I need a program that replaces me. It needs to do exactly three things:"

1. **Hold inventory** — the program should hold both pulsa and cash, like I do.
2. **Set prices** — the program needs to know what price to buy and sell at.
3. **Execute trades** — when someone wants to trade, the program does it automatically.

The nephew thinks for a moment. "The first and third are easy. The hard part is #2 — how does the program know what price to set?"

## The One Rule the Program Needs

Budi explains his instinct: *"When lots of people buy from me, I slowly raise my price. When lots of people sell to me, I slowly lower my price. I don't think about it — I just feel the crowd."*

The nephew translates this into code logic:

```
If someone BUYS from the program:
    → The program's inventory of the asset goes DOWN
    → So the program should RAISE the price slightly

If someone SELLS to the program:
    → The program's inventory of the asset goes UP
    → So the program should LOWER the price slightly
```

This is intuitive. If everyone wants to buy pulsa from the machine, pulsa becomes scarcer inside the machine. Higher price. If everyone is selling pulsa to the machine, the machine is flooded with pulsa. Lower price.

**This is exactly how real financial markets work.** Apple stock goes up when more people want to buy than sell. It goes down when more people want to sell than buy. The machine just formalizes this into code.

## The Automated Market Maker (AMM)

This program — a robot that holds inventory, sets prices algorithmically, and trades automatically — is called an **Automated Market Maker,** or **AMM.**

> **AMM** = a computer program that acts as a market maker, using math (not human judgment) to set prices.

Instead of Budi standing at the terminal making gut-feel decisions, we have a program running 24/7, processing trades instantly, never getting tired, never making emotional mistakes.

## The Key Difference: Who Sets the Price?

| Traditional Market (Stock Exchange) | Automated Market Maker (DeFi) |
|-------------------------------------|-------------------------------|
| Buyers and sellers place orders | No orders. Just a pool of assets. |
| An order book matches them | A formula calculates the price. |
| Price = where supply meets demand | Price = what the formula says, based on how much is in the pool. |
| Needs lots of participants to work | Works with just ONE provider of assets. |

This last point is revolutionary. A traditional exchange needs lots of buyers AND lots of sellers to function. Without enough participants, the order book is empty and trading stalls.

An AMM works with just one person depositing assets. The formula handles price discovery. This means **you can create a functioning market for any asset, at any time, with almost no setup.**

## The Tradeoff

Of course, Budi-the-human had advantages:

| Budi (Human) | AMM (Program) |
|--------------|---------------|
| Can adjust to news and events | Only follows its formula |
| Can refuse a suspicious trade | Trades with anyone, always |
| Gets tired, needs sleep | Runs forever |
| Makes gut-feel mistakes | Makes zero judgment errors |
| Can't scale beyond one location | Can serve the entire internet |

For crypto, which is global, 24/7, and purely digital, the AMM model is a natural fit. No sleep. No borders. No sick days.

## Where We Are Now

So far, we've built:

```
Chapter 1: Liquidity = ease of trading
Chapter 2: Market makers provide liquidity, profit from spread
Chapter 3: Profit = spread × volume − inventory risk
Chapter 4: An AMM is a computer program that does a market maker's job
```

The AMM is the bridge between Budi's bus terminal and the world of DeFi. But we still haven't answered the central question:

**What formula does the AMM actually use to set prices?**

That's Chapter 5.

---

*Next: The math inside the machine. Don't worry — it's simpler than you think.*
