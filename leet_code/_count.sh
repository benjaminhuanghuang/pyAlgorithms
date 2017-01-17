count=1
#for py in *.py
#for py in `find . -name "*.py"`
for py in `find . -regextype './[0-9]*.py'`

do
    echo $py
    let count=count+1
done

echo $count