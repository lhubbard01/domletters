#!/usr/bin/python3
import string
import sys
from functools import reduce

def dominant(X: str, verbose: bool = False):
    """returns the sum of all dominant characters, i.e. on a per-word basis, summed
    Args: 
      @X - the candidate string
      @verbose - display encountered valid substrings

    @returns: the sum of all dominant characters, running_sum: int
    """

    sb = "" # encountered letters for dict tallying at valid break character, string build

    idx           = 0
    
    invalid_flag  = 0 #if an encountered character breaks the candidate substrings validity, is flipped and indicates to not include in dominant string tally
    running_sum   = 0
    
    mp={k:0 for k in string.ascii_letters.lower()} #per character tally, map
    while idx < len(X):
        if X[idx] in string.ascii_letters: # case : character is a valid candidate for tally regardless of flag
          sb+=X[idx]
        elif X[idx] in "\n ":                # case : break character to potential;y initiate tally
            if not invalid_flag: # is valid substring for dominant character tally
              if verbose:
                print(sb)

              for letter in sb.lower():
                mp[letter]+=1 
              running_sum+=max(mp.items(), key=lambda k: k[1])[1] #maximum value acording to custom ordinal definition\

            sb, invalid_flag = "", 0 # reset string and valid flag for next candidate when space is encountered
            mp={k:0 for k in string.ascii_letters.lower()}

        else:                              # case : invalid character encountered for dominant, set invalid
          sb, invalid_flag = X[idx],1
        idx += 1                           
    if not invalid_flag:
      for letter in sb.lower():
        mp[letter]+=1 

      if verbose:
        print(sb)
    return running_sum






print(dominant(reduce(str.__add__, sys.stdin.readlines(), "")))  # reduce the lines separated from list elements,
#captured from stdin on a per newline character basis, into a single string for processing, and return to stdout.
