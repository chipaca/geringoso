# Copyright 2020 John Lenton
# Licensed under GPLv3, see LICENSE file for details.

import unittest

from geringoso import _pe, geringoso

class Test(unittest.TestCase):
    def test_pe(self):
        for win, wout in {
                'jo': 'jopo',
                'sol': 'sopol',
                'que': 'quepe',
                'guai': 'guapai',
                'guay': 'guapay',
                'viei': 'viepei',
                'ciu': 'ciupu',
                'pst': 'pst',
                'rin': 'ripin',
                'muy': 'mupuy',
                'y': 'ipy',
                }.items():
            with self.subTest(win=win):
                self.assertEqual(_pe(win), wout)

    def test_geringoso(self):
        for win, wout in {
                'hola': 'hopolapa',
                'geringoso': 'geperipingoposopo',
                'ciudad': 'ciupudapad',
                'ñoñé': 'ñopoñépe',
                'a\N{COMBINING ACUTE ACCENT}rbol': 'áparbopol',
                }.items():
            with self.subTest(win=win):
                self.assertEqual(geringoso(win), wout)
