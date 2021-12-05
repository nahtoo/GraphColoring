#!bin/bash

echo "Plain"

for i in {0..9}
do
python dfsb.py 50_4_625_Tests/$i plaindsfb/50_4_625_Tests$i 0
done

echo "\nMin-conflict"

for i in {0..9}
do
python minconflicts.py 50_4_625_Tests/$i minconflict/50_4_625_Tests$i
done

echo "\nImproved"

for i in {0..9}
do
python dfsb.py 50_4_625_Tests/$i improveddfsb/50_4_625_Tests$i 1
done


exit 0