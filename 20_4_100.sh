#!bin/bash

for i in {0..9}
do
python minconflicts.py 20_4_100_Tests/$i minconflict/20_4_100_Tests$i
# python dfsb.py 20_4_100_Tests/$i improveddfsb/20_4_100_Tests$i 1
done

exit 0