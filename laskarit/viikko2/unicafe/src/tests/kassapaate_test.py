import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.Maksukortti = Maksukortti(1000)

    def test_kassapaate_alustettu(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassapaate_kateismaksu_edullinen_lounas_kasvattaa_rahasaldoa_ja_laskee_vaihtorahan_suuruuden(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassapaate_kateismaksu_maukas_lounas_kasvattaa_rahasaldoa_ja_laskee_vaihtorahan_suuruuden(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_hyvaksytty_kateismaksu_edullinen_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_hyvaksytty_kateismaksu_maukas_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_hyvaksytty_kateismaksu_edullinen_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_edullinen_kaikki_rahat_palautetaan_ja_kassapaatteen_saldot_sailyvat_ennallaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_maukas_kaikki_rahat_palautetaan_ja_kassapaatteen_saldot_sailyvat_ennallaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_edullinen_hyvksytään_ja_kasvatetaan_lounaiden_maaraa(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.Maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_hyvksytään_ja_kasvatetaan_lounaiden_maaraa(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.Maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_edullinen_hylataan_ja_saldot_sailyvat_ennallaan(self):
        self.Maksukortti.ota_rahaa(900)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.Maksukortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_maukkaasti_hylataan_ja_saldot_sailyvat_ennallaan(self):
        self.Maksukortti.ota_rahaa(900)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.Maksukortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_ei_vaikuta_kassapaatteen_saldoon(self):
        self.kassapaate.syo_edullisesti_kortilla(self.Maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.Maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus_kasvattaa_kortin_ja_kassapaatteen_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.Maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.Maksukortti.saldo, 1100)

    def test_kortille_negatiivisen_saldon_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.Maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.Maksukortti.saldo, 1000)

    def test_kassassa_rahaa_method(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)