import re
test = [3,2,1]

def num_to_string(num):
  string = ".*"
  for n in num:
    string += "(#{"+str(n)+"})"
  string += ".*"
  return string

# ?###???????? 3,2,1
var1 = ".###.##.#..."
var2 = ".###.##..#.."
var3 = ".###.##...#."
var4 = ".###.##....#"
var5 = ".###..##.#.."
var6 = ".###..##..#."
var7 = ".###..##...#"
var8 = ".###...##.#."
var9 = ".###...##..#"
var10 = ".###....##.#"

re.match(re.escape(num_to_string(test)), var1	)