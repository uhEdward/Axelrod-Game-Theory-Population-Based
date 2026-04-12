# Population-Based Axelrod Simulation

## **TLDR**

This project is an extention of Axelrod's research on a variant of the prisoner's dilmma. Axelrod used a scheme whereby he paired agents for 200 consecutive game. In my environment, I placed agents in a pool, randomly assigning them partners every game, forming an artifical "society" of agents and interactions. 

---

## **Background**

Robert Axelrod is an American political scientist renowned for his work on the evolution of cooperation. His original experiment involved 14 strategies, where each strategy was assigned to a single agent. These agents competed in a round-robin tournament, meaning every strategy played against every other strategy, including itself.

### The Game

Each interaction between two agents consisted of 200 consecutive rounds of a repeated prisoner’s dilemma (similar to split-or-steal):

- If both agents cooperate → each receives **3 points**
- If one defects and the other cooperates → defector gets **5 points**, cooperator gets **0**
- If both defect → each receives **1 point**

### One-Shot vs Repeated Games

In a single-round game, the dominant strategy is to defect. No matter what the opponent does, defecting yields a higher payoff. This outcome is known as the **Nash equilibrium**.

However, when the game is repeated many times, the incentives change:

- If both agents cooperate every round → **600 points each (3 × 200)**
- If both defect every round → **200 points each (1 × 200)**

This creates a strong incentive for sustained cooperation.

### Emergence of Cooperation

Axelrod’s results showed that the highest-performing strategies shared two key characteristics:

- **Nice**: they never defect first  
- **Forgiving**: they retaliate, but not indefinitely   

### Tit-for-Tat

The most successful strategy in Axelrod’s tournament was **Tit-for-Tat**.

It works as follows:

- Starts by cooperating → **nice**
- Then mimics the opponent’s previous move 
- Returns to cooperation immediately after → **forgiving**

---

## Research Question

This project extends Axelrod’s original framework by asking:

**What happens when we simulate a society of agents, rather than fixed pairwise interactions?**

In particular, we study how cooperation evolves as we vary:

- **Population size**: Instead of a single instance of each strategy, multiple agents per strategy interact within a shared population. This allows for more realistic dynamics where strategies coexist and compete at scale.

- **Information structure**: Agents may have access to different levels of information. In the local setting, agents only observe their own past interactions with a specific opponent. In the global setting, agents can also observe how their opponents behave with others.

Together, these extensions transform the model from isolated repeated games into a dynamic social system, allowing us to study how cooperation emerges under different societal conditions. 

---

## Baseline Experiments

To validate the framework, we begin with a simple baseline configuration consisting of three canonical strategies:

- Always Cooperate  
- Always Defect  
- Tit-for-Tat  

The goal is to compare how these strategies perform under different interaction and information structures.

### 1. Axelrod Environment (Baseline)

This setting replicates the structure of Axelrod’s original tournament:

- Each strategy is represented by a single agent  
- All agents play against every other agent (including themselves)  
- Each pair plays a fixed number of repeated rounds (e.g. 200)  
- Final scores are aggregated across all pairwise interactions  

This serves as the reference point for all comparisons.

### 2. Population-Based Environment

We extend this setup by introducing a population-based simulation:

- Multiple agents are instantiated per strategy  
- At each step, two agents are randomly selected from the population  
- Agents interact with many different opponents over time  
- Total interactions are matched to the Axelrod setting for fairness  

This transforms the system from fixed pairwise interactions into a dynamic and stochastic environment.

### 3. Interaction Structures

### Interaction and Information Effects

To validate the correctness of the simulation framework, we begin by comparing it against the expected behavior of Axelrod’s original setting.

#### 1. Validation: Equivalent Interaction Structure (Local History)

We first replicate the Axelrod environment using the population-based model by:

- enforcing equal interaction counts between all pairs  
- using a **local history** (agents only observe direct past interactions)  

Although interactions are no longer consecutive (i.e. games are interleaved with others), this setup is equivalent to the original model because each pair still plays the same total number of rounds with no additional information.

**Result:**  
The outcomes match the original Axelrod tournament, with **Tit-for-Tat performing best**, followed by **Always Cooperate**, then **Always Defect**.

**Insight:**  
Reordering interactions does not affect results when agents rely only on local history. The model is therefore a valid extension of the original framework.


#### 2. Random Matching (Stochastic Pairing)

We then relax the interaction structure by sampling agent pairs randomly:

- pairs are drawn with replacement  
- interaction frequencies are no longer uniform  

The history model remains **local**.

**Result:**  
We again observe the same ranking:
- Tit-for-Tat performs best  
- Always Cooperate follows  
- Always Defect performs worst  

However, small variations appear across runs due to randomness.

**Insight:**  
The results are robust to stochastic pairing. While random sampling introduces noise, it does not fundamentally alter strategic outcomes under local information.

#### 3. Global Information (Reputation Effects)

Next, we extend the model by introducing a **global history**:

- agents can observe how their opponents behave with others  
- this effectively introduces a notion of **reputation**  

Interaction structure remains stochastic.

**Result:**  
The overall ranking remains consistent with the local-history case.

**Insight:**  
Access to global information does not significantly alter outcomes in this baseline setting. This suggests that, for these strategies, behavior is largely determined by direct interactions rather than reputation.

#### 4. Scaling the Population (k = 10)

Finally, we increase the population size:

- 10 agents per strategy  
- stochastic matching  
- same total number of interactions  

**Result:**  
The outcome changes significantly:  
**Always Defect emerges as the dominant strategy.**

**Insight:**  
Scaling the population alters the distribution of interactions. Even if theoretical pair proportions remain similar, the increased number of agents and stochastic matching introduce new dynamics that favor defection.

### Summary of Findings

- The model correctly reproduces Axelrod’s results under equivalent conditions  
- Results are robust to random pairing when using local information  
- Introducing global information does not significantly change outcomes in this baseline  
- Increasing population size fundamentally alters the system, leading to the dominance of Always Defect  

This suggests that extending the iterated prisoner’s dilemma to a population setting introduces non-trivial dynamics that are not present in the original two-agent framework.

---

## Code Structure
```
src/
├── agent.py # Agent representation
├── strategy.py # Strategy definitions
├── simulation.py # Simulation engine
├── match.py # Pair interactions
├── population.py # Agent container
├── horizon.py # Information models
├── experiment.py # Experiment runner
├── visualizer.py # Plotting results
```


---

## Usage

Run the simulation:

```bash
python main.py
