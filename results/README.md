# Tested Results

This folder contains tested outputs from the MasRouter Research Implementation.

## Test Case 1: Prime Number Function

### Query

```text
Write a Python function to check prime number
```

### Routing Plan

```text
Task Type: coding
Collaboration Mode: Chain
Agents: Programmer, Tester, Verifier
LLM Used: gemini/gemini-2.5-flash
```

### Observed Workflow

```text
User Query -> MasRouter Plan -> Programmer Agent -> Tester Agent -> Verifier Agent -> Final Answer
```

### Result Summary

- The Programmer generated the Python solution.
- The Tester reviewed correctness and edge cases.
- The Verifier produced the final clean answer.
- The final output contained a working prime number checking function.

### Full Output

```text
results/sample_prime_test_output.txt
```

## Status

Working MVP tested successfully.

## Test Case 2: Average Speed Math Problem

### Query

```text
Solve this math problem: If a car travels 120 km in 3 hours, what is its average speed?
```

### Expected Routing

```text
Task Type: math
Collaboration Mode: Chain + Verification
Agents: Math Analyst, Calculator, Verifier
LLM Used: gemini/gemini-2.5-flash
```

### Observed Workflow

```text
User Query -> MasRouter Plan -> Math Analyst Agent -> Calculator Agent -> Verifier Agent -> Final Answer
```

### Full Output

```text
results/sample_math_test_output.txt
```

### Status

Second test completed successfully.

## Test Case 3: Research Summarization Query

### Query

```text
Summarize the abstract and methodology of a research paper about LLM routing in simple terms
```

### Expected Routing

```text
Task Type: research
Collaboration Mode: Research-Analysis-Summary
Agents: Researcher, Analyst, Summarizer
LLM Used: gemini/gemini-2.5-flash
```

### Observed Workflow

```text
User Query -> MasRouter Plan -> Researcher Agent -> Analyst Agent -> Summarizer Agent -> Final Answer
```

### Full Output

```text
results/sample_research_test_output.txt
```

### Status

Third test completed successfully.
