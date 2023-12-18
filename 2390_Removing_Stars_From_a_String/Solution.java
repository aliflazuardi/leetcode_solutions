class Solution {

    Stack<Character> stack = new Stack<Character>();

    public String removeStars(String s) {
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '*') {
                stack.pop();
            } else {
            stack.add(s.charAt(i));

            }
        }

        String ans = "";

        while(!stack.isEmpty()) {
            ans = stack.pop() + ans;
        }


        return ans;
    }
}