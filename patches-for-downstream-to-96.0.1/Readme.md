This directory contains the patch file for the downstream to Firefox 96.0.1 and includes all commits between both release versions

used command:

````
git format-patch -R 713683b^...c134791 --stdout > downstream-commit.patch
or
git format-patch -R 713683b^...c134791
````

Note: see the commit SHAs from 96.0.1 and 96.0.3



REVERT CHANGES (33 Commits) FROM 96.0.3 to 96.0.1 in timolasi/project-foxhound:
On branch downstream-merge-96.0.1
Your branch is up to date with 'origin/downstream-merge-96.0.1'.

nothing to commit, working tree clean
$ git revert -^C
$ git format-patch -R 713683b^...c134791^C
$ git revert --help
$ git revert --no-edit -n -s 713683b4a6b03aba9e6bd80d65a8e13c462f071a
$ git revert --no-edit -n -s c539b624258f64a86e8d2c0a29287166e630aa8c
Removing services/settings/dumps/main/search-telemetry-v2.json
Removing browser/components/search/test/unit/test_urlTelemetry_generic.js
$ git revert --no-edit -n -s 723f2b3dd4f885827602e56f3e79e7aaabe52421
$ git revert --no-edit -n -s 8794c7425eba8920c91a508aa65db0d390490941
$ git revert --no-edit -n -s d8d2ad7a4ad9dc95c86d5ebd193fbeff67ca7d9e
$ git revert --no-edit -n -s 372ac6b4a53e7df7100f0da099e2d2d2a133c347
$ git revert --no-edit -n -s 90b5653d389b36f6ce1bee720a76fb09ab75e3c6
$ git revert --no-edit -n -s eee931c88856fae8feb84ece12b7419d5112973b
$ git revert --no-edit -n -s 11053e4be8b7f1881c99245eea52c69221c7d2cc
$ git revert --no-edit -n -s bc9e79597151469a500a191434e81f2624629b85
Removing testing/web-platform/meta/cookies/schemeful-same-site/schemeful-websockets.sub.tentative.html.ini
Removing testing/web-platform/meta/cookies/schemeful-same-site/schemeful-subresource.tentative.html.ini
$ git revert --no-edit -n -s 4dad6e6f9ff2bb22c7bee9b5d18feac293cf4eba
$ git revert --no-edit -n -s a785496c613d35e335479781de19644b727317b5
$ git revert --no-edit -n -s 354b475d2845b2a0acf55ac6b19e5e9974bca5a4
$ git revert --no-edit -n -s 89c5488ab6eff5536eb1a835665894720741bd2a
$ git revert --no-edit -n -s 6ed9a7e211e65371aed0c5b759d4378fef57d60c
Auto-merging modules/libpref/init/StaticPrefList.yaml
$ git revert --no-edit -n -s 2b268a5aa4b4fe8f4ef555e2c3178bf0e7694d29
$ git revert --no-edit -n -s 05351a1fb61deac918656809ec5a52b7d2ebf217
$ git revert --no-edit -n -s a6f506346a54345333369432db9ff1dc0deb8507
$ git revert --no-edit -n -s 9e842ec685a501ffe630d90acfccfd33662db7a9
$ git revert --no-edit -n -s bfc5e35cc94ec79746097951527a63cd9a189af4
$ git revert --no-edit -n -s 7054d7b3b98eadb62d3e4ffe399ccfb93ac4fe4c
$ git revert --no-edit -n -s b054c28649f5c03d539b0dd508ef8ad5e3d81958
Removing browser/components/urlbar/tests/browser/browser_searchMode_newWindow.js
$ git revert --no-edit -n -s d2f7af809f5f9e9724de682537870511c8e7fa98
$ git revert --no-edit -n -s e0b72b794fc7c01b448c751ba6c605295309f27b
$ git revert --no-edit -n -s 5a4bd2a35d3d0dd021948f6ce6569c7144915ad2
$ git revert --no-edit -n -s c91e878a3b82363722b8f0018a8300f6fec8ad4b
$ git revert --no-edit -n -s c6faa95054a0f309f2b15fa3c1be2a9c203311a9
$ git revert --no-edit -n -s df422c169ae41f44cb2a5df6534073a5830d7df6
$ git revert --no-edit -n -s dcceeea907faffe2bc1a6ee272f7532ac4fe18a2
Removing browser/components/urlbar/content/quicksuggestOnboarding_magglass_animation.svg
Removing browser/components/urlbar/content/quicksuggestOnboarding_magglass.svg
Removing browser/components/urlbar/content/quicksuggestOnboarding.html
$ git revert --no-edit -n -s 7ef1f0e80025adf8b0b825c4698a3847adb1966e
$ git revert --no-edit -n -s 8faefe680cd30db5c1ea9652d314fff3dda26b15
$ git revert --no-edit -n -s 0669f3eca7b1b37bb6190e97389e280df7d7ca0a
$ git revert --no-edit -n -s 136cd85c3504630133d8f9cad673647f2e42b33b
