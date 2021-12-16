import task1QuadEquaComplex as qec

class TestQuad:
    def test_quad_1_3_6(self):
        assert qec.quadratic_equation('1', '3', '6') == [-15.0, 2, (-1.5+1.9364916731037085j), (-1.5-1.9364916731037085j)]
    def test_quad_5_16_minus_6(self):
        assert qec.quadratic_equation('5', '16', '-6') == [376.0, 2, 0.33907194296653176, -3.539071942966532]
    def test_quad_5_1_minus_2j_minus_17(self):
        assert qec.quadratic_equation('5', '1-2j', '-17') == [(337-4j), 2, (1.7357883021148688+0.1891054976344715j), (-1.9357883021148687+0.2108945023655285j)]