This directory contains the patch file for the downstream to Firefox 96.0.1 and includes all commits between both release versions

used command:

````
git format-patch -R 713683b^...c134791 --stdout > downstream-commit.patch
or
git format-patch -R 713683b^...c134791
````

Note: see the commit SHAs from 96.0.1 and 96.0.3
 
