# CVE-2018-4121 - Safari Wasm Sections POC RCE Exploit

by MWR Labs (c) 2018 

## Details

* this proof of concept exploit targets Safari 11.0.3 (13604.5.6) on macOS 10.13.3 (17D47) versions only.
* compile the payload of your choice as a dylib with a constructor
* run `python file_to_jsarray.py your.dylib payload.js`
* serve this directory and point Safari to /exploit.html 
* exploit is not fully reliable and uses hardcoded offsets for this macOS/Safari version. 
* exploit takes a while to run due to the size of the heap spray (24.5GB). 
* this issue is addressed in macOS 10.13.4 as CVE-2018-4121 (https://support.apple.com/en-gb/HT208692)

## Credits

* Natalie Silvanovich of Google Project Zero - https://bugs.chromium.org/p/project-zero/issues/detail?id=1522
* Ian Beer of Google Project Zero - https://googleprojectzero.blogspot.co.uk/2014/07/pwn4fun-spring-2014-safari-part-i_24.html 
* Phoenhex - https://phoenhex.re/
* Fermin Serna - https://media.blackhat.com/bh-us-12/Briefings/Serna/BH_US_12_Serna_Leak_Era_Slides.pdf 

## References

* https://labs.mwrinfosecurity.com/assets/BlogFiles/apple-safari-wasm-section-vuln-write-up-2018-04-16.pdf
* https://labs.mwrinfosecurity.com/mwr-vulnerability-disclosure-policy
* https://www.mwrinfosecurity.com/about-us/
