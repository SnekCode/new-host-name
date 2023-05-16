# new-host-name

## Target
To rename files based on content within.  Currently targets the value of `new_host_name="blah"`.  Could be expanded in the future to accept and argument to define this.

## Usage
`py rename.py *.txt`

## Examples
given a file `bat1.txt`
```txt
some garbage text
to see if the = sed / regex functions
new_host_name="213-east"
work
properly=or not
```

after running the command `py rename.py *.txt`

`bat1.txt` will be renamed `213-east.txt`
