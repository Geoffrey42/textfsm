import unittest
import textfsm

class TrackOptionTests(unittest.TestCase):
    def test_getException(self):
        files = [
            'cisco_show_run_part_address-family_ipv4_vrf_01.template',
            'show_run_part_address-family_ipv4_vrf_2_rcsw-ac1bb01.output.txt'
        ]

        with open(files[0], 'r') as template_file, open(files[1], 'r') as output_file:
            template = textfsm.TextFSM(template_file)
            output = f.read(output_file)

        with self.assertRaises(Exception):
            try:
                template = textfsm.TextFSM(output)
            except:
                pass
            else:
                raise Exception

if __name__ == '__main__':
    unittest.main()
