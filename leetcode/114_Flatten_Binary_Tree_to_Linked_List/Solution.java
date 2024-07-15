/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.Stack;

class Solution {

    Stack<TreeNode> stack = new Stack<TreeNode>();

    public void flatten(TreeNode root) {
        if(root == null) {
        } else {
            if(root.right != null) {
                stack.push(root.right);
            }
            if(root.left != null) {
                root.right = root.left;
                stack.push(root.left);
                root.left = null;
            }

            while(!stack.isEmpty()) {
                TreeNode curr = stack.pop();
                if(curr.right != null) {
                    stack.push(curr.right);
                }
                
                if(curr.left != null) {
                    curr.right = curr.left;
                    stack.push(curr.left);
                    curr.left = null;
                } else {
                    if(!stack.isEmpty())
                        curr.right = stack.peek();
                }
            }
        }

        


    }
}