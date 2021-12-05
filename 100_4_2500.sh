echo "Plain"

for i in {0..9}
do
python dfsb.py 100_4_2500_Tests/$i plaindsfb/100_4_2500_Tests$i 0
done

echo "\nMin-conflict"

for i in {0..9}
do
python minconflicts.py 100_4_2500_Tests/$i minconflict/100_4_2500_Tests$i
done

echo "\nImproved"

for i in {0..9}
do
python dfsb.py 100_4_2500_Tests/$i improveddfsb/100_4_2500_Tests$i 1
done


exit 0