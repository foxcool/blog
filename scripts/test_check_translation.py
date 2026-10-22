import re
import unittest

import check_translation as ct


class ProseTest(unittest.TestCase):
    def test_skips_front_matter_code_and_quotes(self):
        text = '---\ntitle: "x"\n---\nBody "Navigating the Surge" here\n```\ncrucial\n```\n'
        lines = ct.prose(text)
        self.assertEqual([no for no, _ in lines], [4])
        self.assertNotIn("Navigating", lines[0][1])

    def test_keeps_link_text_drops_url(self):
        (_, line), = ct.prose("See [the realm](https://x.io/robust)")
        self.assertIn("realm", line)
        self.assertNotIn("robust", line)


class MetricsTest(unittest.TestCase):
    def test_not_but_matches_dash_and_but(self):
        self.assertEqual(len(ct.NOT_BUT_RE.findall("It is not BTC — it's ETH. Not gold but debt.")), 2)

    def test_not_but_stays_inside_sentence(self):
        self.assertEqual(ct.NOT_BUT_RE.findall("It is not over. But later."), [])

    def test_leverage_is_not_a_cliche(self):
        self.assertIsNone(ct.CLICHE_RE.search("banks add leverage"))


class GlossaryTest(unittest.TestCase):
    glossary = [(re.compile("храпови", re.I), re.compile("ratchet effect", re.I))]

    def test_missing_term_reported(self):
        self.assertEqual(ct.missing_terms("эффект храповика", "a lock-in effect", self.glossary),
                         ["ratchet effect"])

    def test_term_absent_in_original_is_ignored(self):
        self.assertEqual(ct.missing_terms("ничего", "nothing", self.glossary), [])

    def test_glossary_file_parses(self):
        self.assertTrue(ct.load_glossary())


if __name__ == "__main__":
    unittest.main()
