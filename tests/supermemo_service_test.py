import unittest

from src.service.supermemo_service import clear_content_str


class TestSupermemoService(unittest.TestCase):
    def test_clear_content_str_case_short_html_tag(self):
        given = 'Comprehensive<br>'

        actual = clear_content_str(given)

        self.assertEqual('Comprehensive', actual)

    def test_clear_content_str_case_html_decoded(self):
        given = '&#1042;&#1089;&#1077;&#1086;&#1073;&#1098;&#1077;&#1084;&#1083;&#1102;&#1097;&#1080;&#1081;'

        actual = clear_content_str(given)

        self.assertEqual('Всеобъемлющий', actual)

    def test_clear_content_str_case_full_html_tag(self):
        given = '<span lang="EN-US">A failure&#160;</span>'

        actual = clear_content_str(given)

        self.assertEqual('A failure', actual)

    def test_clear_content_str_case_inner_html_tag(self):
        given = '<p class="MsoNormal"><span>An affiliation</span></p>'

        actual = clear_content_str(given)

        self.assertEqual('An affiliation', actual)

    def test_clear_content_str_case_html_encoded_with_apostrophe(self):
        given = 'Master&#8217;s&#10;thesis'

        actual = clear_content_str(given)

        self.assertEqual('Master’s thesis', actual)

    def test_clear_content_str_case_html_tag_with_inner_encoded(self):
        given = '<p class="MsoNormal"><span>Master&#8217;s&#10;thesis</span></p>'

        actual = clear_content_str(given)

        self.assertEqual('Master’s thesis', actual)

    def test_clear_content_str_case_html_tag_with_inner_encoded_spaces_case_1(self):
        given = '<span lang="EN-US">Turnover&#160;of goods</span><span lang="EN-US"></span>'

        actual = clear_content_str(given)

        self.assertEqual('Turnover of goods', actual)

    def test_clear_content_str_case_html_tag_with_inner_encoded_spaces_case_2(self):
        given = '<span lang="EN-US">A&#160;</span><span lang="EN-US">sole</span><span lang="EN-US"> </span><span lang="EN-US">trader</span>'

        actual = clear_content_str(given)

        self.assertEqual('A sole trader', actual)


if __name__ == "__main__":
    unittest.main()
