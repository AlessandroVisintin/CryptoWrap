from __future__ import annotations
from hashlib import sha256
from typing import List


class Node:
	"""
	Node of a binary tree.
	"""
	
	def __init__(self, left:Node, right:Node, value:str) -> Node:
		"""
		Args:
			left : left child of Node.
			right : right child of Node.
			value : value to be stored inside the node.
		"""
		self.left = left
		self.right = right
		self.value = value


class MerkleTree:
	"""
	Create a MerkleTree.
	"""
	
	def __init__(self, values: List[str]) -> MerkleTree:
		"""
		"""
		leaves = [
			Node(None, None, sha256(x.encode('utf-8')).hexdigest())
			for x in values
			]
		
		if len(leaves) % 2 == 1: # duplicate last element if odd
			leaves.append(leaves[-1])
		
		self.root = self._build(leaves)
	
	
	def _build(self, nodes: List[Node]) -> Node:
		"""
		Build Merkle tree recursively.
		
		Args:
			nodes : list of Node(s).
		
		Returns:
			parent node of the list.
		"""
		if  len(nodes) == 2:
			x = nodes[0].value + nodes[1].value
			return Node(nodes[0], nodes[1], sha256(x.encode('utf-8')).hexdigest())
		
		mid = len(nodes) // 2
		left = self._build(nodes[:mid])
		right = self._build(nodes[mid:])
		
		x = left.value + right.value
		value = sha256(x.encode('utf-8')).hexdigest()
		
		return Node(left, right, value)
		
			