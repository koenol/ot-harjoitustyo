import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_ota_rahaa_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_ota_rahaa_ei_vahenna_saldoa_jos_kate_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_negatiivinen_summa_ei_vahenna_saldoa(self):
        self.maksukortti.ota_rahaa(-100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0) 
    
    def test_negatiivinen_summa_ei_kasvata_saldoa(self):
        self.maksukortti.ota_rahaa(-100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_maksukortti_str(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")