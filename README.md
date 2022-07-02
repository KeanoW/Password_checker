# Password_checker
This program checks to see if your password have been leaked via the haveibeenpwned api. The api uses a a k-Anonymity model that allows a password to be searched for by a
partial hash. In order to parse the password given to the api it must first be hashed with the SHA1 hashing algorithm and it accepts the first five chars of the hash. The
api returns the suffix of the hashes that start with the five char prefix.
