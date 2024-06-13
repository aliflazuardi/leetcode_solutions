/* class Solution { */
/* public: */
/*     vector<int> productExceptSelf(vector<int>& nums) { */
/*         int product = 1; */
/*         int zeroCnt = 0; */
/*         for (const int& num : nums) { */
/*             if (num == 0) { */
/*                 zeroCnt++; */
/*                 continue; */
/*             } */
/*             product = product * num; */
/*         } */
/**/
/*         if (zeroCnt >= 2) { */
/*             for (int& num : nums) { */
/*                 num = 0; */
/*             } */
/*         } else if (zeroCnt == 1) { */
/*             for (int& num : nums) { */
/*                 if (num == 0) { */
/*                     num = product; */
/*                 } else { */
/*                     num = 0; */
/*                 } */
/*             } */
/*         } else { */
/*             for (int& num : nums) { */
/*                 num = product / num; */
/*             } */
/*         } */
/**/
/*         return nums; */
/*     } */
/* }; */

// O(N) without division
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);

        int prefix = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefix;
            prefix = prefix * nums[i];
        }

        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] = result[i] * postfix;
            postfix = postfix * nums[i];
        }

        return result;
    }
};
