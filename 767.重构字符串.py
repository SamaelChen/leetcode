#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# %%
# @lc code=start
import collections
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        ch_dict = {}
        ch_list = []
        res = ''
        for ch in s:
            if ch in ch_dict:
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1
        for key, val in ch_dict.items():
            ch_list.append([val, key])
        ch_list = collections.deque(sorted(ch_list, key=lambda x: x[0], reverse=True))
        if (len(s) % 2 == 0 and ch_list[0][0] > len(s)/2) or (len(s) % 2 != 0 and ch_list[0][0] > (len(s)+1)/2):
            return ''
        while len(ch_list) > 1:
            first = ch_list.popleft()
            res += first[1]
            first[0] -= 1
            if first[0] > 0:
                ch_list.append(first)
            second = ch_list.popleft()
            res += second[1]
            second[0] -= 1
            if second[0] > 0:
                ch_list.append(second)
            ch_list = collections.deque(sorted(ch_list, key=lambda x: x[0], reverse=True))
        if len(ch_list) == 1:
            res += ch_list[0][1]
        return res

    def reorganizeStringEdit(self, S: str) -> str:

        max_dup = (len(S) + 1) // 2
        counts = collections.Counter(S)

        heap = []
        for c, f in counts.items():
            if f > max_dup:
                return ''
            heap.append([-f, c])
        heapq.heapify(heap)

        result = []
        while len(heap) > 1:
            first = heapq.heappop(heap)
            result.append(first[1])
            first[0] += 1
            second = heapq.heappop(heap)
            result.append(second[1])
            second[0] += 1

            if first[0] < 0:
                heapq.heappush(heap, first)
            if second[0] < 0:
                heapq.heappush(heap, second)

        if len(heap) == 1:
            result.append(heap[0][1])

        return ''.join(result)
# @lc code=end
# %%
# s = Solution()
# s.reorganizeStringOwn('abbcccddddeeeee')
# s.reorganizeStringOwn("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao")
# %%
