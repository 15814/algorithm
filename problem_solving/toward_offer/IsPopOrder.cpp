

class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        if (pushV.size() != popV.size()) {
            return false;
        }
        if (pushV.empty()) {
            return true;
        }
        stack<int> st;
        int idx = 0;

        for (size_t i = 0; i < popV.size(); i++) {

            if (st.empty()) {
                if (idx < pushV.size()) {
                    st.push(pushV[idx]);
                    idx++;
                }else{
                    return false;
                }
            }

            if (st.top()!= popV[i]) {
                bool found = false;
                for (int j = idx; j < pushV.size(); j++) {
                    st.push(pushV[j]);
                    if (pushV[j] == popV[i]) {
                        found = true;
                        idx = j+1;
                        break;
                    }
                }
                if (!found) {
                    return false;
                }
            }

            st.pop();

        }

        return true;
    }
};







//note
