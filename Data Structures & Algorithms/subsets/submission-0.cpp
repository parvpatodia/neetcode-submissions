class Solution {
public:
    void helper(vector<int>& nums,vector<vector<int>>& ans,vector<int>
    & subset,int index)
    {
        if(index==nums.size()){
            ans.push_back(subset);
            return;
        }

        //pick
        subset.push_back(nums[index]);
        helper(nums,ans,subset,index+1);
        subset.pop_back();


        //notpick
        helper(nums,ans,subset,index+1);

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> subset;
        helper(nums,ans,subset,0);
        return ans;
    }
};
