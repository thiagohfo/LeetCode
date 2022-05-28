class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = {}
        keys_to_del = []

        for i in arr:
            if i in str_dict:
                str_dict[i] += 1
            else:
                str_dict[i] = 1

        for key, value in str_dict.items():
            if value > 1:
                keys_to_del.append(key)

        for i in keys_to_del:
            del str_dict[i]

        list_keys = [key for key in str_dict.keys()]

        if len(list_keys) >= k:
            return list_keys[k - 1]
        else:
            return ""