echo "Plain"

for i in {0..9}
do
python dfsb.py 400_4_40000_Tests/$i plaindsfb/400_4_40000_Tests$i 0
done

echo "\nMin-conflict"

for i in {0..9}
do
python minconflicts.py 400_4_40000_Tests/$i minconflict/400_4_40000_Tests$i
done

echo "\nImproved"

for i in {0..9}
do
python dfsb.py 400_4_40000_Tests/$i improveddfsb/400_4_40000_Tests$i 1
done


exit 0