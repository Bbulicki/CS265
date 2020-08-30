#!/usr/bin/env python3
# test_gInt.py - Unit test for Unit Class
#
# Brandin Bulicki
#
#
#


import sys
import unittest

from gInt import gInt

class gIntTest( unittest.TestCase ) :
	'''Tests for gInt Class'''
	
	def setUp( self ) :
		'''Optional.  Run before each test'''
		self.u1 = gInt( 3, -2 )
		self.u2 = gInt( 2, 5 )
		self.u3 = gInt( 13 )
		
	def test_add( self ) :
		r = self.u1 + self.u2
		
		self.assertEqual(r, gInt(5, 3), 'Addition Failed')

		r = self.u1 + self.u3

		self.assertEqual(r, gInt(16, -2), 'Addition of real and negative imaginary + real failed')

		r = self.u2 + self.u3

		self.assertEqual(r, gInt(15, 5), 'Addition of positive real and imaginary + real failed')

	def test_mul( self ) :
		r = self.u1 * self.u2

		self.assertEqual(r, gInt(16, 11), 'Multiplication Failed')

		r = self.u2 * self.u3

		self.assertEqual(r, gInt(26, 65), 'Multiplication of positive real and imaginary * real failed')

	def test_norm( self ) :
		r = self.u1.norm()

		self.assertEqual(r, 13, 'Norm Failed')

		r = self.u2.norm()
		self.assertEqual(r, 29, 'Norm Failed')

		r = self.u3.norm()
		self.assertEqual(r, 169, 'Norm Failed')
if __name__ == '__main__' :
	sys.argv.append( '-v' )
	unittest.main()
