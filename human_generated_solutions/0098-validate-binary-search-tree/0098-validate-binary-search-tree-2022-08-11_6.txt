def isValidBST(self, root: Optional[TreeNode]) -> bool:
	def check_validate(root, lower, upper):
		if not root:
			return True
		if lower >= root.val or upper <= root.val:
			return False
		else:
			return check_validate(root.left, lower, root.val) and check_validate(
				root.right, root.val, upper
			)

	return check_validate(root, -math.inf, math.inf)