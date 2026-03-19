/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    if root == nil || root.Left == nil && root.Right == nil{
        return root;
    }

    left := invertTree(root.Left);
    right := invertTree(root.Right);

    root.Left = right;
    root.Right = left;

    return root;
}