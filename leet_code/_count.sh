count=1
#for py in *.py
#for py in `find . -name "*.py"`
#for py in `find . -regex './[0-9]*.py'`
for py in `ls ./[0-9]*.py`

do
    echo $py
    let count=count+1
done

echo $count