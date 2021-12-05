Python program  solve  the  graph  coloring  problem  using  Depth  first  withbacktracking and Min-Conflicts Local Search.

## To generate random graph coloring problem

`python CSPGenerator.py<N> <M> <K> <outputfilepath> 0`

## <span>dfsb.py</span>
Module runs in two  modes.   
1. Plain  DFS-B  and  
2. DFS-B with variable, value ordering + AC3 for constraint propagation.

A sample execution of <span>dfsb.py</span> should be as below:

`python dfsb.py</span><INPUTFILE> <OUTPUTFILE><MODEFLAG>` . `<MODEFLAG>` can be either 0 (plain DFS-B) or 1 (improved DFS-B).

## <span>minconflicts.py</span>

`python minconflicts.py<INPUTFILE> <OUTPUTFILE>`

