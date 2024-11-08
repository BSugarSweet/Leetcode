class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        substring = ""
        symbols = "!?',;."
        dic = defaultdict(int)

        for i in paragraph:
            if i in symbols or i == " ":
                if substring and substring not in banned:
                    dic[substring] += 1
                substring = ""
                continue
            substring += i
        if substring and substring not in banned:
            dic[substring] += 1
        return max(dic, key = dic.get)


        