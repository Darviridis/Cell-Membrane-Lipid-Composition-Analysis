# Cell Membrane Lipid Composition Analysis

## Description
This project analyzes and visualizes the lipid composition of cell membranes
in three cell types: erythrocytes, neurons, and mitochondria.

## Data
Lipid percentages (mol%) based on van Meer et al., 2008 and Sastry, 1985.

| Lipid | Erythrocyte | Neuron | Mitochondria |
|-------|-------------|--------|--------------|
| PC    | 19%         | 30%    | 40%          |
| PE    | 18%         | 27%    | 35%          |
| SM    | 17%         | 8%     | 3%           |
| Cholesterol | 40%   | 22%    | 7%           |
| Other | 6%          | 13%    | 15%          |

## Results
![Erythrocyte composition](erythrocyte_membrane.png)
![Cell comparison](membrane_comparison.png)

## Requirements
- Python 3
- pandas
- matplotlib

## Usage
```bash
python membrane_analysis.py
```
