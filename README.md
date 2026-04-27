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
