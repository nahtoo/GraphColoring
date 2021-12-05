echo "Plain"

for i in {0..9}
do
python dfsb.py 200_4_10000_Tests/$i plaindsfb/200_4_10000_Tests$i 0
done

echo "\nMin-conflict"

for i in {0..9}
do
python minconflicts.py 200_4_10000_Tests/$i minconflict/200_4_10000_Tests$i
done

echo "\nImproved"

for i in {0..9}
do
python dfsb.py 200_4_10000_Tests/$i improveddfsb/200_4_10000_Tests$i 1
done


exit 0