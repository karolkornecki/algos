from functools import cache
from typing import List


# top down
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True
            for word in wordDict:
                if i >= len(word) - 1 and is_word_end_here(s, word, i) and dp(i - len(word)):
                    return True
            return False

        return dp(len(s) - 1)

# bottom up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if i >= len(word) - 1 and is_word_end_here(s, word, i):
                    if i - len(word) >= 0:
                        if dp[i - len(word)]:
                            dp[i] = True
                    else:
                        dp[i] = True
        return dp[len(s) - 1]


def is_word_end_here(s, word, i):
    return s[i - len(word) + 1:i + 1] == word


if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"])
    assert s.wordBreak("applepenapple", ["apple", "pen"])
    assert not s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert s.wordBreak("fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami",
                       ["kfomka", "hecagbngambii", "anobmnikj", "c", "nnkmfelneemfgcl", "ah", "bgomgohl", "lcbjbg",
                        "ebjfoiddndih",
                        "hjknoamjbfhckb", "eioldlijmmla", "nbekmcnakif", "fgahmihodolmhbi", "gnjfe", "hk", "b", "jbfgm",
                        "ecojceoaejkkoed", "cemodhmbcmgl", "j", "gdcnjj", "kolaijoicbc", "liibjjcini", "lmbenj",
                        "eklingemgdjncaa",
                        "m", "hkh", "fblb", "fk", "nnfkfanaga", "eldjml", "iejn", "gbmjfdooeeko", "jafogijka",
                        "ngnfggojmhclkjd",
                        "bfagnfclg", "imkeobcdidiifbm", "ogeo", "gicjog", "cjnibenelm", "ogoloc", "edciifkaff", "kbeeg",
                        "nebn", "jdd",
                        "aeojhclmdn", "dilbhl", "dkk", "bgmck", "ohgkefkadonafg", "labem", "fheoglj", "gkcanacfjfhogjc",
                        "eglkcddd",
                        "lelelihakeh", "hhjijfiodfi", "enehbibnhfjd", "gkm", "ggj", "ag", "hhhjogk", "lllicdhihn",
                        "goakjjnk", "lhbn",
                        "fhheedadamlnedh", "bin", "cl", "ggjljjjf", "fdcdaobhlhgj", "nijlf", "i", "gaemagobjfc", "dg",
                        "g",
                        "jhlelodgeekj", "hcimohlni", "fdoiohikhacgb", "k", "doiaigclm", "bdfaoncbhfkdbjd", "f",
                        "jaikbciac",
                        "cjgadmfoodmba", "molokllh", "gfkngeebnggo", "lahd", "n", "ehfngoc", "lejfcee", "kofhmoh",
                        "cgda", "de",
                        "kljnicikjeh", "edomdbibhif", "jehdkgmmofihdi", "hifcjkloebel", "gcghgbemjege", "kobhhefbbb",
                        "aaikgaolhllhlm",
                        "akg", "kmmikgkhnn", "dnamfhaf", "mjhj", "ifadcgmgjaa", "acnjehgkflgkd", "bjj", "maihjn",
                        "ojakklhl", "ign",
                        "jhd", "kndkhbebgh", "amljjfeahcdlfdg", "fnboolobch", "gcclgcoaojc", "kfokbbkllmcd", "fec",
                        "dljma", "noa",
                        "cfjie", "fohhemkka", "bfaldajf", "nbk", "kmbnjoalnhki", "ccieabbnlhbjmj", "nmacelialookal",
                        "hdlefnbmgklo",
                        "bfbblofk", "doohocnadd", "klmed", "e", "hkkcmbljlojkghm", "jjiadlgf", "ogadjhambjikce",
                        "bglghjndlk",
                        "gackokkbhj", "oofohdogb", "leiolllnjj", "edekdnibja", "gjhglilocif", "ccfnfjalchc", "gl",
                        "ihee",
                        "cfgccdmecem", "mdmcdgjelhgk", "laboglchdhbk", "ajmiim", "cebhalkngloae", "hgohednmkahdi",
                        "ddiecjnkmgbbei",
                        "ajaengmcdlbk", "kgg", "ndchkjdn", "heklaamafiomea", "ehg", "imelcifnhkae", "hcgadilb",
                        "elndjcodnhcc", "nkjd",
                        "gjnfkogkjeobo", "eolega", "lm", "jddfkfbbbhia", "cddmfeckheeo", "bfnmaalmjdb", "fbcg", "ko",
                        "mojfj", "kk",
                        "bbljjnnikdhg", "l", "calbc", "mkekn", "ejlhdk", "hkebdiebecf", "emhelbbda", "mlba", "ckjmih",
                        "odfacclfl",
                        "lgfjjbgookmnoe", "begnkogf", "gakojeblk", "bfflcmdko", "cfdclljcg", "ho", "fo", "acmi",
                        "oemknmffgcio",
                        "mlkhk", "kfhkndmdojhidg", "ckfcibmnikn", "dgoecamdliaeeoa", "ocealkbbec", "kbmmihb", "ncikad",
                        "hi",
                        "nccjbnldneijc", "hgiccigeehmdl", "dlfmjhmioa", "kmff", "gfhkd", "okiamg", "ekdbamm", "fc",
                        "neg", "cfmo",
                        "ccgahikbbl", "khhoc", "elbg", "cbghbacjbfm", "jkagbmfgemjfg", "ijceidhhajmja", "imibemhdg",
                        "ja", "idkfd",
                        "ndogdkjjkf", "fhic", "ooajkki", "fdnjhh", "ba", "jdlnidngkfffbmi", "jddjfnnjoidcnm",
                        "kghljjikbacd",
                        "idllbbn", "d", "mgkajbnjedeiee", "fbllleanknmoomb", "lom", "kofjmmjm", "mcdlbglonin",
                        "gcnboanh", "fggii",
                        "fdkbmic", "bbiln", "cdjcjhonjgiagkb", "kooenbeoongcle", "cecnlfbaanckdkj", "fejlmog",
                        "fanekdneoaammb",
                        "maojbcegdamn", "bcmanmjdeabdo", "amloj", "adgoej", "jh", "fhf", "cogdljlgek", "o",
                        "joeiajlioggj", "oncal",
                        "lbgg", "elainnbffk", "hbdi", "femcanllndoh", "ke", "hmib", "nagfahhljh", "ibifdlfeechcbal",
                        "knec",
                        "oegfcghlgalcnno", "abiefmjldmln", "mlfglgni", "jkofhjeb", "ifjbneblfldjel", "nahhcimkjhjgb",
                        "cdgkbn",
                        "nnklfbeecgedie", "gmllmjbodhgllc", "hogollongjo", "fmoinacebll", "fkngbganmh", "jgdblmhlmfij",
                        "fkkdjknahamcfb", "aieakdokibj", "hddlcdiailhd", "iajhmg", "jenocgo", "embdib", "dghbmljjogka",
                        "bahcggjgmlf",
                        "fb", "jldkcfom", "mfi", "kdkke", "odhbl", "jin", "kcjmkggcmnami", "kofig", "bid", "ohnohi",
                        "fcbojdgoaoa",
                        "dj", "ifkbmbod", "dhdedohlghk", "nmkeakohicfdjf", "ahbifnnoaldgbj", "egldeibiinoac",
                        "iehfhjjjmil", "bmeimi",
                        "ombngooicknel", "lfdkngobmik", "ifjcjkfnmgjcnmi", "fmf", "aoeaa", "an", "ffgddcjblehhggo",
                        "hijfdcchdilcl",
                        "hacbaamkhblnkk", "najefebghcbkjfl", "hcnnlogjfmmjcma", "njgcogemlnohl", "ihejh", "ej", "ofn",
                        "ggcklj",
                        "omah", "hg", "obk", "giig", "cklna", "lihaiollfnem", "ionlnlhjckf", "cfdlijnmgjoebl",
                        "dloehimen",
                        "acggkacahfhkdne", "iecd", "gn", "odgbnalk", "ahfhcd", "dghlag", "bchfe", "dldblmnbifnmlo",
                        "cffhbijal",
                        "dbddifnojfibha", "mhh", "cjjol", "fed", "bhcnf", "ciiibbedklnnk", "ikniooicmm", "ejf",
                        "ammeennkcdgbjco",
                        "jmhmd", "cek", "bjbhcmda", "kfjmhbf", "chjmmnea", "ifccifn", "naedmco", "iohchafbega",
                        "kjejfhbco",
                        "anlhhhhg"])
